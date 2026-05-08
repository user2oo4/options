# Options

## General
Learn and test out different option pricing models, testing out different strategies.

## Getting started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Download data:

```bash
python3 scripts/fetch_data.py SPY --start 2024-01-01 --end 2024-05-01 --expiry 2024-06-21
```
OR

```bash
python3 -m scripts.fetch_data SPY --start 2024-01-01 --end 2024-05-01 --expiry 2024-06-21
```

3. See data at `data/raw/`.

## What this repo contains

- `src/data/loader.py`: functions to download price history and option chain data using `yfinance`
- `scripts/fetch_data.py`: command-line script to save raw CSVs
- `tests/test_data_loader.py`: simple test for option chain cleaning




