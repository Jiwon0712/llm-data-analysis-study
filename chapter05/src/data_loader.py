"""원본 CSV 로더."""
from pathlib import Path

import pandas as pd

TABLE_NAMES = ["customers", "products", "orders", "order_items"]


def load_sales_data(raw_dir):
    """raw_dir 안의 <name>.csv 4개를 읽어 {'customers': df, ...} 로 반환한다."""
    raw_dir = Path(raw_dir)
    data = {}
    for name in TABLE_NAMES:
        path = raw_dir / f"{name}.csv"
        if not path.exists():
            raise FileNotFoundError(f"원본 파일을 찾을 수 없습니다: {path}")
        # utf-8-sig는 BOM이 있는 파일과 없는 파일을 모두 읽는다.
        data[name] = pd.read_csv(path, encoding="utf-8-sig")
    return data