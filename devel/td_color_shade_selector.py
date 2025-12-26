from kavya_components import ColorShadeSelector


css = ColorShadeSelector(key="shadeselector")

from py_tailwind_utils import *

from kavya.type_factory.webpage_type_factory import MutableSSRWebPage_StubWrappedTypeGen
import kavya as kv
from addict import Dict
from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.session_managment.session_manager import get_session_manager, sessionctx

from py_tailwind_utils import *
#Webpage_T = assign_id(MutableSSRWebPage_StubWrappedTypeGen())

app = kv.load_app()

wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [css
                                           # hello_btn,
                                           #       tb_1,
                                           #       tb_2
                                           
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)
