import kavya as kv
from py_tailwind_utils import *
import kavya_components as kvx
from addict_tracking_changes import Dict


#@oj.webpage_cache
# title = kv.PD.Title("Demo: Advanced capabilities",
#                     classes="bg-gradient-to-r bg-clip-text text-3xl font-extrabold text-transparent sm:text-5xl"
#                     )
#from . import dummy_company_section_domain_components 
span1  = kv.AC.Textarea(key="targetSpan1",
                        text="a text area with lots of lots of text",
                        twsty_tags=[bg/green/100, pd/2]
                        )

span2  = kv.AC.Textarea(key="targetSpan2",
                        text="another text area with lots of lots of text",
                        twsty_tags=[bg/blue/100, pd/2]
                        )


dockbar  = kvx.Dockbar([span1, span2],
                       ["Item1", "Item2" ],
                       )
undock_btn_panel = kv.HM.Halign(kv.HM.Div(key = "undock_btn_panel",
                                          childs = dockbar.undock_btns.values(),
                                          twsty_tags=[space/x/4]
                                          )
                                )

wrapped_item_panel = kv.HM.Halign(kv.HM.Div(childs = dockbar.wrapped_components.values(),
                                            twsty_tags=[space/y/4]
                                            ),
                                  )


dock_undock_tlc = kv.MD.Div(key="dock_undock",
                            childs = [undock_btn_panel,
                                      wrapped_item_panel
                                      ],
                            twsty_tags=[space/y/4]
                            )


app = kv.load_app()

wp_endpoint = kv.create_endpoint(key="mutableDiv_SSRPage",
                                 childs = [dock_undock_tlc

                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)
