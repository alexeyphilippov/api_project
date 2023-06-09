from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import marshmallow_dataclass


class BaseSchema:

    @classmethod
    def load(cls, data, many=False):
        """
        Десериализация из строки в объект
        :param data:
        :param many: True, если необходимо обработать список
        :return:
        """
        schema = marshmallow_dataclass.class_schema(cls)()

        obj: cls = schema.load(data, many=many)

        return obj

    def dump(self) -> dict:
        """
        Сериализация объекта в словарь
        """
        schema = marshmallow_dataclass.class_schema(self.__class__)()

        obj_json = schema.dump(self)

        return obj_json


@dataclass
class CallerInfo(BaseSchema):
    phone_number: str
    push_token: Optional[str] = None
    ip: Optional[str] = None


@dataclass
class CalleeInfo(BaseSchema):
    phone_number: str
    push_token: Optional[str] = None
    ip: Optional[str] = None


@dataclass
class CallSessionInfo(BaseSchema):
    caller_id: int
    callee_id: int
    call_session_initiation_dttm: datetime
    delay: int
