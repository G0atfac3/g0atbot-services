# eBay Arbitrage Bot

Automated product research and flipping. Finds undervalued products, lists on eBay with profit margin.

## How It Works

1. **Product Research** - Scans clearance sections, thrift stores, wholesale sites
2. **Price Analysis** - Calculates profit after fees, shipping, sourcing costs
3. **Listing Creation** - Writes titles, descriptions, sets optimal price
4. **Price Monitoring** - Adjusts based on competitor pricing
5. **Auto-relisting** - Relists unsold items

## Setup

```bash
export EBAY_API_KEY="your_key"
export EBAY_AUTH_TOKEN="your_token"
```

## Usage

```bash
python find_deals.py --category electronics --max-price 20
python list_item.py --sku 12345 --price 45.99
python monitor.py --check-hours 6
```

## Note

eBay banned AI "buy-for-me" agents Feb 2026. This tool is for LISTING only - human must approve purchases.
