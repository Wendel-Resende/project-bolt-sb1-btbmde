import yfinance as yf
from datetime import datetime

def load_stock_data(ticker: str, period_choice: str, period: str = None, start_date: datetime = None, end_date: datetime = None):
    """
    Carrega dados históricos das ações usando yfinance.
    """
    if period_choice == "Período predefinido":
        return yf.download(ticker, period=period)
    return yf.download(ticker, start=start_date, end=end_date)