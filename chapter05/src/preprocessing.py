"""Chapter 05 전처리 모듈.

Notebook에서 셀 단위로 실행하던 전처리 규칙을 함수로 옮긴 것이다.
"""
from pathlib import Path

import pandas as pd

TABLE_NAMES = ["customers", "products", "orders", "order_items"]

PRIMARY_KEYS = {
    "customers": "customer_id",
    "products": "product_id",
    "orders": "order_id",
    "order_items": "order_item_id",
}

status_map = {
    "complete": "completed",
    "Complete": "completed",
    "COMPLETED": "completed",
    "완료": "completed",
    "cancel": "cancelled",
    "Cancel": "cancelled",
    "CANCELLED": "cancelled",
    "취소": "cancelled",
    "refund": "refunded",
    "Refund": "refunded",
    "REFUNDED": "refunded",
    "환불": "refunded",
}


# ---------------------------------------------------------------------------
# 도우미 함수
# ---------------------------------------------------------------------------
def strip_string_columns(df):
    """문자열 컬럼의 앞뒤 공백을 제거한다. (원본 DataFrame은 바꾸지 않는다.)"""
    result = df.copy()
    # 'object'만 쓰면 pandas 4 경고가 나므로 'string'도 함께 지정한다.
    string_columns = result.select_dtypes(include=["object", "string"]).columns
    for column in string_columns:
        result[column] = result[column].apply(
            lambda value: value.strip() if isinstance(value, str) else value
        )
    return result


def to_number(series):
    """천 단위 쉼표를 제거하고 숫자로 변환한다. 변환 불가 값은 NaN."""
    return pd.to_numeric(
        series.astype(str).str.replace(",", "", regex=False),
        errors="coerce",
    )


# ---------------------------------------------------------------------------
# 테이블별 전처리 (Notebook 함수 그대로)
# ---------------------------------------------------------------------------
def preprocess_customers(df):
    result = strip_string_columns(df)

    if "age" in result.columns:
        result["age"] = pd.to_numeric(result["age"], errors="coerce")
        result["age"] = result["age"].fillna(result["age"].median())

    if "city" in result.columns:
        result["city"] = result["city"].fillna("Unknown")

    if "signup_date" in result.columns:
        result["signup_date"] = pd.to_datetime(result["signup_date"], errors="coerce")

    return result.drop_duplicates()


def preprocess_products(df):
    result = strip_string_columns(df)

    if "price" in result.columns:
        result["price"] = to_number(result["price"])
        result = result[result["price"] > 0]

    return result.drop_duplicates()


def preprocess_orders(df):
    result = strip_string_columns(df)

    if "order_status" in result.columns:
        result["order_status"] = result["order_status"].replace(status_map)

    if "order_date" in result.columns:
        result["order_date"] = pd.to_datetime(result["order_date"], errors="coerce")
        result["order_month"] = result["order_date"].dt.to_period("M").astype(str)
        result["order_dayofweek"] = result["order_date"].dt.day_name()

    return result.drop_duplicates()


def preprocess_order_items(df):
    result = strip_string_columns(df)

    if "quantity" in result.columns:
        result["quantity"] = to_number(result["quantity"])
        result = result[result["quantity"] > 0].copy()

    if "unit_price" in result.columns:
        result["unit_price"] = to_number(result["unit_price"])
        result = result[result["unit_price"] > 0].copy()

    if {"quantity", "unit_price"}.issubset(result.columns):
        result["line_total"] = result["quantity"] * result["unit_price"]

    return result.drop_duplicates()


# ---------------------------------------------------------------------------
# 전체 파이프라인
# ---------------------------------------------------------------------------
def preprocess_sales_data(raw):
    """raw: {'customers': df, ...} -> 같은 형태의 전처리 결과 dict."""
    return {
        "customers": preprocess_customers(raw["customers"]),
        "products": preprocess_products(raw["products"]),
        "orders": preprocess_orders(raw["orders"]),
        "order_items": preprocess_order_items(raw["order_items"]),
    }


def validate_relationships(processed):
    """FK가 부모 테이블에 없는 행 수를 센다."""
    customers = processed["customers"]
    products = processed["products"]
    orders = processed["orders"]
    order_items = processed["order_items"]

    invalid_customers = orders[~orders["customer_id"].isin(customers["customer_id"])]
    invalid_orders = order_items[~order_items["order_id"].isin(orders["order_id"])]
    invalid_products = order_items[~order_items["product_id"].isin(products["product_id"])]

    return pd.DataFrame(
        {
            "check": [
                "orders.customer_id exists in customers.customer_id",
                "order_items.order_id exists in orders.order_id",
                "order_items.product_id exists in products.product_id",
            ],
            "invalid_count": [
                len(invalid_customers),
                len(invalid_orders),
                len(invalid_products),
            ],
        }
    )


def compare_shapes(raw, processed):
    """처리 전/후 행·열 수 비교표."""
    rows = []
    for name in TABLE_NAMES:
        rows.append(
            {
                "dataset": name,
                "rows_raw": raw[name].shape[0],
                "columns_raw": raw[name].shape[1],
                "rows_processed": processed[name].shape[0],
                "columns_processed": processed[name].shape[1],
            }
        )
    return pd.DataFrame(rows)


def duplicate_summary(data, key_columns=None):
    """전체 행 중복과 PK 중복 건수.

    key_columns: {'테이블명': 'PK 컬럼명'} 형태의 dict. 생략하면 기본 PK를 쓴다.
    """
    key_columns = key_columns or PRIMARY_KEYS
    rows = []
    for name in TABLE_NAMES:
        df = data[name]
        key = key_columns.get(name)
        rows.append(
            {
                "dataset": name,
                "full_row_duplicates": int(df.duplicated().sum()),
                "primary_key": key,
                "key_duplicates": int(df[key].duplicated().sum())
                if key in df.columns
                else None,
            }
        )
    return pd.DataFrame(rows)


def save_processed_data(processed, output_dir):
    """전처리 결과를 <name>_clean.csv로 저장하고 경로 목록을 반환한다."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = []
    for name in TABLE_NAMES:
        path = output_dir / f"{name}_clean.csv"
        processed[name].to_csv(path, index=False, encoding="utf-8-sig")
        paths.append(path)
    return paths


def build_preprocessing_report(raw, processed, relationship_checks=None, comparison=None):
    """전처리 요약 보고서(Markdown 문자열)를 만든다."""
    if comparison is None:
        comparison = compare_shapes(raw, processed)
    if relationship_checks is None:
        relationship_checks = validate_relationships(processed)

    lines = [
        "# Chapter 05 전처리 요약",
        "",
        "## 처리 전/후 shape",
        "",
        comparison.to_markdown(index=False),
        "",
        "## 처리 후 관계 검증",
        "",
        relationship_checks.to_markdown(index=False),
        "",
        "## 처리 전 중복 요약",
        "",
        duplicate_summary(raw).to_markdown(index=False),
        "",
    ]
    return "\n".join(lines)