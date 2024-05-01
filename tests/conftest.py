import pytest
from flask import Flask
from flask import JWTManager

from app import create_app
from route.db_extension import db

FLASK_CFG = "testing"


@pytest.fixture(scope="session", autouse=True)
def app() -> Flask:
    """
    Create test app instance
    """

    app_inst = create_app(FLASK_CFG)

    with app_inst.app_context() as app_ctx:
        app_ctx.push()
        JWTManager(app_inst)
        db.drop_all()
        db.create_all()

        yield app_inst
        app_ctx.pop()


@pytest.fixture(scope="class")
def test_client(request, app):
    """
    generates client
    """
    request.cls.client = app.test_client()
