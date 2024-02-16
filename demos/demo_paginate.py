"""
drop down color not working in firefox
"""

from py_tailwind_utils import *
import ofjustpy as oj
from addict_tracking_changes import Dict
import ofjustpy_components as ojx
import itertools
import macropy.activate
import with_hyperui



app = oj.load_app()
def on_btn_click(dbref,msg):
    pass

#items = [oj.PC.Span(text=f"item {i}") for i in range(40 * 20)]

items  = [with_hyperui.demo_testimonial(i) for i in range(10 * 6)]
#items = [with_hyperui.demo_testimonial() for i in range(40 * 8)]
xx = with_hyperui.GridUSP()

    
def page_container_gen(cid, childs, **pkwargs):
    hc_types = Dict()
    hc_types.part_viewer = lambda **kwargs: oj.PC.StackV(**kwargs)
    hc_types.full_viewer = lambda **kwargs: oj.HCCStatic.Div(key=f"{cid}_page_view", **kwargs)
    return ojx.BiSplitView(childs, hc_types, **pkwargs)

    
paginate = ojx.Paginate("mypaginate", items, page_container_gen,  num_pages=10, chunk_size=6, twsty_tags=[mr/4])

paginate_container = oj.Mutable.Container(key = "paginate_container",
                                          childs = [paginate],
                                          twsty_tags=[]
                                          )

wp_endpoint = oj.create_endpoint(key="paginate",
                                    childs = [paginate_container,
                                              ],
                                    title="Paginate"
                                    )

oj.add_jproute("/", wp_endpoint)



