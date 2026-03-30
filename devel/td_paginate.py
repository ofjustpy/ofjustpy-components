import kavya as kv
from kavya_components import Paginate, BiSplitView
from py_tailwind_utils import *


app = kv.load_app()
items = [kv.PD.Halign(kv.PC.Span(text=f"item {i}", twsty_tags=[fw.light, fz.sm, pd/y/2])) for i in range(40 * 20)]
def page_container_gen(cid, childs, **pkwargs):
    hc_types = Dict()
    hc_types.part_viewer = lambda **kwargs: kv.PD.StackV(**kwargs)
    # TODO: replace kv.MD with HCCStatic
    # key=f"{cid}_page_view", 
    hc_types.full_viewer = lambda **kwargs: kv.HS.Div( **kwargs)
    return BiSplitView(childs, hc_types, **pkwargs)


paginate = Paginate("mypaginate",
                    items,
                    page_container_gen,  num_pages=20, chunk_size=40, twsty_tags=[space/y/4, mr/st/8])

paginate_container = kv.MD.Container(key = "paginate_container",
                                          childs = [paginate],
                                          twsty_tags=[H/64]
                                          )


wp_endpoint = kv.create_endpoint(key="example_008",
                                 childs = [paginate_container],
                                 title="example_008",
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )

kv.add_route("/", wp_endpoint)
