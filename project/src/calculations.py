import numpy as np
import pandas as pd

def calculate_volatility_metrics(data: pd.DataFrame):
    """
    Calcula métricas de volatilidade para um DataFrame de preços.
    """
    data['Daily Return'] = data['Close'].pct_change()
    volatility = np.std(data['Daily Return']) * np.sqrt(252)
    avg_volatility = data['Daily Return'].std() * np.sqrt(252)
    max_price = float(data['Close'].max())
    min_price = float(data['Close'].min())
    
    return {
        'volatility': volatility,
        'avg_volatility': avg_volatility,
        'max_price': max_price,
        'min_price': min_price,
        'daily_returns': data['Daily Return']
    }