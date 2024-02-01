from engine import *
import pandas as pd
import matplotlib.pyplot as plt

market_parameters = {
    "stock_price": 100,
    "divident_rate": 0.03,
    "interest_rate": 0.06,
    "volatility": 0.30,
}

option_parameters = {
    "strike": 100, 
    "maturity": 0.5,
    "option_type": "call",
    "exercise_style": "european",
}

# How to call Black-Scholes formula
black_scholes_merton(market_parameters, option_parameters)

# How to call Binomial Lattice
num_steps = 10
binomial_lattice(num_steps, market_parameters, option_parameters)