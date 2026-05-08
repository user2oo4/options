import pandas as pd

from src.data.loader import clean_option_chain


def test_clean_option_chain_computes_mid():
    df = pd.DataFrame(
        {
            "bid": [1.0, 2.5],
            "ask": [1.2, 2.7],
            "strike": [100, 110],
            "expiry": ["2024-06-21", "2024-06-21"],
            "lastPrice": [1.1, 2.6],
            "volume": [10, 5],
            "openInterest": [15, 8],
            "impliedVolatility": [0.22, 0.25],
        }
    )

    result = clean_option_chain(df)

    assert "mid" in result.columns
    assert result.loc[0, "mid"] == 1.1
    assert result.loc[1, "mid"] == 2.6
    assert pd.api.types.is_datetime64_any_dtype(result["expiry"])
