# Multi-Agent AI: Financial Intelligence Module
# Developed by: Sushanth Reddy Kandakatla
# Purpose: Tracking Market Trends for Startup Valuation

import random

class StockAnalyzer:
    def __init__(self, tickers):
        self.tickers = tickers
        self.market_sentiment = "Bullish" # Default 'Big Bull' mindset

    def fetch_simulated_price(self, ticker):
        # In a real build, we would use yfinance or Alpha Vantage API
        price = random.uniform(100, 500)
        return round(price, 2)

    def analyze_market(self):
        print(f"--- Global Market Report ---")
        for ticker in self.tickers:
            price = self.fetch_simulated_price(ticker)
            print(f"Ticker: {ticker} | Live Price: ${price} | Status: ACCUMULATE")
        
        print(f"\nOverall Sentiment: {self.market_sentiment}")

if __name__ == "__main__":
    # Tracking high-growth tech & AI stocks
    portfolio = ["NVDA", "TSLA", "MSFT", "GOOGL"]
    
    monitor = StockAnalyzer(portfolio)
    monitor.analyze_market()
