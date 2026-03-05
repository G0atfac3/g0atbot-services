#!/usr/bin/env python3
"""
Client Finder - Business Website & LinkedIn Research

Finds businesses that need AI automation by:
1. Searching for businesses without modern websites
2. Finding companies using outdated tech
3. Targeting by industry/pain points
"""

import requests
import json
import time
from pathlib import Path
from datetime import datetime

SEARCH_TEMPLATES = {
    "small_business": [
        "site:linkedin.com \"small business owner\" \"looking for help\"",
        "site:linkedin.com founder \"need marketing\" automation",
        "\"overwhelmed with admin\" \"small business\"",
    ],
    "industries": [
        "real estate agent needs automation",
        "law firm marketing automation",
        "accounting firm AI automation",
        "medical practice marketing",
        "restaurant owner social media",
    ],
    "pain_points": [
        "too expensive marketing agency",
        "need lead generation help",
        "looking for VA expensive",
        "social media management too much work",
    ]
}

class ClientFinder:
    def __init__(self):
        self.results_file = Path(__file__).parent / "found_clients.json"
        self.clients = self.load_clients()
    
    def load_clients(self):
        if self.results_file.exists():
            return json.load(open(self.results_file))
        return {"leads": [], "contacted": [], "replied": []}
    
    def save(self):
        with open(self.results_file, 'w') as f:
            json.dump(self.clients, f, indent=2)
    
    def search_duckduckgo(self, query):
        """Basic search - returns topic snippets"""
        url = f"https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_html": 1,
            "skip_disambig": 1
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            return data.get("RelatedTopics", [])
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def find_leads(self, category="small_business", limit=10):
        """Find leads from searches"""
        queries = SEARCH_TEMPLATES.get(category, SEARCH_TEMPLATES["small_business"])
        
        found = []
        for query in queries[:3]:
            print(f"Searching: {query}")
            results = self.search_duckduckgo(query)
            
            for r in results[:limit]:
                if isinstance(r, dict) and r.get("Text"):
                    lead = {
                        "source": query,
                        "snippet": r.get("Text", "")[:200],
                        "found": datetime.now().isoformat(),
                        "status": "new"
                    }
                    found.append(lead)
            
            time.sleep(1)  # Rate limit
        
        # Add to clients
        self.clients["leads"].extend(found)
        self.save()
        
        print(f"Found {len(found)} new leads")
        return found
    
    def generate_outreach(self, lead):
        """Generate personalized outreach message"""
        snippet = lead.get("snippet", "")
        
        templates = [
            f"Hey, I saw your post about {snippet[:50]}... We help small businesses automate exactly that. Happy to chat if interested.",
            f"Hi! Noticed you're looking for help with {snippet[:50]}. Our AI agents handle that 24/7 - a fraction of the cost. Want to learn more?",
        ]
        
        return templates[lead.get("id", 0) % len(templates)]

if __name__ == "__main__":
    cf = ClientFinder()
    
    # Run searches
    for category in SEARCH_TEMPLATES.keys():
        print(f"\n=== {category.upper()} ===")
        cf.find_leads(category, limit=5)
    
    print(f"\nTotal leads: {len(cf.clients['leads'])}")
