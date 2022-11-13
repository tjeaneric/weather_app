from typing import Optional
from fastapi import APIRouter, Depends, Response
from models.location import Location
from models.validation_error import ValidationError
from services import openweather_service

router = APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    try:
        return await openweather_service.get_report_async(
            loc.city, loc.state, loc.country, units
        )
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return Response(content=str(x), status_code=500)
