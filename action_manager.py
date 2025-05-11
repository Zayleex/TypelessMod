from event_data import EventData
from twitch_api import TwitchAPI
class ActionManager:
    def __init__(self):
        self.twitch_api = TwitchAPI()

    def action(self, data: list[EventData]):
        for event in data:
            if event.event == "ban":
                self.twitch_api.ban_user(event)
            elif event.event == "timeout":
                self.twitch_api.timeout_user(event)
            elif event.event == "title":
                self.twitch_api.change_title(event)
            elif event.event == "category":
                self.twitch_api.change_category(event)

