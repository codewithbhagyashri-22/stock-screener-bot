import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed

load_dotenv()
webhok_url = os.getenv("DISCORD_WEBHOOK_URL")

def post_stock_to_discord(stock):
    webhook = DiscordWebhook(url=webhok_url)
    embed = DiscordEmbed(
        title=f"{stock['ticker']} 📊",
        description="Meets all screening criteria.",
        color="03b2f8"
    )
    embed.add_embed_field(name="Volume Today", value=str(stock['vol_today']))
    embed.add_embed_field(name="RVol", value=f"{stock['rvol']:.2f}")
    embed.add_embed_field(name="IV Jump", value=f"{stock['iv_jump']}%")
    embed.add_embed_field(name="Call/Put Ratio", value=f"{stock['call_put_ratio']}")
    embed.add_embed_field(name="Premium", value=f"${stock['premium']:,}")
    webhook.add_embed(embed)
    webhook.execute()
