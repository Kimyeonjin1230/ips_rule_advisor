from fastapi import APIRouter, Request
from src.getinfo.getinfo_service import get_info
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

@router.get("/getinfo", response_class=HTMLResponse)
async def get_info_page(request: Request, cve_code: str):
    cve_code = request.query_params.get("cve_code")
    info_result = await get_info(cve_code)
    return templates.TemplateResponse("info.html", {"request": request, "info": info_result})