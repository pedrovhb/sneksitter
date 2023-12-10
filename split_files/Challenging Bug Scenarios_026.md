---
file: /home/pedro/Documents/chatgpt_export/Markdown/Challenging Bug Scenarios.md
heading_stack: <root> -> 16b4f038-f461-4bea-aab3-f16d97102976 -> System -> f030f68c-1381-4970-ab86-0ddb5dbec373 -> System -> aaa2a9a6-bc09-4eb8-ade3-de667199f255 -> User -> 297b2268-6318-4cbd-8782-30c76dd52aa2 -> Assistant -> Scenario 1: Race Condition in Multithreading -> Scenario 2: Memory Leak -> Scenario 3: Heisenbug (Behavior changes under observation) -> Scenario 4: Non-Deterministic Behavior -> aaa2da28-e469-4aab-accc-b52d7aa18433 -> User -> 24b2a49b-4ec7-4808-8cb2-7a985f77921f -> Assistant -> Scenario 1: Nested Async Calls Hiding a Deadlock -> Scenario 2: Data Corruption due to Inconsistent Global State -> Scenario 3: Intermittent Failure due to Uninitialized Variable -> Scenario 4: Floating-Point Error in Financial Calculation -> aaa2f2f6-ffae-4515-a01d-078e412919d2 -> User -> ea8eacaa-5157-4848-b99b-ba96457a30cb -> Assistant -> Possible Ideas for Complex Scenario -> Selected Scenario: Time Series Data Analysis for Stock Prices
---
### Selected Scenario: Time Series Data Analysis for Stock Prices

The program reads time-series data for stock prices and performs various calculations to predict future prices. It uses a sliding window mechanism to calculate moving averages, volatility, and other metrics. The bug occurs under very specific conditions: it gives incorrect predictions for stocks with ticker symbols containing numerical characters, but only during market opening times.

Here's the code for the selected scenario:

```python
import datetime
import random
from typing import List, Dict

# Simulated stock data
stock_data = {
    "AAPL": [150 + random.uniform(-1, 1) for _ in range(100)],
    "GOOGL": [2800 + random.uniform(-10, 10) for _ in range(100)],
    "TSLA3": [650 + random.uniform(-5, 5) for _ in range(100)]  # Notice the numerical character
}

def is_market_open() -> bool:
    # Let's assume the market is open from 9:30 to 16:00
    current_time = datetime.datetime.now().time()
    return current_time >= datetime.time(9, 30) and current_time <= datetime.time(16, 0)

def moving_average(data: List[float], window_size: int) -> float:
    return sum(data[-window_size:]) / window_size

def predict_stock_price(ticker: str) -> float:
    data = stock_data.get(ticker, [])
    if not data:
        return 0.0

    # Twist: Incorrect calculations only for tickers containing numerical characters
    # and during market opening times (9:30 to 10:00)
    if any(char.isdigit() for char in ticker) and \
       datetime.datetime.now().time() <= datetime.time(10, 0) and \
       is_market_open():
        return moving_average(data, 20)  # Incorrect: should be a more complex calculation
    else:
        return moving_average(data, 50)  # Correct calculation

def main():
    tickers_to_predict = ["AAPL", "GOOGL", "TSLA3"]
    predictions: Dict[str, float] = {}

    for ticker in tickers_to_predict:
        predictions[ticker] = predict_stock_price(ticker)

    for ticker, prediction in predictions.items():
        print(f"Predicted price for {ticker}: ${prediction:.2f}")

if __name__ == "__main__":
    main()
```

In this program, the bug is well-hidden among various realistic functionalities. It only occurs for stock tickers with numerical characters and during the first 30 minutes of market opening time. Even then, it manifests as a subtle miscalculation rather than an outright failure.

[child ⬇️](#aaa2c237-68df-47bf-9959-baeb804e76b0)

---

(main branch ⎇)
###### aaa2c237-68df-47bf-9959-baeb804e76b0
[parent ⬆️](#ea8eacaa-5157-4848-b99b-ba96457a30cb)
