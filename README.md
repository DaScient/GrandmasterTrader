# GrandmasterTrader | TradePulse Live v3

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**TradePulse Live v3** is a real-time market analytics dashboard, delivering live prices, technical indicators, sentiment scores, Monte Carlo forecasts and dynamic Buy/Hold/Sell signals for stocks, OTC tickers, crypto & forex.

## 🚀 Features

- 🌐 **Live price feeds** via Yahoo Finance (stocks/forex) & CCXT (crypto)  
- 📊 **Technical Indicators**: RSI & Awesome Oscillator + Golden Cross detection  
- 📰 **Sentiment Analysis**: VADER-powered headlines from Yahoo Finance RSS  
- 🔮 **Monte Carlo Forecasts**: 10th/50th/90th percentile price simulations  
- 🔔 **Signals**: Simple RSI+AO rules drive Buy/Hold/Sell recommendations  
- 📈 **Interactive Drill-Down**: Click any symbol to view Plotly candlestick charts, indicator overlays, forecast bands with zoom/pan and time-range selectors  
- 🔄 **Auto-Refresh**: Table & charts update automatically every 15 seconds  

## 🛠️ Prerequisites

- Python 3.8+  
- pip  
- (Optional) a brokerage API key for extended data

## ⚙️ Installation

```bash
# 1. Clone repo
git clone https://github.com/yourusername/GrandmasterTrader.git
cd GrandmasterTrader

# 2. Setup virtualenv
python3 -m venv venv
source venv/bin/activate          # macOS/Linux
venv\Scripts\activate             # Windows

# 3. Install dependencies
pip install -r requirements.txt
