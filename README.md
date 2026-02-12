# Volatility Risk Premium and Market Regime Analysis

This repository contains an independent quantitative finance research project
that implements the Black–Scholes option pricing framework to extract
implied volatility from SPY options and analyze the relationship between
implied volatility, realized volatility, and market performance.

The project integrates option pricing theory, numerical methods,
and empirical analysis to study volatility risk premia
and volatility-driven market regimes.

---

## 📌 Project Motivation

Volatility is a central source of risk in financial markets.
Option-implied volatility reflects forward-looking market expectations,
while realized volatility captures ex-post risk.
Understanding the relationship between these measures is essential
for risk management and portfolio allocation.

This project was developed as part of independent preparation
for graduate study in Financial Engineering.

---

## 🔍 Methodology Overview

The analysis consists of the following components:

- Implementation of Black–Scholes pricing for European call options
- Numerical inversion of option prices using Brent’s method
- Construction and analysis of volatility smiles
- Estimation of realized volatility from historical SPY returns
- Computation of the volatility risk premium (IV − RV)
- Classification of volatility regimes and evaluation of performance

All core pricing and calibration routines are implemented from scratch in Python.

---

## 📁 Repository Structure

volatility-risk-premium/
│
├── src/ # Core pricing and calibration modules
├── notebooks/ # Research notebook with full analysis
├── report/ # Technical report (PDF + Markdown)
├── requirements.txt # Python dependencies
└── README.md

---

## 📊 Key Empirical Findings

- Implied volatility exhibits significant skew and curvature,
  indicating systematic deviations from the constant-volatility assumption.
- High-volatility regimes are associated with negative average returns
  and poor risk-adjusted performance.
- Normal volatility regimes exhibit strong and stable returns.
- The volatility risk premium is predominantly positive,
  reflecting compensation for bearing volatility risk.

---

## 📄 Technical Report

A detailed description of the methodology, results, and interpretation
is available in the technical report:

👉 **[Download Technical Report (PDF)](report/final_report.pdf)**

---

## ⚙️ Installation and Setup

Clone the repository:

```bash
git clone https://github.com/AadritoHossain/volatility-risk-premium.git
cd volatility-risk-premium

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

▶️ Usage

Launch the research notebook:

cd notebooks
jupyter lab

Open exploration.ipynb and execute the cells sequentially
to reproduce the analysis.

Data Limitations
Yahoo Finance does not provide historical option chains.
As a result, implied volatility time series are constructed
using contemporaneous option data,
while realized volatility is computed from historical returns.

This limitation is discussed in detail in the technical report.

Author

Aadrito Hossain

This project was completed as part of independent quantitative research in preparation for graduate study in financial engineering and quantitative finance.
