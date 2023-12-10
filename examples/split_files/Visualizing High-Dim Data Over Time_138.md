# Generate synthetic data
synthetic_data = generate_synthetic_data()
synthetic_data.head()
== Output ==
## Dataframe Summary

Number of Rows: 5

Number of Columns: 4

### Column Information

|    | Column Name   | Data Type   |   Missing Values |   % Missing |
|----|---------------|-------------|------------------|-------------|
|  0 | x             | float64     |                0 |           0 |
|  1 | y             | float64     |                0 |           0 |
|  2 | time          | int64       |                0 |           0 |
|  3 | branch        | int64       |                0 |           0 |

### Categorical Summary

| Column Name   |
|---------------|

### Sample Data (5x4)

|    |   branch |        y |         x |   time |
|----|----------|----------|-----------|--------|
|  3 |        0 | 3.3091   | -2.53949  |      3 |
|  1 |        0 | 1.90009  | -1.1711   |      1 |
|  4 |        0 | 3.70637  | -1.74274  |      4 |
|  0 |        0 | 0.981038 | -0.266003 |      0 |
|  2 |        0 | 2.51248  | -1.85003  |      2 |


==== Cell ID: 72c5ac2d-c114-4d0a-ad68-57bd498be7a8
Cell Type: code
Cell State: finished_with_no_error
== Source ==
