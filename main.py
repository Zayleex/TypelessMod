from chat_listener import ChatListener
from config_loader import ConfigLoader
from logger import Logger
import data
from socket_manager import SocketManager

config_loader = ConfigLoader()
config = config_loader.load()
logger = Logger("Logs")

top_streamer = data.top_streamer
print(f"{len(top_streamer)} amount of Streamers")

socket_manager = SocketManager(top_streamer ,config)

socket_manager.initialize()








