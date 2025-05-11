class EventData:
    def __init__(self, json_data):
        self.event = json_data["event"]
        self.username = json_data["username"]
        self.duration = json_data["duration"]
        self.title = json_data["title"]
        self.category = json_data["category"]
