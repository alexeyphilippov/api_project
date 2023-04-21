from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import CallerInfo
from starlette.responses import JSONResponse
from database.models import Caller

from database.db import get_session

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def root():
    return "Hello World"


@router.post("/add_caller/")
async def add_caller(data: CallerInfo, session: AsyncSession = Depends(get_session)):
    caller = Caller(phone_number=data.phone_number, push_token = data.push_token, ip=data.ip)
    session.add(caller)
    await session.flush()
    return JSONResponse()
