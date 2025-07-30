import yfinance as yf

def get_volume_metrics(ticker):
    try:
        data = yf.Ticker(ticker).history(period="15d")
        if len(data) < 11:
            return None
        vol_today = data['Volume'][-1]
        adv_10 = data['Volume'][-11:-1].mean()
        rvol = vol_today / adv_10
        return {
            "ticker": ticker,
            "vol_today": vol_today,
            "adv_10": adv_10,
            "rvol": rvol,
            "pass": vol_today >= 1.2 * adv_10 and rvol >= 1.2
        }
    except Exception as e:
        return None
