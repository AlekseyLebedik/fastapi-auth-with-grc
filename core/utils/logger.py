import os
from dataclasses import dataclass
from typing import List, Tuple, Union

from loguru import logger

current_dir = os.getcwd()
logger_dir = os.path.abspath(os.path.join(current_dir, "logger/info.json"))

logger.add(
    logger_dir,
    level="ERROR",
    format="{time} {level} {message}",
    rotation="1 week",
    compression="zip",
    serialize=True,
)


@dataclass
class Logger:
    def listMessage(self, messages: Union[List, any], method):
        if isinstance(messages, Tuple):
            for message in messages:
                method(message)
        else:
            method(messages[0])

    def info(self, *messages):
        self.listMessage(messages, logger.info)

    def warning(self, *messages):
        self.listMessage(messages, logger.warning)

    def error(self, *messages):
        self.listMessage(messages, logger.error)


_logger = Logger()
