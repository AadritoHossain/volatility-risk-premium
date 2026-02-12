import yfinance as yf


def get_spy_price():
    spy = yf.Ticker("SPY")
    data = spy.history(period="1d")
    return data["Close"].iloc[-1]


def get_spy_options(expiry):
    spy = yf.Ticker("SPY")
    opt = spy.option_chain(expiry)
    return opt.calls
