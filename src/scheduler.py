import pandas as pd
from .screener import evaluate_ticker
from .discord_bot import post_stock_to_discord
from .score_stock import score_stock

def run_screening():
    valid_stocks = []
    tickers = pd.read_csv("data/tickers.csv")["Symbol"].tolist()
    for ticker in tickers:
        stock_data = evaluate_ticker(ticker)
        
        if stock_data:
            stock_data["score"] = score_stock(stock_data)
            if stock_data["score"] > 3:
                valid_stocks.append(stock_data)

    # Sort by score, descending
    valid_stocks.sort(key=lambda x: x["score"], reverse=True)

    # Pick top 5–15 (e.g., top 10)
    top_stocks = valid_stocks[:5]

    for stock in top_stocks:
        message = (
        f"**{stock['ticker']}**\n"
        f"Volume Today: {stock['vol_today']}\n"
        f"📈 IV Jump: {stock['iv_jump']}%\n"
        f"💰 Premium: ${stock['premium']:,}\n"
        f"📊 RVol: {stock['rvol']}\n"
        f"🔄 Call/Put Ratio: {stock['call_put_ratio']}\n"
        f"🏆 Score: {stock['score']}"
    )
        post_stock_to_discord(stock)
