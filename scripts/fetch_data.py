import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.data.loader import download_option_chain, download_underlying_history, save_dataframe


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch underlying history and option chain data.")
    parser.add_argument("symbol", type=str, help="Ticker symbol, e.g. SPY or AAPL")
    parser.add_argument("--start", type=str, default=None, help="Start date for history, e.g. 2023-01-01")
    parser.add_argument("--end", type=str, default=None, help="End date for history, e.g. 2024-01-01")
    parser.add_argument("--expiry", type=str, default=None, help="Option expiry date to fetch, e.g. 2024-06-21")
    parser.add_argument("--data-dir", type=str, default="data/raw", help="Directory to save downloaded CSV files")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading {args.symbol} price history...")
    history = download_underlying_history(args.symbol, start=args.start, end=args.end)
    history_path = data_dir / f"{args.symbol}_history.csv"
    save_dataframe(history, history_path)
    print(f"Saved underlying history to {history_path}")

    print(f"Downloading {args.symbol} option chain...")
    option_data = download_option_chain(args.symbol, expiry=args.expiry)
    if isinstance(option_data, dict):
        for exp, df in option_data.items():
            path = data_dir / f"{args.symbol}_options_{exp}.csv"
            save_dataframe(df, path)
            print(f"Saved option chain for {exp} to {path}")
    else:
        path = data_dir / f"{args.symbol}_options_{args.expiry}.csv"
        save_dataframe(option_data, path)
        print(f"Saved option chain for {args.expiry} to {path}")


if __name__ == "__main__":
    main()
