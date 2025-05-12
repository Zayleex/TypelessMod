from config_loader import ConfigLoader
from logger import Logger
import data
from socket_manager import SocketManager

config_loader = ConfigLoader()
config = config_loader.load()
logger = Logger("Logs")

top_streamer = data.top_streamer[0:21]

socket_manager = SocketManager(top_streamer ,config)
socket_manager.initialize()
socket_manager.assign_streamer("zayleex")








