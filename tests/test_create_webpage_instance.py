import pytest
import sys
import ofjustpy as oj
import sys
from addict import Dict
app = oj.load_app()

sys.path.append("../")
import importlib

from starlette.testclient import TestClient            

@pytest.fixture
def testclient():
    client = TestClient(app)
    return client

@pytest.fixture
def reqobj():
    req = Dict()
    req.session_id = "abc"
    return req

@pytest.fixture(name="demo_mod", params=("demos.demo_mouseover_slideshow",
                                         "demos.demo_two_column_stackv",
                                         "demos.demo_paginate",
                                         "demos.demo_dock_undock",
                                         "demos.demo_hierarchy_navigation_using_italian_cuisine"
                                         )
                )
def _demo_mod(request):
    return request.param

def test_slideshow(demo_mod, testclient, reqobj):
    mouseover_module = importlib.import_module(demo_mod)
    endpoint_func = getattr(mouseover_module, 'wp_endpoint')
    wp_obj = endpoint_func(reqobj)
    response = testclient.get(f'/')

    assert response.status_code == 200


# def test_slideshow(testclient, reqobj):
#     mouseover_module = importlib.import_module(f"demos.demo_mouseover_slideshow")
#     endpoint_func = getattr(mouseover_module, 'wp_endpoint')
#     wp_obj = endpoint_func(reqobj)
#     response = testclient.get(f'/')

#     assert response.status_code == 200
    
