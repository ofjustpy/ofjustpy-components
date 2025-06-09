import ofjustpy as oj
#import devel_hinav_refactored_try2
import devel_hinav_refactored_try4
from starlette.testclient import TestClient
app = oj.load_app()
with TestClient(app) as client:
    response = client.get('/')
