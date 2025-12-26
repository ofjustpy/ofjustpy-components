"""
drop down color not working in firefox
"""
from py_tailwind_utils import *
import kavya as kv
from addict_tracking_changes import Dict
import kavya_components as kvx

app = oj.load_app()

def on_btn_click(dbref, msg, target_of):
    print("Color selector called ")
    
    pass
view_directive= Dict()
#TODO: replace Mutable ==> HCCMutable
view_directive.part_viewer = lambda **kwargs: kv.MD.StackV(**kwargs)
view_directive.full_viewer = lambda **kwargs: kv.MD.Div(**kwargs)
    
def gen_cs():
    for idx in range(0, 20):
        yield oj.Mutable.ColorSelector(key = f"tc_colorselector_{idx}",
                                       on_click = on_btn_click
                                       )
                             
                
twocolumn_view = ojx.BiSplitView([_ for _ in gen_cs()],
                             view_directive,
                             twsty_tags=[W/full])

twocolumn_container = oj.Mutable.Container(key="twocolumn_container",
                                           childs = [twocolumn_view],
                                           title = "Two column"
                                           
                                           )
wp_endpoint = oj.create_endpoint(key="two columns",
                                    childs = [twocolumn_container
                                              ],
                                    title="Two column items viewer"
                                    )

oj.add_jproute("/", wp_endpoint)


