"""
For Testing The Home Route
"""
import pytest
from httpx import AsyncClient
from fastapi import FastAPI
from starlette.status import HTTP_404_NOT_FOUND

pytestmark = pytest.mark.asyncio


class TestRoutes:
    """
    This Tests Whether All The Routes are okay
    """

    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        """
        :param app: Get the app fixture from conftest
        :param client: get the async client fixture from conftest
        :return:
        """
        res = await client.get(app.url_path_for("home:root"))
        assert res.status_code != HTTP_404_NOT_FOUND

