#!/usr/bin/env python3
"""
Automated Research Bot

Runs daily to find:
- Leads to contact
- Content ideas
- Competitor strategies
"""

import subprocess
import json
from datetime import datetime

SEARCH_QUERIES = [
    # Pain points
    "need help with automation",
    "looking for VA expensive", 
    "marketing agency too expensive",
    "overwhelmed with admin work",
    "small business owner struggling",
    
    # Opportunities
    "AI automation",
    "chatbot for business",
    "lead generation help",
    "content marketing help",
    
    # Competitors
    "AI agency",
    "automation agency",
    "chatbot agency"
]

def run_search(query):
    """Run web search and return results"""
    cmd = f'curl -s "https://api.duckduckgo.com/?q={query}&format=json&no_html=1"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    try:
        data = json.loads(result.stdout)
        return data.get("RelatedTopics", [])[:5]
    except:
        return []

def daily_research():
    print(f"🔍 Running daily research - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    results = []
    for query in SEARCH_QUERIES[:10]:  # Limit searches
        print(f"  Searching: {query}")
        topics = run_search(query)
        if topics:
            results.append({
                "query": query,
                "results": len(topics)
            })
    
    # Save to research file
    research_file = "/Users/g0atface/clawd/mybusiness/automation-agency/daily_research.json"
    with open(research_file, 'w') as f:
        json.dump({
            "date": datetime.now().isoformat(),
            "searches": results
        }, f, indent=2)
    
    print(f"✅ Research complete - {len(results)} queries run")
    return results

if __name__ == "__main__":
    daily_research()
