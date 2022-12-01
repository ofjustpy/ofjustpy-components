"""
drop down color not working in firefox
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
import ofjustpy_components as ojx
import itertools

app = oj.load_app()
def on_btn_click(dbref,msg):
    pass

items = [oj.PC.Span(text=f"item {i}") for i in range(40 * 20)]
def page_container_gen(cid, childs, **pkwargs):
    hc_types = Dict()
    hc_types.part_viewer = lambda **kwargs: oj.PC.StackV(**kwargs)
    hc_types.full_viewer = lambda **kwargs: oj.HCCStatic.Div(key=f"{cid}_page_view", **kwargs)
    return ojx.BiSplitView(childs, hc_types, **pkwargs)

    
paginate = ojx.Paginate("mypaginate", items, page_container_gen,  num_pages=20, chunk_size=40)

paginate_container = oj.Mutable.Container(key = "paginate_container",
                                          childs = [paginate],
                                          twsty_tags=[H/64]
                                          )


wp_endpoint = oj.create_endpoint(key="paginate",
                                    childs = [paginate_container
                                              ],
                                    title="Paginate"
                                    )

oj.add_jproute("/", wp_endpoint)



