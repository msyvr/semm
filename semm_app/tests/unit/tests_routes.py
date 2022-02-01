# /semm/semm_app/tests/unit/tests_routes.py

import pytest

from flask import request, jsonify
from semm_app import create_app
from routes import siwe_restricted

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))

async def test_index(test_cli):
    resp = await test_cli.get('/')
    assert resp.status == 200

async def test_index(test_cli):
    resp = await test_cli.get('/info')
    assert resp.status == 200

async def test_index(test_cli):
    resp = await test_cli.get('/credentials_not_verified')
    assert resp.status == 200

async def test_index(test_cli):
    resp = await test_cli.get('/siwe_restricted')
    assert resp.status == 200