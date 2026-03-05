#!/usr/bin/env python3
"""
Automated Lead Generation Bot
==============================
Scans for leads, enriches data, and initiates outreach.

Target industries: SMBs, startups, agencies
Sources: Twitter, LinkedIn, directories
"""

import requests, json, time, csv
from datetime import datetime
from pathlib import Path

LEADS_FILE = Path("/Users/g0atface/clawd/bots/lead-gen/leads.csv")
OUTREACH_FILE = Path("/Users/g0atface/clawd/bots/lead-gen/outreach.json")

# Lead criteria
TARGET_INDUSTRIES = [
    "marketing agency",
    "seo agency", 
    "web design",
    "saas",
    "startup",
    "ecommerce",
    "crypto",
    "ai startup"
]

TARGET_SIZE = "10-50 employees"

def load_leads():
    """Load leads from CSV"""
    leads = []
    if LEADS_FILE.exists():
        with open(LEADS_FILE, "r") as f:
            reader = csv.DictReader(f)
            leads = list(reader)
    return leads

def save_lead(lead):
    """Save a lead to CSV"""
    leads = load_leads()
    leads.append(lead)
    
    with open(LEADS_FILE, "w") as f:
        if leads:
            writer = csv.DictWriter(f, fieldnames=leads[0].keys())
            writer.writeheader()
            writer.writerows(leads)

def scrape_twitter(query, limit=10):
    """Scrape Twitter/X for leads (simplified)"""
    # In production, use Twitter API
    # This is a placeholder
    print(f"🐦 Searching Twitter for: {query}")
    
    leads = []
    # Would use Twitter API here
    # For now, just print
    print(f"   (Twitter scraping requires API - skipping)")
    return leads

def scrape_google(query, limit=10):
    """Scrape Google for business listings"""
    print(f"🔍 Searching Google for: {query}")
    
    leads = []
    
    # Use Google Custom Search API in production
    # For now, return sample data structure
    
    return leads

def enrich_lead(lead):
    """Enrich lead data with additional info"""
    print(f"   Enriching: {lead.get('company', 'Unknown')}")
    
    # Add enrichment data
    lead["enriched_at"] = datetime.now().isoformat()
    lead["score"] = calculate_score(lead)
    
    return lead

def calculate_score(lead):
    """Calculate lead score based on fit"""
    score = 50  # Base score
    
    # Industry match
    industry = lead.get("industry", "").lower()
    for target in TARGET_INDUSTRIES:
        if target in industry:
            score += 20
            break
    
    # Size fit
    size = lead.get("size", "")
    if "10" in size or "50" in size:
        score += 15
    
    # Has contact
    if lead.get("email"):
        score += 15
    
    return min(score, 100)

def generate_outreach(lead):
    """Generate personalized outreach message"""
    
    templates = {
        "seo": "Hey {name}, saw {company}'s great SEO work. We help agencies like yours scale with AI automation. Quick 10-min call?",
        "marketing": "Hi {name}, love what {company}'s doing with {industry}. We help marketing agencies 10x their output. Have 5 mins?",
        "default": "Hi {name}, came across {company} and think we can help. AI automation for {industry} companies. 5 min?"
    }
    
    industry = lead.get("industry", "").lower()
    
    template = templates["default"]
    for key in templates:
        if key in industry:
            template = templates[key]
            break
    
    message = template.format(
        name=lead.get("name", "there"),
        company=lead.get("company", "your company"),
        industry=lead.get("industry", "your industry")
    )
    
    return message

def send_outreach(lead):
    """Send outreach message"""
    message = generate_outreach(lead)
    print(f"   📤 Outreach: {message[:50]}...")
    
    # Save to outreach file
    outreach = {
        "lead": lead.get("company"),
        "message": message,
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    }
    
    try:
        with open(OUTREACH_FILE) as f:
            data = json.load(f)
    except:
        data = []
    
    data.append(outreach)
    
    with open(OUTREACH_FILE, "w") as f:
        json.dump(data, f, indent=2)
    
    return outreach

def run_campaign(industry, count=5):
    """Run a lead gen campaign for an industry"""
    print("=" * 50)
    print(f"🎯 LEAD GEN CAMPAIGN: {industry}")
    print("=" * 50)
    
    # Search for leads
    leads = scrape_google(f"{industry} company UK", count)
    
    if not leads:
        print("⚠️ No leads found")
        return
    
    print(f"\n📋 Found {len(leads)} potential leads")
    
    # Enrich and score
    scored_leads = []
    for lead in leads:
        lead = enrich_lead(lead)
        scored_leads.append(lead)
        print(f"   {lead.get('company')}: {lead.get('score')}/100")
    
    # Filter to high-scoring leads
    hot_leads = [l for l in scored_leads if l.get("score", 0) >= 60]
    
    if hot_leads:
        print(f"\n🔥 {len(hot_leads)} hot leads (60+ score)")
        
        # Send outreach to top 3
        for lead in hot_leads[:3]:
            send_outreach(lead)
    else:
        print("\n❌ No hot leads - need more research")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print(__doc__)
    elif sys.argv[1] == "run":
        industry = sys.argv[2] if len(sys.argv) > 2 else "marketing agency"
        run_campaign(industry)
    elif sys.argv[1] == "list":
        leads = load_leads()
        print(f"\n📋 {len(leads)} leads in database:")
        for lead in leads[:10]:
            print(f"   - {lead.get('company')}: {lead.get('score')}/100")
    else:
        print(__doc__)
