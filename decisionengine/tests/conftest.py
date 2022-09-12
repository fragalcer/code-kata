import pytest
from decisionengine.app import app as decisionengine_app


@pytest.fixture()
def app():
    app = decisionengine_app
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
