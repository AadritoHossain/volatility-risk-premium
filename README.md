# Volatility Risk Premium and Market Regime Analysis

This repository contains an independent quantitative finance research project
that implements the Black–Scholes option pricing framework to extract
implied volatility from SPY options and analyze the relationship between
implied volatility, realized volatility, and market performance.

The project integrates option pricing theory, numerical methods,
and empirical analysis to study volatility risk premia
and volatility-driven market regimes.

---

## Project Motivation

Volatility is a central source of risk in financial markets.
Option-implied volatility reflects forward-looking market expectations,
while realized volatility captures ex-post risk.
Understanding the relationship between these measures is essential
for risk management and portfolio allocation.

This independent research project complements my current MSE studies
in Financial Mathematics at Johns Hopkins University.

---

## Methodology Overview

The analysis consists of the following components:

- Implementation of Black–Scholes pricing for European call options
- Numerical inversion of option prices using Brent’s method
- Construction and analysis of volatility smiles
- Estimation of realized volatility from historical SPY returns
- Computation of the volatility risk premium (IV − RV)
- Classification of volatility regimes and evaluation of performance

All core pricing and calibration routines are implemented from scratch in Python.

---

## Repository Structure

| Path | Contents |
| --- | --- |
| `src/` | Core pricing and calibration modules |
| `notebooks/` | Research notebook with full analysis |
| `report/` | Technical report (PDF + Markdown) |
| `requirements.txt` | Python dependencies |
| `README.md` | Project overview and setup instructions |

---

## Key Empirical Findings

- Implied volatility exhibits significant skew and curvature,
  indicating systematic deviations from the constant-volatility assumption.
- High-volatility regimes are associated with negative average returns
  and poor risk-adjusted performance.
- Normal volatility regimes exhibit strong and stable returns.
- The volatility risk premium is predominantly positive,
  reflecting compensation for bearing volatility risk.

---

## Technical Report

A detailed description of the methodology, results, and interpretation
is available in the technical report:

**[Download Technical Report (PDF)](report/final_report.pdf)**

---

## Installation and Setup

The commands below use a macOS/Linux shell and require Git and Python with
`venv` and `pip` available. The committed notebook records Python 3.14.3.
The dependency file includes platform-specific packages, so it may need
adjustments outside macOS.

Clone the repository:

```bash
git clone https://github.com/AadritoHossain/volatility-risk-premium.git
cd volatility-risk-premium
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies from the repository root. JupyterLab is included in
`requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## Usage

With the virtual environment active, launch JupyterLab from the notebook
directory so the notebook's relative imports resolve correctly:

```bash
cd notebooks
python -m jupyterlab exploration.ipynb
```

Select the Python kernel associated with the virtual environment and work
through `exploration.ipynb` interactively, in order.

The committed notebook includes exploratory scratch cells, including incomplete
`New T =`, `New K =`, and `New Market Price =` assignments and a prose-only
code cell. Skip these cells or convert them to Markdown before execution;
the notebook is not currently a clean, end-to-end "Run All" workflow.
It also uses live Yahoo Finance data and positional option-expiry selections,
which may need adjustment to the available expirations. An internet connection
is required, and fresh results may differ from the saved outputs.

See the technical report for the full methodology and empirical findings.

## Data Limitations

Yahoo Finance does not provide historical option chains.
As a result, implied volatility time series are constructed
using contemporaneous option data,
while realized volatility is computed from historical returns.

This limitation is discussed in detail in the technical report.

## Author

Aadrito Hossain

MSE student in Financial Mathematics at Johns Hopkins University.
This project is part of my independent quantitative finance research.
