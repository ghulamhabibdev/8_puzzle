import json
import os
from datetime import datetime
class JsonLog:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename,
"w") as f:
                json.dump([], f)
    def _load_data(self):
        with open(self.filename,
"r") as f:
            return json.load(f)
    def _save_data(self, data):
        with open(self.filename,
"w") as f:
            json.dump(data, f, indent=4)
    def add(self, data):
        """
        Add a new log entry into JSON file
        """
        logs = self._load_data()

        # Optional: add timestamp automatically
        entry = {
    "timestamp": datetime.now().isoformat(),
    "data": data
}

        logs.append(entry)

        self._save_data(logs)
        print("Log added successfully!")