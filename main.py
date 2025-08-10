from fastapi import FastAPI
from fastapi.responses import JSONResponse
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address, Request
from slowapi import Limiter, _rate_limit_exceeded_handler



limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
@limiter.limit("1/minute")
async def homepage(request: Request):
    content = {
        "id": 1,
        "function": "testing rate limiting code with an extremely simple api"
    }
    return JSONResponse(content=content)