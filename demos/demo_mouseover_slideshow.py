import ofjustpy as oj
import  ofjustpy_components as ojx

app = oj.load_app()
slide_labels = ["easy_to_use" ,
                "batteries_included",
                 "interactivity",
                 "performant",
                 "tradeoffs",
                 "misc"
    ]

slide_info = { "easy_to_use": ("Easy to use",
                               oj.PC.Ul(childs=[oj.PC.Li(text="Unified Python approach - Eliminates need for multiple languages (JavaScript, Jinja2, CSS, HTML)"),
                                             oj.PC.Li(text="Versatile Python APIs - Tackle all web development tasks, including UI events, styling, and layout"),
                                             oj.PC.Li(text="Efficient component interaction - Easily manipulate complex elements like docking panels and hierarchical navigation")
])
                               ),
               "batteries_included": ("Batteries included",
                                      oj.PC.Ul(
                                          childs=[
                                              oj.PC.Li(text="Session management"),
                                              oj.PC.Li(text="Signed cookie management"),
                                              oj.PC.Li(text="User authentication"),
                                              oj.PC.Li(text="Database interaction hooks"),
                                              oj.PC.Li(text="Style/theme manipulation: overwrite, merge styles")
                                          ]
                                      )
                                      ),
               "interactivity": ("Build for interactivity",
                                  oj.PC.Ul(
                                      childs=[
                                          oj.PC.Li(text="Effortlessly handle browser UI events in Python"),
                                          oj.PC.Li(text="Dynamically modify browser UI elements from Python"),
                                          oj.PC.Li(text="Incorporates an Elm-inspired React modeling framework")
                                      ]
                                  )
                                  ),
               "performant": ("Performant",
                              oj.PC.Ul(
                                  childs=[
                                      oj.PC.Li(text="ASGI: Concurrent sessions in a single Python thread"),
                                      oj.PC.Li(text="Svelte runtime on browser: Optimized for speed"),
                                      oj.PC.Li(text="NGINX web server in C: Engineered for speed")
                                  ]
                              )
                              ),
               "tradeoffs": ("Design tradeoffs",
                             oj.PC.Ul(
                                    childs=[
                                        oj.PC.Li(text="Prioritizes ease of use over performance"),
                                        oj.PC.Li(text="Encourages good programming practices: Readability, Reusability, Maintainability"),
                                        oj.PC.Li(text="Comprehensive: Covers all web development aspects - layout, styling, reactivity, components")
                                    ]
                                    )

                             ),
               "misc": ("Misc",

                        oj.PC.Ul(
                               childs=[
                                   oj.PC.Li(text="Comprehensive documentation: Detailed guides and resources for easy understanding"),
                                   oj.PC.Li(text="Extensive testing: Robust testing capabilities for reliable applications"),
                                   oj.PC.Li(text="Low learning curve: Designed for quick adoption and user-friendly experience"),
                                   oj.PC.Li(text="Open source: Free to use and contribute, fostering community-driven development"),
                                   oj.PC.Li(text="Easily extensible: Built-in plugin framework allows seamless integration of new features")
                               ]
                               )
                        
                        )
               
               }

slideShow = ojx.SlideShow("demo_slideshow",
                      slide_labels,
                      slide_info,
                      "misc"
                      )

wp_endpoint = oj.create_endpoint(key="demo_slideshow",
                          childs = [slideShow],
                                 title="Mouseover slideshow",
                                 csr_bundle_dir="hyperui"
                        )

oj.add_jproute("/", wp_endpoint)

