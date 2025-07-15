# File: modules/predictive.py

import numpy as np

def monte_carlo(series, days=7, sims=500):
    """
    Perform a Monte Carlo forecast on a price series.
    Returns the 10th, 50th, and 90th percentile of simulated end prices.
    """
    returns = series.pct_change().dropna()
    mu = returns.mean()
    sigma = returns.std()
    last_price = series.iloc[-1]

    results = []
    for _ in range(sims):
        path = last_price * np.cumprod(1 + np.random.normal(mu, sigma, days))
        results.append(path[-1])

    return np.percentile(results, [10, 50, 90])
