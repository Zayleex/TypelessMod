from chat_listener import ChatListener

class SocketManager:
    def __init__(self, streamer_list: list[str], config):
        self.streamer_list = streamer_list
        self.listeners: list[ChatListener] = []
        self.config = config


    def initialize(self):
        list_size = 10
        streamer_lists = []
        for i in range(0, len(self.streamer_list), list_size):
            streamer_lists.append(self.streamer_list[i:i + list_size])
        for streamer_list in streamer_lists:
            chat_listener = ChatListener(self.config)
            self.listeners.append(chat_listener)
            chat_listener.connect()
            for steamer in streamer_list:
                chat_listener.add_streamer(steamer)
                print("Joined streamer: ", steamer)



    def create_new_listener(self):
        chat_listener = ChatListener(self.config)
        self.listeners.append(chat_listener)
        return chat_listener


    def check_free_socket(self):
        for listener in self.listeners:
            if listener.streamer_count < 10:
                return listener
        return None


