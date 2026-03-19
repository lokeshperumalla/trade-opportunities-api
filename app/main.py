from fastapi import FastAPI, Depends
from fastapi import Request
from fastapi.responses import PlainTextResponse
from slowapi.middleware import SlowAPIMiddleware

from app.auth import verify_api_key
from app.rate_limiter import limiter
from app.search import search_sector_news
from app.ai_analysis import analyze_market
from app.sessions import update_session
from app.utils import validate_sector

app = FastAPI(
    title="Trade Opportunities API",
    description="Analyze Indian market sectors and generate trade opportunity reports",
    version="1.0"
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str, api_key=Depends(verify_api_key)):

    # Input validation
    validate_sector(sector)

    # Session tracking
    update_session("guest")

    # Collect market data
    news = search_sector_news(sector)

    # AI analysis
    report = analyze_market(sector, news)

    return PlainTextResponse(report)