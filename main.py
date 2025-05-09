from chat_listener import ChatListener
from config_loader import ConfigLoader
from logger import Logger
import data

config_loader = ConfigLoader()
config = config_loader.load()
logger = Logger("Logs")

top_streamer = data.top_streamer
to_listen = []


for streamer in top_streamer:
    to_listen.append(f"#{streamer}")

usernames = ",".join(to_listen)

print(usernames)

chat_listener = ChatListener(usernames, config)
chat_listener.listen()


