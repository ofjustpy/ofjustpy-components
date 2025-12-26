import kavya as kv
from kavya_components import ColorShadeSelector
from starlette.testclient import TestClient

color_shade_selector = ColorShadeSelector(key="color_shade_selector")

app = kv.load_app()

wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [color_shade_selector
                                           #
                                           #       tb_1,
                                           #       tb_2
                                           
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)


testclient = TestClient(app)
response = testclient.get(f'/')
print(response.text)
