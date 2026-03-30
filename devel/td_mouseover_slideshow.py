from py_tailwind_utils import *
import kavya as kv
from addict_tracking_changes import Dict
import kavya_components as kvx
from py_tailwind_utils import space, y


app = kv.load_app()

slide_labels = ["easy_to_use" ,
                "batteries_included",
                 "interactivity",
                 "performant",
                 "tradeoffs",
                 "misc"
    ]


slide_info = { "easy_to_use": ("Easy to use",
                               kv.PD.Ul(childs=[kv.PC.Li(text="Unified Python approach - Eliminates need for multiple languages (JavaScript, Jinja2, CSS, HTML)"),
                                             kv.PC.Li(text="Versatile Python APIs - Tackle all web development tasks, including UI events, styling, and layout"),
                                             kv.PC.Li(text="Efficient component interaction - Easily manipulate complex elements like docking panels and hierarchical navigation")
])
                               ),
               "batteries_included": ("Batteries included",
                                      kv.PD.Ul(
                                          childs=[
                                              kv.PC.Li(text="Session management"),
                                              kv.PC.Li(text="Signed cookie management"),
                                              kv.PC.Li(text="User authentication"),
                                              kv.PC.Li(text="Database interaction hooks"),
                                              kv.PC.Li(text="Style/theme manipulation: overwrite, merge styles")
                                          ]
                                      )
                                      ),
               "interactivity": ("Build for interactivity",
                                  kv.PD.Ul(
                                      childs=[
                                          kv.PC.Li(text="Effortlessly handle browser UI events in Python"),
                                          kv.PC.Li(text="Dynamically modify browser UI elements from Python"),
                                          kv.PC.Li(text="Incorporates an Elm-inspired React modeling framework")
                                      ]
                                  )
                                  ),
               "performant": ("Performant",
                              kv.PD.Ul(
                                  childs=[
                                      kv.PC.Li(text="ASGI: Concurrent sessions in a single Python thread"),
                                      kv.PC.Li(text="Svelte runtime on browser: Optimized for speed"),
                                      kv.PC.Li(text="NGINX web server in C: Engineered for speed")
                                  ]
                              )
                              ),
               "tradeoffs": ("Design tradeoffs",
                             kv.PD.Ul(
                                    childs=[
                                        kv.PC.Li(text="Prioritizes ease of use over performance"),
                                        kv.PC.Li(text="Encourages good programming practices: Readability, Reusability, Maintainability"),
                                        kv.PC.Li(text="Comprehensive: Covers all web development aspects - layout, styling, reactivity, components")
                                    ]
                                    )

                             ),
               "misc": ("Misc",

                        kv.PD.Ul(
                               childs=[
                                   kv.PC.Li(text="Comprehensive documentation: Detailed guides and resources for easy understanding"),
                                   kv.PC.Li(text="Extensive testing: Robust testing capabilities for reliable applications"),
                                   kv.PC.Li(text="Low learning curve: Designed for quick adoption and user-friendly experience"),
                                   kv.PC.Li(text="Open source: Free to use and contribute, fostering community-driven development"),
                                   kv.PC.Li(text="Easily extensible: Built-in plugin framework allows seamless integration of new features")
                               ]
                               )
                        
                        )
               
               }

slideShow = kvx.SlideShow("demo_slideshow",
                      slide_labels,
                      slide_info,
                      "misc"
                      )


wp_endpoint = kv.create_endpoint(key="mouseover_slideshow",
                                 childs = [slideShow
                                           # hello_btn,
                                           #       tb_1,
                                           #       tb_2
                                           
                                           ],
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )
kv.add_route("/", wp_endpoint)
