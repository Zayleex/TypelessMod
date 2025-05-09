import threading
import time
from socket import socket
import time


class ChatListener:
    def __init__(self, streamers: list[str], config):
        self.url = "irc.chat.twitch.tv"
        self.port = 6667
        self.socket = socket()
        self.config = config
        self.bot_name = config["bot_name"]

        self.streamers = streamers
        self.streamer_count = len(streamers)


    def listen(self):
        access_token = self.config["access_token"]
        initial_listen = True

        self.socket.connect((self.url, self.port))
        self.socket.send(f"PASS oauth:{access_token}\r\n".encode())
        self.socket.send(f"NICK {self.bot_name}\r\n".encode())

        for streamer in self.streamers:
            self.socket.send(f"JOIN #{streamer}\r\n".encode())
            print(f"Joined {streamer}!")
            time.sleep(1)
            while initial_listen:
                data = self.socket.recv(2048).decode()
                buffer = data.split("\r\n")
                for line in buffer:
                    print(line)
                    if self.get_status_code(line) == "353":
                            threading.Thread(target=self.listen_data).start()
                            print(f"Listening to {streamer}!")
                            initial_listen = False


    def listen_data(self):
        while True:
            data = self.socket.recv(2048).decode("utf-8")
            buffer = data.split("\r\n")
            for line in buffer:
                if line.startswith("PING"):
                    self.socket.send(f"PONG {data}\r\n".encode())
                    continue
                elif line != "":
                    username = self.get_chatter(line)
                    message = self.get_message(line)
                    print(f"{username}: {message}")


    def remove_streamer(self, streamer: str):
        self.socket.send(f"PART {streamer}\r\n".encode())
        self.streamers.remove(streamer)
        self.streamer_count -= 1


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