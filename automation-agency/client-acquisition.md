# Client Acquisition Bot

Finds potential clients who need AI automation.

## How It Works

1. **Monitor Keywords** - "need help with automation", "looking for VA", "too expensive"
2. **Find Decision Makers** - Founders, CEOs, ops managers
3. **Enrich Data** - Get emails, company info
4. **Outreach** - DM or email with personalized pitch

## Keywords to Monitor

```
automation, streamline, save time, need VA, too expensive
marketing agency, social media management, lead gen
business owner, founder, solopreneur
```

## Usage

```bash
python find_clients.py --keywords "marketing agency" --limit 50
python outreach.py --client-id 123
```

## Engagement Templates

### Initial Outreach
"Hey [Name], saw your post about [pain point]. We help [industry] businesses automate [task]. 
Would you be open to a 10-min chat?"

### Follow-up (24h)
"Following up - just wanted to share how we helped [similar company] achieve [result]."

## Tracking

Leads → Client Manager → Delivery → Payment
