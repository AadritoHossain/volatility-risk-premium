# Volatility Risk Premium and Factor Timing Using Black–Scholes Implied Volatility - Aadrito Hossain

## 1. Introduction
This project was developed as part of independent preparation for graduate study in financial engineering.I am very motivated to learn and have been teaching myself how to code and to understand Quant Finance.
I have used AI to help me build this. Majority of AI use was to debug issues and to help me write professional interpretation of my data. Transparency is very important to me and I will not take full credit for this. However, this project was created for me to learn through actions and sometimes help is need to learn something this complex.
Understanding and managing volatility risk is central to quantitative finance.
Option-implied volatility reflects market expectations of future uncertainty,
while realized volatility captures ex-post risk.
This study examines the relationship between implied and realized volatility
and investigates whether volatility regimes contain information about future market performance.

## 2. Theoretical Framework

We employ the Black–Scholes model for European call options under the assumptions
of lognormal asset price dynamics, constant volatility, and frictionless markets.
Although these assumptions are known to be violated in practice,
the framework provides a tractable baseline for option valuation.

Implied volatility is obtained by numerically inverting the Black–Scholes pricing equation
using Brent’s root-finding method.

## 3. Data

Daily SPY price data and option chains are obtained from Yahoo Finance.
Options are filtered to exclude illiquid contracts with zero bid-ask spreads.
Near at-the-money options with approximately one month to maturity are selected
to ensure numerical stability.

Due to data limitations, historical option chains are unavailable.
Accordingly, implied volatility analysis is based on contemporaneous market data,
while realized volatility is computed from historical returns.

## 4. Methodology

Realized volatility is computed as the annualized rolling standard deviation
of daily returns over a 21-day window.

Implied volatility is extracted from option mid-prices using the Black–Scholes framework.
Volatility smiles are constructed by calibrating implied volatility across strikes.

Market regimes are classified based on realized volatility relative to its
historical mean and standard deviation.

## 5. Empirical Results

The implied volatility surface exhibits pronounced skew and curvature,
indicating systematic deviations from the constant-volatility assumption.

Realized volatility displays significant right-skewness, with elevated levels
during periods of market stress.

Regime-based analysis reveals that high-volatility periods are associated
with negative average returns and poor risk-adjusted performance,
while normal regimes exhibit strong positive returns.

## 6. Discussion

The observed volatility skew reflects asymmetric downside risk
and investor demand for protection.
Positive volatility risk premia indicate compensation required by option sellers
for bearing volatility risk.

The relationship between volatility regimes and returns suggests that
volatility contains economically meaningful information that may be incorporated
into risk-aware portfolio allocation strategies.

## 7. Limitations

This study relies on publicly available data, which restricts access to
historical option chains.
Transaction costs, liquidity effects, and stochastic volatility dynamics
are not explicitly modeled.
Future work may extend the framework using richer datasets and alternative models.

## 8. Conclusion

This project integrates option pricing theory, numerical methods,
and empirical analysis to study volatility risk.
The results demonstrate that implied and realized volatility provide
valuable information about market risk and performance,
highlighting the importance of volatility modeling in quantitative finance.
