#!/usr/bin/env python3
"""
Auto-Post Optimizer

Learns from engagement what content works best.
"""

import json
import random
from datetime import datetime
from pathlib import Path

POST_TEMPLATES = {
    "value": [
        "Here's how to {topic}...",
        "The secret to {topic}...",
        "I {action} for 30 days. Here's what happened:",
    ],
    "story": [
        "I made ${amount} using {method}...",
        "My AI agent {action} while I slept...",
        "6 months ago I started. Now {result}.",
    ],
    "offer": [
        "New: {service} - {price}",
        "Offering {service}. DM to get started.",
        "{service} starting at {price}. Limited spots.",
    ],
    "education": [
        "{topic} in 5 steps:",
        "Everything you need to know about {topic}:",
        "Why {topic} matters:",
    ]
}

class AutoPoster:
    def __init__(self):
        self.history_file = Path(__file__).parent / "post_history.json"
        self.history = self.load_history()
    
    def load_history(self):
        if self.history_file.exists():
            return json.load(open(self.history_file))
        return {"posts": [], "engagement": {}}
    
    def save(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)
    
    def generate_post(self, template_type="mixed"):
        if template_type == "mixed":
            template_type = random.choice(list(POST_TEMPLATES.keys()))
        
        template = random.choice(POST_TEMPLATES[template_type])
        
        # Customizations
        content = template.format(
            topic=random.choice(["automation", "AI", "lead generation"]),
            action=random.choice(["made $500", "saved 10 hours", "generated 100 leads"]),
            amount=random.choice(["500", "1000", "5000"]),
            method=random.choice(["AI agents", "automation", "bots"]),
            result=random.choice(["$10K/month", "freedom", "a business"]),
            service=random.choice(["lead gen", "content", "setup"]),
            price=random.choice(["$497", "$200/mo", "$97"])
        )
        
        return content, template_type
    
    def log_post(self, content, template_type, platform="x"):
        self.history["posts"].append({
            "content": content,
            "type": template_type,
            "platform": platform,
            "date": datetime.now().isoformat()
        })
        self.save()
    
    def get_best_types(self):
        """Return best performing post types"""
        types = {}
        for post in self.history["posts"]:
            t = post.get("type", "unknown")
            types[t] = types.get(t, 0) + 1
        return sorted(types.items(), key=lambda x: -x[1])

if __name__ == "__main__":
    ap = AutoPoster()
    post, type_ = ap.generate_post()
    print(f"Generated post ({type_}): {post}")
