# File: modules/indicators.py

import pandas as pd
import numpy as np

def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

def ao(high: pd.Series, low: pd.Series) -> pd.Series:
    median = (high + low) / 2
    sma5  = median.rolling(window=5).mean()
    sma34 = median.rolling(window=34).mean()
    return sma5 - sma34

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['rsi'] = rsi(df['Close'])
    df['ao']  = ao(df['High'], df['Low'])
    df['ma50']  = df['Close'].rolling(window=50).mean()
    df['ma200'] = df['Close'].rolling(window=200).mean()
    df['golden_cross'] = (
        (df['ma50'].shift(1) < df['ma200'].shift(1)) &
        (df['ma50'] > df['ma200'])
    )
    return df
