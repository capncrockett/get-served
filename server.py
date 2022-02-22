from importlib import reload
import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route


async def hello(request):
    return JSONResponse({'message': '😎'})


async def posted(request):   # is this a request if it's a POST?
    announcement = 'posted'
    return JSONResponse({'message': f'Yo shit got {announcement}!'})


async def counted(request):
    count_it = "you're counting!"
    return JSONResponse({'count': count_it})


# Allow all incoming request origins.
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

# Starlette works as a router and then demands a cors authentication.
app = Starlette(debug=True, routes=[
    Route('/hello', hello),
    Route('/posted', posted),
    Route('/counted', counted)
], middleware=middleware)

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1",
                port=5000, log_level="info", reload=True)
# app()
