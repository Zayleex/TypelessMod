import threading
import time
from socket import socket

class ChatListener:
    def __init__(self, username: str, config):
        self.username = username
        self.url = "irc.chat.twitch.tv"
        self.port = 6667
        self.socket = socket()
        self.config = config

    def listen(self):
        access_token = self.config["access_token"]
        initial_listen = True
        try:
            self.socket.connect((self.url, self.port))
            self.socket.send(f"PASS oauth:{access_token}\r\n".encode())
            self.socket.send(f"NICK {self.username}\r\n".encode())
            self.socket.send(f"JOIN #{self.username}\r\n".encode())
            while initial_listen:
                data = self.socket.recv(2048).decode()
                buffer = data.split("\r\n")
                for line in buffer:
                    if self.get_status_code(line) == "353":
                            print("Ready for chat!")
                            threading.Thread(target=self.listen_data).start()
                            initial_listen = False
        except Exception as e:
            print(e)


    def listen_data(self):
        start_listening = False
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