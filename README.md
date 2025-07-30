# 📊 Stock Screener Bot (POC)

A proof-of-concept (POC) bot that identifies high-conviction stocks daily using volume and options activity filters. Results are posted to a Discord channel via webhook.

This POC demonstrates the logic and workflow using `yfinance` for volume screening and mock data for options activity.

---

## 🚀 Features

- 📈 Volume Screener: Uses `yfinance` to detect volume spikes.
- 💰 Options Screener (Mock Data): Filters based on implied volatility, open interest, call/put ratio, and premium.
- ✅ Smart Scoring: Applies weighted scoring to shortlist 5–15 top tickers.
- 🔗 Discord Integration: Posts results automatically via webhook.

---

## 🧪 Technologies Used

- `Python 3.10+`
- `yfinance` (for fetching historical stock volume)
- `pandas`
- `discord-webhook` (for Discord webhook integration)
- `mock data` (for implied volatility, OI, premiums, etc.)

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt

## ⚙️ How It Works

### 1. Volume Screener

Fetches 15-day historical data using `yfinance` and calculates:

- **Today's volume**
- **10-day average daily volume (ADV)**
- **Relative Volume (RVol)** = Volume Today / ADV

**Stocks are shortlisted if:**
- Volume ≥ 1.2 × ADV  
- RVol ≥ 1.2

---

### 2. Options Filter (Mock Data)

Simulated filters include:

- Options volume ≥ 1.5× 20-day average  
- Implied Volatility (IV) ≥ 25% over 20-day average  
- Call/Put Ratio ≥ 2 or ≤ 0.5  
- Premium > $50,000  

---

### 3. Scoring System

Each ticker is scored based on:

- 40% IV spike  
- 30% Premium  
- 20% Volume spike  
- 10% OI  

Top-ranked tickers are posted.

---

### 4. Discord Posting

Filtered results are posted to a Discord channel using a webhook with:

- Ticker  
- Score  
- Volume Spike  
- IV Spike  
- Premium  
- Call/Put Ratio  

---

## 🧪 Example Output

**META**
Volume Today: 13227300
📈 IV Jump: 30%
💰 Premium: $60,000
📊 RVol: 1.2695912579005715
🔄 Call/Put Ratio: 2.1
🏆 Score: 4

📂 Notes
This is a POC, not intended for production.

Mock data is used in place of real options API (e.g., Polygon.io).

Replace mock data logic with a live options API when going to production.

Discord webhook is optional and can be disabled for local testing.

🛠️ Next Steps (Production Upgrade)
✅ Replace mock options data with real-time from Polygon.io or IEX Cloud.

✅ Store historical IV/OI data in SQLite or TimescaleDB.

✅ Add retries and error handling for API failures.

✅ Deploy using cron job or serverless scheduler.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

💬 Contact
Made with 💻 by [Bhagyashri Salgare]
Connect: [GitHub](https://github.com/codewithbhagyashri-22) | [LinkedIn](https://www.linkedin.com/in/bhagyashri-salgare-485b5b146/)

