import json
from datetime import datetime
from pathlib import Path

CLIENTS_FILE = Path(__file__).parent / "clients.json"

class ClientManager:
    def __init__(self):
        self.clients = self.load()
    
    def load(self):
        if CLIENTS_FILE.exists():
            return json.load(open(CLIENTS_FILE))
        return {"leads": [], "clients": [], "completed": []}
    
    def save(self):
        with open(CLIENTS_FILE, 'w') as f:
            json.dump(self.clients, f, indent=2)
    
    def add_lead(self, name, email, service, source="website"):
        lead = {
            "id": len(self.clients["leads"]) + 1,
            "name": name,
            "email": email,
            "service": service,
            "source": source,
            "added": datetime.now().isoformat(),
            "status": "new"
        }
        self.clients["leads"].append(lead)
        self.save()
        return lead
    
    def move_to_client(self, lead_id, price):
        for lead in self.clients["leads"]:
            if lead["id"] == lead_id:
                lead["status"] = "converted"
                lead["price"] = price
                lead["converted"] = datetime.now().isoformat()
                self.clients["clients"].append(lead)
                self.save()
                return lead
        return None
    
    def get_summary(self):
        return {
            "total_leads": len(self.clients["leads"]),
            "active_clients": len(self.clients["clients"]),
            "completed": len(self.clients["completed"]),
            "pipeline_value": sum(c.get("price", 0) for c in self.clients["clients"])
        }

if __name__ == "__main__":
    cm = ClientManager()
    print(cm.get_summary())
