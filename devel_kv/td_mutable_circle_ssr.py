from kavya_components.linear_selector import Circle

def on_click(*args):
    pass

circle = Circle(key="circle_1",
                text="hello",
                on_click=on_click
                )

# class ParentDummy:
#     def add_component(*args, **kwargs):
#         pass
#     pass

# parent_dummy = ParentDummy()

# circle_linked = circle.stub()(parent_dummy)

# print(list(circle_linked.to_html_iter()))

# from py_tailwind_utils import *

import kavya as kv
from addict import Dict

app = kv.load_app()
wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [circle
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 svelte_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)
from addict import Dict

request = Dict()
request.session.session_id = "abc-123-xyz"
wp = wp_endpoint(request)
print("".join(wp.to_html_iter())
      )
# print(wp.components)
