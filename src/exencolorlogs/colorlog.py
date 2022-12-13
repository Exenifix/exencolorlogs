import logging
import os.path
from datetime import date, datetime
from pathlib import Path

from exencolor import colored, Color

logging.addLevelName(25, "OK")
OK = 25

COLORS: dict[str, Color] = {
    "OK": Color.BRIGHT_GREEN,
    "CRITICAL": Color.BRIGHT_RED,
    "ERROR": Color.BRIGHT_RED,
    "WARNING": Color.BRIGHT_YELLOW,
    "INFO": Color.BRIGHT_CYAN,
    "DEBUG": Color.WHITE,
}


class Logger(logging.Logger):
    """Base class for logging.
    :param tag: A tag to use for logging.
    :param level: Minimum level to display the logs of."""
    def __init__(self, tag: str = "BOT", level: int = logging.DEBUG):
        super().__init__(tag, level)
        handler = logging.StreamHandler()
        formatter = Formatter()
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def ok(self, message, *args, **kwargs):
        """Log message with OK level"""
        self.log(OK, message, *args, **kwargs)


class FileLogger(logging.Logger):
    def __init__(self, tag: str, level: int = logging.DEBUG, folder: Path | str = "logs", ext: str = "log"):
        """Logging class that handles files creation for you and writes logs to there too.
        :param tag: A tag to use for logging.
        :param level: Minimum level to display the logs of.
        :param folder: The folder to use for log files.
        :param ext: Files extension you want log files to have. No any dots at the beginning!"""
        super().__init__(tag, level)
        if not os.path.exists(folder):
            os.mkdir(folder)
        file_handler = FileHandler(folder, ext)
        file_handler.setFormatter(logging.Formatter("{asctime} [ {levelname} ] {name}: {message}", style="{"))
        self.addHandler(file_handler)
        handler = logging.StreamHandler()
        formatter = Formatter()
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def ok(self, message, *args, **kwargs):
        self.log(OK, message, *args, **kwargs)


class FileHandler(logging.FileHandler):
    def __init__(self, folder: Path | str, ext: str):
        self.baseDir = Path(folder)
        self.ext = ext
        self._lastEntryOn: date | None = None

        super().__init__((self.baseDir / f"{datetime.now().date()}.{self.ext}").as_posix())

    def emit(self, record: logging.LogRecord) -> None:
        today = datetime.now().date()
        if self._lastEntryOn != today:
            self.stream.close()
            self.stream = None  # type: ignore
            self.baseFilename = (self.baseDir / f"{today}.{self.ext}").as_posix()
        super().emit(record)


class Formatter(logging.Formatter):
    def __init__(self):
        super().__init__("{asctime} [ {levelname} ] {name}: {message}", style="{")

    def format(self, record: logging.LogRecord):
        color = COLORS[record.levelname]
        record.levelname = colored(record.levelname, foreground=color)
        return super().format(record)
