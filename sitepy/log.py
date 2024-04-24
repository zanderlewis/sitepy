import sys
import os
import time
from collections import deque

class Logger:
    def __init__(self, log_file, console_output=True, max_size=1024, backup_count=5, log_format="{timestamp} - {level}: {message}"):
        self.log_file = log_file
        self.console_output = console_output
        self.max_size = max_size
        self.backup_count = backup_count
        self.log_format = log_format
        self.levels = {'DEBUG': 0, 'INFO': 1, 'WARNING': 2, 'ERROR': 3, 'CRITICAL': 4}
        self.logs = deque(maxlen=self.backup_count)
        self.handlers = {}

    def log(self, level, message):
        if level not in self.levels:
            raise ValueError(f"Invalid log level: {level}")

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_entry = self.log_format.format(timestamp=timestamp, level=level.upper(), message=message)

        with open(self.log_file, 'a') as file:
            file.write(log_entry + '\n')
        
        if self.console_output:
            print(log_entry)

        self.logs.append(log_entry)

        if os.path.getsize(self.log_file) > self.max_size:
            self._rotate_logs()

    def _rotate_logs(self):
        if self.backup_count > 0:
            for i in range(self.backup_count - 1, 0, -1):
                if os.path.exists(f"{self.log_file}.{i}"):
                    os.replace(f"{self.log_file}.{i}", f"{self.log_file}.{i + 1}")
            os.replace(self.log_file, f"{self.log_file}.1")
        with open(self.log_file, 'w'):
            pass

    def set_log_format(self, log_format):
        self.log_format = log_format

    def set_console_output(self, console_output):
        self.console_output = console_output

    def set_max_size(self, max_size):
        self.max_size = max_size

    def set_backup_count(self, backup_count):
        self.backup_count = backup_count

    def add_handler(self, level, handler_func):
        if level not in self.levels:
            raise ValueError(f"Invalid log level: {level}")
        self.handlers[level] = handler_func

    def log_with_handler(self, level, message):
        if level in self.handlers:
            self.handlers[level](message)
        self.log(level, message)

    def debug(self, message):
        self.log_with_handler('DEBUG', message)

    def info(self, message):
        self.log_with_handler('INFO', message)

    def warning(self, message):
        self.log_with_handler('WARNING', message)

    def error(self, message):
        self.log_with_handler('ERROR', message)

    def critical(self, message):
        self.log_with_handler('CRITICAL', message)

