from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.schemas import CallerInfo, CalleeInfo, CallSessionInfo
from database.db import get_session
from database.models import Caller, Callee, CallSessions

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root():
    return "Hello yeah World"


@router.post("/caller/add_caller/")
async def add_caller(data: CallerInfo, session: AsyncSession = Depends(get_session)):
    caller = Caller(phone_number=data.phone_number, push_token=data.push_token)
    session.add(caller)
    await session.flush()


@router.post("/callee/add_callee/")
async def add_callee(data: CalleeInfo, session: AsyncSession = Depends(get_session)):
    callee = Callee(phone_number=data.phone_number, push_token=data.push_token)
    session.add(callee)
    await session.flush()


@router.get("/caller/get_caller_by_num/{phone_number}", response_class=JSONResponse)
async def get_caller_by_num(phone_number: str, session: AsyncSession = Depends(get_session),):
    statement = select(Caller).where(Caller.phone_number == phone_number)
    caller = await session.execute(statement)
    return caller.scalars().first()


@router.get("/callee/get_callee_by_num/{phone_number}", response_class=JSONResponse)
async def get_callee_by_num(phone_number: str, session: AsyncSession = Depends(get_session)):
    statement = select(Callee).where(Callee.phone_number == phone_number)
    callee = await session.execute(statement)
    return callee.scalars().first()


@router.post("/caller/declare_call_session/")
async def declare_call_session(data: CallSessionInfo, session: AsyncSession = Depends(get_session)):
    call_session = CallSessions(caller_id=data.caller_id, callee_id=data.callee_id,
                                call_session_initiation_dttm=data.call_session_initiation_dttm,
                                delay=data.delay)
    session.add(call_session)
    await session.flush()


@router.get("/callee/fetch_call_session/{callee_id}", response_class=JSONResponse)
async def fetch_call_session(callee_id: int, session: AsyncSession = Depends(get_session)):
    statement = select(CallSessions).where(Callee.phone_number == phone_number)
    callee = await session.execute(statement)
    return callee.scalars().first()