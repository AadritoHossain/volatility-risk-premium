import numpy as np
from scipy.optimize import brentq
from src.black_scholes import bs_call_price


def implied_vol_call(market_price, S, K, T, r):

    def objective(sigma):
        return bs_call_price(S, K, T, r, sigma) - market_price

    try:
        iv = brentq(objective, 1e-6, 5.0)
        return iv
    except ValueError:
        return np.nan
