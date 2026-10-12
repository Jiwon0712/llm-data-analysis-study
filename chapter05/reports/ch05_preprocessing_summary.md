# Chapter 05 전처리 요약

## 처리 전/후 shape

| dataset     |   rows_raw |   columns_raw |   rows_processed |   columns_processed |
|:------------|-----------:|--------------:|-----------------:|--------------------:|
| customers   |        150 |             6 |              150 |                   6 |
| products    |        100 |             4 |              100 |                   4 |
| orders      |        300 |             5 |              300 |                   7 |
| order_items |        764 |             5 |              764 |                   6 |

## 처리 후 관계 검증

| check                                                |   invalid_count |
|:-----------------------------------------------------|----------------:|
| orders.customer_id exists in customers.customer_id   |               0 |
| order_items.order_id exists in orders.order_id       |               0 |
| order_items.product_id exists in products.product_id |               0 |

## 처리 전 중복 요약

| dataset     |   full_row_duplicates | primary_key   |   key_duplicates |
|:------------|----------------------:|:--------------|-----------------:|
| customers   |                     0 | customer_id   |                0 |
| products    |                     0 | product_id    |                0 |
| orders      |                     0 | order_id      |                0 |
| order_items |                     0 | order_item_id |                0 |
