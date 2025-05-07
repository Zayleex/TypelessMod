from datetime import datetime
import os

class Logger:
    def __init__(self, path):
        self.path = path

    def get_current_time(self):
        time_keys = {}
        current_time = datetime.now()
        time_keys["day"] = current_time.strftime("%d")
        time_keys["month"] = current_time.strftime("%m")
        time_keys["year"] = current_time.strftime("%Y")
        time_keys["timestamp"] = current_time.strftime("%H:%M:%S")
        return time_keys

    def create_path(self):
        time_keys = self.get_current_time()
        return f"{self.path}/{time_keys['year']}/{time_keys['month']}"

    def log(self, level, message):
        full_path = self.create_path()
        time_keys = self.get_current_time()
        if not os.path.isdir(full_path):
            os.makedirs(full_path)
        os.chdir(full_path)
        with open(f"{time_keys["day"]}.txt", "a") as file:
            file.write(f"[{level}] {time_keys['timestamp']} - {message}\n")

    def info_log(self, message):
        self.log("INFO", message)

    def warn_log(self, message):
        self.log("WARN", message)

    def error_log(self, message):
        self.log("ERROR", message)

    def fatal_log(self, message):
        self.log("FATAL", message)



