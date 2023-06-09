from datetime import datetime
from typing import Union

from sqlalchemy import Column, BigInteger, VARCHAR, TIMESTAMP, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Caller(Base):
    __tablename__ = 'caller'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    phone_number: Union[str, Column] = Column(VARCHAR(length=512), nullable=False)
    push_token: Union[str, Column] = Column(VARCHAR(length=512), default=None)
    actuality_dttm: Union[datetime, Column] = Column(TIMESTAMP, default=datetime.now(), nullable=False)

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]


class Callee(Base):
    __tablename__ = 'callee'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    phone_number: Union[str, Column] = Column(VARCHAR(length=512), nullable=False)
    push_token: Union[str, Column] = Column(VARCHAR(length=512), default=None)
    actuality_dttm: Union[datetime, Column] = Column(TIMESTAMP, default=datetime.now(), nullable=False)

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]


class Calls(Base):
    __tablename__ = 'calls'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    caller_id: Union[int, Column] = Column(BigInteger, ForeignKey('caller.id', ondelete="CASCADE"), nullable=False)
    callee_id: Union[int, Column] = Column(BigInteger, ForeignKey('callee.id', ondelete="CASCADE"), nullable=False)
    status_id: Union[int, Column] = Column(BigInteger, ForeignKey('call_statuses.id', ondelete="CASCADE"),
                                           nullable=False)
    call_started_dttm: Union[TIMESTAMP, Column] = Column(TIMESTAMP, nullable=False)
    call_ended_dttm: Union[TIMESTAMP, Column] = Column(TIMESTAMP, nullable=False)
    actuality_dttm: Union[datetime, Column] = Column(TIMESTAMP, default=datetime.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint("caller_id", "callee_id", "call_started_dttm",
                         name="calls_caller_id_callee_id_call_started_dttm_key"),
        UniqueConstraint("caller_id", "callee_id", "call_ended_dttm",
                         name="calls_caller_id_callee_id_call_ended_dttm_key"),
    )

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]


class CallStatuses(Base):
    __tablename__ = 'call_statuses'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    status: Union[str, Column] = Column(VARCHAR(length=512), nullable=False)

    __table_args__ = (
        UniqueConstraint('status', name="status_key"),
    )

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]


class CallSessions(Base):
    """
    delay: int Delay in seconds
    """
    __tablename__ = 'call_sessions'

    id: Union[int, Column] = Column(BigInteger, primary_key=True, autoincrement=True)
    caller_id: Union[int, Column] = Column(BigInteger, ForeignKey('caller.id', ondelete="CASCADE"), nullable=False)
    callee_id: Union[int, Column] = Column(BigInteger, ForeignKey('callee.id', ondelete="CASCADE"), nullable=False)
    call_session_initiation_dttm: Union[TIMESTAMP, Column] = Column(TIMESTAMP, nullable=False)
    delay: int = Column(Integer, nullable=False)  # delay in seconds
    actuality_dttm: Union[datetime, Column] = Column(TIMESTAMP, default=datetime.now(), nullable=False)

    __table_args__ = (
        UniqueConstraint("caller_id", "callee_id", "call_session_initiation_dttm",
                         name="calls_caller_id_callee_id_call_session_initiation_dttm_key"),
        UniqueConstraint("caller_id", "callee_id", "delay",
                         name="calls_caller_id_callee_id_delay_key")
    )

    @property
    def table_name(self):
        return self.target_table.split('.')[1]

    @property
    def schema_name(self):
        return self.target_table.split('.')[0]
