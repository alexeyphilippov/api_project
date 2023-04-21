from dataclasses import dataclass, field
from typing import Optional, Dict, List

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
    ip: str
    push_token: str