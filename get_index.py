import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from enum import Enum
import os


def download_nasdaq_100_data(start_date, end_date, interval):
    nasdaq_minute_data = yf.download('^NDX', start=start_date, end=end_date, interval=interval)
    
    nasdaq_minute_data.to_csv(f'data\\{interval}\\{end_date}.csv')
    
if __name__ == "__main__":
    days_back = 7
    interval = "1m"
    end_date = datetime.now().strftime(r'%Y-%m-%d')
    
    if not os.path.exists("data"):
        os.mkdir("data")
        
    if not os.path.exists(f"data\\{interval}"):
        os.mkdir(f"data\\{interval}")
    
    if interval == "1m" and days_back > 7:
        days_back = 7
    
    start_date = (datetime.now() - timedelta(days=days_back)).strftime(r'%Y-%m-%d')
    
    download_nasdaq_100_data(start_date, end_date, "1m")