#!/usr/bin/env python3
"""
Learning Client Acquisition System

Monitors X and Reddit for:
- Pain points people have
- Competitors' clients
- Trending topics to post about
- Winning sales messages
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent / "learning_data.json"

class LearningSystem:
    def __init__(self):
        self.data = self.load()
    
    def load(self):
        if DATA_FILE.exists():
            return json.load(open(DATA_FILE))
        return {
            "pain_points": [],
            "competitors": [],
            "winning_messages": [],
            "trending_topics": [],
            "outreach_results": []
        }
    
    def save(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_pain_point(self, platform, keyword, context):
        self.data["pain_points"].append({
            "platform": platform,
            "keyword": keyword,
            "context": context,
            "date": datetime.now().isoformat()
        })
        self.save()
    
    def add_winning_message(self, message_type, content, engagement):
        self.data["winning_messages"].append({
            "type": message_type,
            "content": content,
            "engagement": engagement,
            "date": datetime.now().isoformat()
        })
        self.save()
    
    def get_insights(self):
        return {
            "total_pain_points": len(self.data["pain_points"]),
            "top_keywords": self.get_top_keywords(),
            "best_message_types": self.get_best_types()
        }
    
    def get_top_keywords(self):
        keywords = {}
        for pp in self.data["pain_points"]:
            kw = pp.get("keyword", "")
            if kw:
                keywords[kw] = keywords.get(kw, 0) + 1
        return sorted(keywords.items(), key=lambda x: -x[1])[:10]
    
    def get_best_types(self):
        types = {}
        for wm in self.data["winning_messages"]:
            t = wm.get("type", "")
            if t:
                types[t] = types.get(t, 0) + wm.get("engagement", 0)
        return sorted(types.items(), key=lambda x: -x[1])[:5]

if __name__ == "__main__":
    ls = LearningSystem()
    print(json.dumps(ls.get_insights(), indent=2))
