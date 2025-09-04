import json

from event_data import EventData
import requests

class TwitchAPI:
    def __init__(self, config):
        self.config = config

    def ban_user(self, data: EventData):
        pass

    def timeout_user(self, data: EventData):
        pass

    def change_title(self, data: EventData, streamer):
        url = "https://api.twitch.tv/helix/channels"
        header = {
            "Authorization": f"Bearer {self.refresh_token(streamer)}",
            "Client-Id": self.config.client_id,
            "Content-Type": "application/json",
        }
        data = {
            "title": data.title,
        }
        title = data.title

        response = requests.patch(url, headers=header, json=json.dumps(data))
        print(response.status_code)

    def change_category(self, data: EventData):
        pass

    def refresh_token(self, streamer):
        pass

    def get_game_id(self, data: EventData):
        url = "https://api.twitch.tv/helix/games"
        header = {
            "Authorization": f"Bearer {self.refresh_token(streamer)}",
            "Client-Id": self.config.client_id,
        }