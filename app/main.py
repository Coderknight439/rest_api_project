from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import api_router
from app.config import settings
import uvicorn
from fastapi.staticfiles import StaticFiles
from app.tasks import populate_database


def get_application():
    application = FastAPI(title=settings.PROJECT_NAME, version=settings.API_V1_STR)
    origins = ["*"]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router)
    return application


app = get_application()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=9000, reload=True)
    populate_database.delay()
