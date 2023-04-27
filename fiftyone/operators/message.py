from enum import Enum
import json


class MessageType(Enum):
    SUCCESS = "success"
    ERROR = "error"


class GeneratedMessage:
    def __init__(self, type=MessageType.SUCCESS, cls=None, body=None):
        self.type = type
        self.cls = cls
        self.body = body

    def to_json(self):
        return {
            "type": str(self.type),
            "cls": self.cls.__name__,
            "body": self.body.to_json() if self.body else None,
        }

    def to_json_line(self):
        return json.dumps(self.to_json()) + "\n"