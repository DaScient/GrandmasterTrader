# File: modules/data_fetch.py

import yfinance as yf
import ccxt
from .indicators import compute_indicators
from .sentiment import get_news_sentiment
from .predictive import monte_carlo
from modules.utils import ASSETS

exchange = ccxt.binance({'enableRateLimit': True})

def fetch_price(symbol):
    """
    Fetch live price for a symbol. Crypto via CCXT; otherwise try 1m intraday then daily close.
    """
    if symbol.endswith('-USD'):
        try:
            return exchange.fetch_ticker(symbol)['last']
        except Exception:
            pass

    # Try intraday 1m
    try:
        df_min = yf.Ticker(symbol).history(period='1d', interval='1m')
        if not df_min.empty:
            return df_min['Close'].iloc[-1]
    except Exception:
        pass

    # Fallback to daily close
    try:
        df_day = yf.Ticker(symbol).history(period='1d')
        if not df_day.empty:
            return df_day['Close'].iloc[-1]
    except Exception:
        pass

    return 0.0

def get_signals(symbol):
    df = yf.Ticker(symbol).history(period='3mo', interval='1d')
    df = compute_indicators(df)

    live = fetch_price(symbol)
    sent = get_news_sentiment(symbol)
    p10, p50, p90 = monte_carlo(df['Close'], days=5, sims=500)

    target = round(p90, 2)
    upside = round((target - live) / live * 100, 2)

    sig = 'Hold'
    if df['rsi'].iloc[-1] < 30 and df['ao'].iloc[-1] > 0:
        sig = 'Buy'
    if df['rsi'].iloc[-1] > 70:
        sig = 'Sell'

    return {
        'symbol': symbol,
        'current_price': round(live, 2),
        'rsi': round(df['rsi'].iloc[-1], 2),
        'ao': round(df['ao'].iloc[-1], 2),
        'sentiment': round(sent, 2),
        'target_price': target,
        'upside_pct': upside,
        'signal': sig
    }

def get_history(symbol, period: str = '3mo', interval: str = '1d'):
    """
    Returns a DataFrame with columns:
      Date, Open, High, Low, Close, rsi, ao, forecast_low, forecast_mid, forecast_high
    """
    df = yf.Ticker(symbol).history(period=period, interval=interval)
    df = compute_indicators(df)
    # Monte Carlo forecast on Close
    p10, p50, p90 = monte_carlo(df['Close'], days=7, sims=500)
    df['forecast_low']    = p10
    df['forecast_mid']    = p50
    df['forecast_high']   = p90
    df = df.reset_index().rename(columns={'index':'Date'})
    # Trim to JSON-friendly columns
    return df[[
      'Date','Open','High','Low','Close','rsi','ao',
      'forecast_low','forecast_mid','forecast_high'
    ]]
