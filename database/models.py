from datetime import datetime
from typing import Union

from sqlalchemy import Column, BigInteger, VARCHAR, TIMESTAMP, ForeignKey, Integer, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, Index, REAL, DateTime, func, Text
from sqlalchemy.orm import declarative_base, relationship, selectinload

Base = declarative_base()


class Caller(Base):
    __tablename__ = 'caller'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    phone_number: Union[str, Column] = Column(VARCHAR(length=512), nullable=False)
    push_token: Union[str, Column] = Column(VARCHAR(length=512),  default=None)
    ip: Union[str, Column] = Column(VARCHAR(length=512), nullable=False)
    actuality_dttm: Union[datetime, Column] = Column(TIMESTAMP, default=datetime.now(), nullable=False)

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]
