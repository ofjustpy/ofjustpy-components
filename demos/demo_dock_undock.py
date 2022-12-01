"""
drop down color not working in firefox
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
import ofjustpy_components as ojx
from ofjustpy_components.htmlcomponents import  BiSplitView, Paginate, Dockbar
from py_tailwind_utils import space, y

app = oj.load_app()
def on_btn_click(dbref,msg):
    pass


span1  = oj.AC.Textarea(key="targetSpan1",
                        text="a text area with lots of lots of text",
                        pcp=[bg/green/1, pd/2]
                     )
span2  = oj.AC.Textarea(key="targetSpan2",
                       text="another text area with lots of lots of text",
                       pcp=[bg/blue/1, pd/2]
                       )

            
dockbar  = Dockbar([span1, span2],
                   ["Item1", "Item2" ],
                   )

undock_btn_panel = oj.Halign(oj.HCCMutable.Div(key = "undock_btn_panel",
                                     childs = dockbar.undock_btns.values(),
                                     twsty_tags=[space/x/4]
                                               ),
                             content_type="mutable"
                             )


wrapped_item_panel = oj.Halign(oj.HCCMutable.Div(
                                       childs = dockbar.wrapped_components.values(),
                                       twsty_tags=[space/y/4]
                                       ),
                               content_type="mutable"
                               )


dock_undock_tlc = oj.Mutable.Div(key="dock_undock",
                                       childs = [undock_btn_panel,
                                                 wrapped_item_panel
                                                 ],
                                       twsty_tags=[space/y/4]
                                       )

dock_undock_container = oj.Mutable.Container(key="dock_undock_container",
                                             childs = [dock_undock_tlc]
                                             )



wp_endpoint = oj.create_endpoint(key="dock_undock",
                                    childs = [dock_undock_container
                                              ],
                                    title="Docking/Undocking"
                                    )

oj.add_jproute("/", wp_endpoint)



