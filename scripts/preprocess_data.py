"""chapter05 전처리를 한 번에 실행한다.

사용법 (저장소 루트에서):
    python scripts/preprocess_data.py
    python scripts/preprocess_data.py --raw-dir chapter05/data/raw
"""
import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CHAPTER_DIR = REPO_ROOT / "chapter05"
sys.path.insert(0, str(CHAPTER_DIR))  # chapter05/src 를 import 할 수 있게 한다.

from src.data_loader import load_sales_data  # noqa: E402
from src.preprocessing import (  # noqa: E402
    build_preprocessing_report,
    compare_shapes,
    duplicate_summary,
    preprocess_sales_data,
    save_processed_data,
    validate_relationships,
)

PROCESSED_DIR = CHAPTER_DIR / "data" / "processed"
REPORT_PATH = CHAPTER_DIR / "reports" / "ch05_preprocessing_summary.md"


def find_raw_dir(raw_dir_arg=None):
    """원본 CSV가 있는 폴더를 찾는다."""
    if raw_dir_arg:
        return Path(raw_dir_arg)
    candidates = [CHAPTER_DIR / "data" / "raw", CHAPTER_DIR / "data"]
    for candidate in candidates:
        if (candidate / "customers.csv").exists():
            return candidate
    raise FileNotFoundError(
        "원본 CSV(customers.csv 등)를 찾지 못했습니다. "
        "--raw-dir 옵션으로 폴더를 지정하세요. 확인한 위치: "
        + ", ".join(str(c) for c in candidates)
    )


def main():
    parser = argparse.ArgumentParser(description="chapter05 전처리 실행")
    parser.add_argument("--raw-dir", default=None, help="원본 CSV 폴더")
    args = parser.parse_args()

    try:
        import tabulate  # noqa: F401  (보고서의 to_markdown에 필요)
    except ImportError:
        sys.exit("tabulate 패키지가 필요합니다: pip install tabulate")

    raw_dir = find_raw_dir(args.raw_dir)
    print(f"원본 폴더: {raw_dir}")

    raw = load_sales_data(raw_dir)
    processed = preprocess_sales_data(raw)

    comparison = compare_shapes(raw, processed)
    relationship_checks = validate_relationships(processed)

    print("\n[처리 전/후 shape]")
    print(comparison.to_string(index=False))
    print("\n[처리 후 관계 검증]")
    print(relationship_checks.to_string(index=False))
    print("\n[처리 후 중복 요약]")
    print(duplicate_summary(processed).to_string(index=False))

    saved_paths = save_processed_data(processed, PROCESSED_DIR)
    print("\n[저장된 clean CSV]")
    for path in saved_paths:
        print(" -", path)

    report = build_preprocessing_report(
        raw,
        processed,
        relationship_checks=relationship_checks,
        comparison=comparison,
    )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print("\n요약 보고서 저장 완료:", REPORT_PATH)


if __name__ == "__main__":
    main()