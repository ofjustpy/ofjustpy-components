"""
drop down color not working in firefox
"""
from py_tailwind_utils import *
import kavya as kv
from addict_tracking_changes import Dict
import kavya_components as kvx

app = kv.load_app()

async def on_btn_click(dbref, msg, wp, request):
    print("Color selector called ")
    
    pass
view_directive= Dict()
#TODO: replace Mutable ==> HCCMutable
view_directive.part_viewer = lambda **kwargs: kv.MD.StackV(**kwargs)
view_directive.full_viewer = lambda **kwargs: kv.MD.Div(**kwargs)
    
def gen_cs():
    for idx in range(0, 20):
        yield kvx.ColorSelector(key = f"tc_colorselector_{idx}",
                                       on_click = on_btn_click
                                       )
                             
                
twocolumn_view = kvx.BiSplitView([_ for _ in gen_cs()],
                             view_directive,
                             twsty_tags=[W/full])

twocolumn_container = kv.MD.Container(key="twocolumn_container",
                                           childs = [twocolumn_view],
                                           title = "Two column"
                                           
                                           )
wp_endpoint = kv.create_endpoint(key="two columns",
                                    childs = [twocolumn_container
                                              ],
                                    title="Two column items viewer",
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                    )

kv.add_route("/", wp_endpoint)


