from config import logger
from core.engine import get_async_session
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from gym import logic, schemas, services
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from users.models import User
from users.utils import current_user


router = APIRouter()


@router.get("/test")
async def test() -> dict:
    """ Test endpoint
    """
    return {"test": "ok"}
