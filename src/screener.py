from .volume_screener import get_volume_metrics
from .options_screener import get_options_metrics

def evaluate_ticker(ticker):
    vol = get_volume_metrics(ticker)
    if not vol or not vol["pass"]:
        return None
    
    options = get_options_metrics(ticker)
    if not options or not options["pass"]:
        return None

    return {
        "ticker": ticker,
        **vol,
        **options
    }
