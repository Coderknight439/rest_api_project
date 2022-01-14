"""
Configure PyTest

"""
import warnings
import os
import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient
from databases import Database
import alembic
from alembic.config import Config
from app.config import settings


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations():
    """
    Run Alembic Upgrade Command For Starting The Test DB.
    Run Alembic Downgrade Command for Destroying Test Db
    :return:
    """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")
    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


# Create a new application for testing
@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from app.main import get_application
    """
    :return:
    """
    return get_application()


# Grab a reference to our database when needed
@pytest.fixture
def db(application: FastAPI) -> Database:
    """
    :param application: Get The Current Application
    :return:
    """
    return application.state._db


# Make requests in our tests
@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    """
    :param application: Get The Current Application
    :return:
    """
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"}
        ) as api_client:
            yield api_client
