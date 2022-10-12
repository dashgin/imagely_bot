import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from imagely.entrypoints.api.api_v1.api import api_router
from imagely.domain.config import settings
from imagely.entrypoints.api.utils import thread_check
from starlette.responses import RedirectResponse

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="This API serves methods to edit images in several ways.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    version=settings.VERSION,
    **settings.SWAGGER_META,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@app.on_event("startup")
def startup():
    thread_check(settings.THREADS)


app.include_router(api_router, prefix=settings.API_V1_STR)


def main():
    uvicorn.run(
        "imagely.entrypoints.api.main:app",
        host="0.0.0.0",
        reload=True,
        port=settings.PORT,
        log_level=settings.LOG_LEVEL,
    )
