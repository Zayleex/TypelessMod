import threading
from socket import socket
import time


class ChatListener:
    def __init__(self, config):
        self.url = "irc.chat.twitch.tv"
        self.port = 6667
        self.socket = socket()
        self.config = config
        self.bot_name = config["bot_name"]
        self.streamers: list[str] = []
        self.streamer_count = 0

        self.chatter_list = {}
        self.amount_tracked_chatter = 100

    def connect(self):
        access_token = self.config["access_token"]
        self.socket.connect((self.url, self.port))
        self.socket.send(f"PASS oauth:{access_token}\r\n".encode())
        self.socket.send(f"NICK {self.bot_name}\r\n".encode())
        thread = threading.Thread(target=self.listen_data).start()


    def listen_data(self):
        while True:
            data = self.socket.recv(2048).decode("utf-8")
            buffer = data.split("\r\n")
            for line in buffer:
                if line.startswith("PING"):
                    self.socket.send(f"PONG {data}\r\n".encode())
                    continue
                if "PRIVMSG" in line:
                    chatter = self.get_chatter(line)
                    message = self.get_message(line)
                    streamer = self.get_streamer(line)
                    print(f"Chatter: {chatter}, Message: {message}, Streamer: {streamer} ")
                    self.add_to_dict(streamer, chatter)


    def remove_streamer(self, streamer: str):
        self.socket.send(f"PART {streamer}\r\n".encode())
        self.streamers.remove(streamer)
        self.streamer_count -= 1

    def add_streamer(self, streamer: str):
        self.socket.send(f"JOIN #{streamer}\r\n".encode())
        self.streamers.append(streamer)
        self.streamer_count += 1
        time.sleep(1)

    @staticmethod
    def get_status_code(data):
        try:
            status_code = data.split(" ")[1]
            return status_code
        except:
            return "0"


    @staticmethod
    def get_chatter(data):
        username = data.split("!")[0].replace(":", "")
        return username

    @staticmethod
    def get_message(data):
        message = data.split("PRIVMSG")[1].split(":")[1]
        return message

    @staticmethod
    def get_streamer(data):
        streamer = data.split("#")[1].split(" ")[0]
        return streamer

    def add_to_dict(self, streamer:str, chatter :str):
        chatter_list = self.chatter_list[chatter]
        if not chatter_list:
            chatter_list = []
        if chatter in chatter_list:
            chatter_list.remove(chatter)
        if chatter_list >= self.amount_tracked_chatter:
            chatter_list.remove(chatter_list[0])
        chatter_list.append(chatter)