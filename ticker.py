import yfinance as yf
import datetime
import matplotlib.pyplot as plt

class Ticker:
    @staticmethod
    def get_historical_data(ticker, start_date=None, end_date=None):
        try:
            # Fetching data using yfinance
            if start_date is not None and end_date is not None:
                data = yf.download(ticker, start=start_date, end=end_date)
            else:
                data = yf.download(ticker)

            if data.empty:
                return None
            return data
        
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            return None

    @staticmethod
    def get_columns(data):
        if data is None:
            return None
        return list(data.columns)

    @staticmethod
    def get_last_price(data, column_name):
        if data is None or column_name is None:
            return None
        if column_name not in Ticker.get_columns(data):
            print(f"Column {column_name} not found in data.")
            return None
        return data[column_name].iloc[-1]

    @staticmethod
    def plot_data(data, ticker, column_name):
        try:
            if data is None:
                return None
            fig, ax = plt.subplots()
            data[column_name].plot(ax=ax)
            ax.set_ylabel(f'{column_name}')
            ax.set_xlabel('Date')
            ax.set_title(f'Historical data for {ticker} - {column_name}')
            ax.legend(loc='best')
            return fig
        except Exception as e:
            print(e)
            return None