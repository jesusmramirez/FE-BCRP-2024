import numpy as np
from scipy.stats import norm

def black_scholes_merton(market_parameters, option_parameters):
    S = market_parameters["stock_price"]
    A = market_parameters["divident_rate"]
    r = market_parameters["interest_rate"]
    sigma = market_parameters["volatility"]
    K = option_parameters["strike"]
    T = option_parameters["maturity"]
    option_type = option_parameters["option_type"]
    exercise_style = option_parameters["exercise_style"]

    if exercise_style == "european":
        pass
        if option_type == "call":
            pass
        elif option_type == "put":
            pass
        else:
            print("Not implemented")
            return None
    else:
        print("Not implemented")
        return None

def binomial_lattice(num_steps, market_parameters, option_parameters):
    n = num_steps
    S = market_parameters["stock_price"]
    A = market_parameters["divident_rate"]
    r = market_parameters["interest_rate"]
    sigma = market_parameters["volatility"]
    K = option_parameters["strike"]
    T = option_parameters["maturity"]
    option_type = option_parameters["option_type"]
    exercise_style = option_parameters["exercise_style"]

    # Do calibration

    # Set stock values

    # Set option values
    
    if option_type == "call":
        pass
    elif option_type == "put":
        pass
    
    # Do pricing
    if exercise_style == "european":
        pass
    elif exercise_style == "american":
        if option_type == "call":
            pass
        elif option_type == "put":
            pass


def binomial_black_scholes(num_steps, market_parameters, option_parameters):
    pass

def binomial_black_scholes_with_richardson_extrapolation(num_steps, market_parameters, option_parameters):
    pass

def binomial_black_scholes_with_richardson_extrapolation_and_greeks(num_steps, market_parameters, option_parameters):
    pass

def compute_greek_by_black_scholes(market_parameters, option_parameters):
    pass

def compute_rho(num_steps, market_parameters, option_parameters):
    pass

def compute_vega(num_steps, market_parameters, option_parameters):
    pass

def finite_difference_method_pricing(num_steps, market_parameters, option_parameters):
    n = num_steps["stock_steps"]
    m = num_steps["time_steps"]
    pass