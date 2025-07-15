# File: main.py

from flask import Flask, jsonify, render_template, request
from modules.utils import ASSETS
from modules.data_fetch import get_signals, get_history   # <--- import get_history

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('dashboard_v3.html')

@app.route('/api/signals')
def api_signals():
    return jsonify([get_signals(s) for s in ASSETS])

# ─── New history endpoint ────────────────────────────────────────────────
@app.route('/api/history/<symbol>')
def api_history(symbol):
    # allow ?period=1mo&interval=1h overrides
    period   = request.args.get('period',   '3mo')
    interval = request.args.get('interval', '1d')
    df = get_history(symbol, period, interval)
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
