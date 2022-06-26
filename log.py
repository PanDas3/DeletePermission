from logging import getLogger
from logging import basicConfig
from logging import error
from logging import info
from logging import warning
from logging import ERROR
from logging import INFO
from logging import WARNING
from time import strftime
from os import getlogin, mkdir, path

class Log():
    def __init__(self) -> None:
        self.currentdate = strftime("%Y%m%d")
        self.current_login = getlogin()
        if(path.isdir("Logs") == False):
            mkdir("Logs")

    def error(self, msg):
        log = getLogger("Logger")
        log.setLevel(ERROR)
        basicConfig(filename=f"Logs\\PermsDel_{self.currentdate}_{self.current_login}.log", level=ERROR, format="%(asctime)s \t %(levelname)s: \t %(message)s")
        error(msg)

    def info(self, msg):
        log = getLogger("Logger")
        log.setLevel(INFO)
        basicConfig(filename=f"Logs\\PermsDel_{self.currentdate}_{self.current_login}.log", level=INFO, format="%(asctime)s \t %(levelname)s: \t\t %(message)s")
        info(msg)

    def warining(self, msg):
        log = getLogger("Logger")
        log.setLevel(WARNING)
        basicConfig(filename=f"Logs\\PermsDel_{self.currentdate}_{self.current_login}.log", level=WARNING, format="%(asctime)s \t %(levelname)s: \t %(message)s")
        warning(msg)

    def __del__(self):
        pass