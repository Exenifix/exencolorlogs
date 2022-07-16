import logging
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
    def __init__(self, tag: str = "BOT", level: int = logging.DEBUG):
        super().__init__(tag, level)
        handler = logging.StreamHandler()
        formatter = Formatter()
        handler.setFormatter(formatter)
        self.addHandler(handler)

    def ok(self, message, *args, **kwargs):
        self.log(OK, message, *args, **kwargs)


class Formatter(logging.Formatter):
    def __init__(self):
        super().__init__("{asctime} [ {levelname} ] {name}: {message}", style="{")

    def format(self, record: logging.LogRecord):
        color = COLORS[record.levelname]
        record.levelname = colored(record.levelname, foreground=color)
        return super().format(record)
