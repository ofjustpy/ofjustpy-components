"""
use custom ui for breadcrumbs
"""


from addict_tracking_changes import Dict
import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_components as ojx
import json

oj.set_style("un")

app = oj.load_app()
italian_cuisine_hierarchy = json.loads("""
{
    "Cuisine: Italian": {
        "Regions": {
            "Northern Italian cuisine": {
                "Dishes": {
                    "Risotto alla Milanese": {
                        "Ingredients": {
                            "Arborio rice": 1,
                            "Saffron": 1,
                            "Parmesan cheese": 1,
                            "Chicken stock": 1
                        },
                        "Techniques": {
                            "Toasting rice": 1,
                            "Adding saffron": 1,
                            "Gradually adding stock": 1,
                            "Finishing with Parmesan cheese": 1
                        },
                        "Utensils": {
                            "Risotto pan": 1,
                            "Wooden spoon": 1
                        }
                    },
                    "Osso Buco": 1,
                    "Polenta": 1,
                    "Tiramisu": 1
                }
            },
            "Central Italian cuisine": {
                "Dishes": {
                    "Spaghetti alla Carbonara": {
                        "Ingredients": {
                            "Spaghetti pasta": 1,
                            "Pancetta": 1,
                            "Eggs": 1,
                            "Pecorino Romano cheese": 1
                        },
                        "Techniques": {
                            "Cooking pasta al dente": 1,
                            "Making the sauce with eggs and cheese": 1,
                            "Crisping pancetta": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for cooking pancetta and making sauce": 1
                        }
                    },
                    "Fettuccine Alfredo": 1,
                    "Bistecca alla Fiorentina": 1,
                    "Panzanella": 1
                }
            },
            "Southern Italian cuisine": {
                "Dishes": {
                    "Pizza Margherita": {
                        "Ingredients": {
                            "Pizza dough": 1,
                            "Tomatoes": 1,
                            "Mozzarella cheese": 1,
                            "Basil": 1
                        },
                        "Techniques": {
                            "Stretching and shaping the dough": 1,
                            "Making tomato sauce": 1,
                            "Topping with cheese and basil": 1
                        },
                        "Utensils": {
                            "Pizza stone or baking sheet": 1,
                            "Pizza peel": 1
                        }
                    },
                    "Pasta alla Puttanesca": {
                        "Ingredients": {
                            "Spaghetti pasta": 1,
                            "Tomatoes": 1,
                            "Olives": 1,
                            "Capers": 1
                        },
                        "Techniques": {
                            "Making tomato sauce with olives and capers": 1,
                            "Cooking pasta al dente": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for making tomato sauce": 1
                        }
                    },
                    "Caponata": 1,
                    "Arancini": 1
                }
            },
            "Sicilian cuisine": {
                "Dishes": {
                    "Pasta alla Norma": 1,
                    "Arancini": 1,
                    "Cannoli": 1,
                    "Cassata": 1
                }
            }
        }
    }
}
"""
)
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.HC_TF import gen_HC_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles

ArrowSpan_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Span",
        TR.SpanMixin,
        staticCoreMixins=[TR.TwStyMixin],
        mutableShellMixins=[TR.HCTextMixin],
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )
)

def BaseWithHighlightedActiveLink():
    comp_box = oj.HCCMutable.Ul()

    def add_item(text):
        oj.HCCMutable.Li(childs= [oj.Mutable.Button(classes="flex items-center gap-2 border-s-[3px] border-blue-500 bg-blue-50 px-4 py-3 text-blue-700", childs = [oj.PD.Span(classes="text-sm font-medium", text=text)

            ]

                                    )
                          ]
                 )
        
    comp_box.add_item = add_item
    return comp_box


class ui_breadcrumb_panel(oj.HCCMutable.Div):

    def __init__(self, num_steps, on_click_eh):
        
        
        # first add house
        house = oj.PD.Li(childs = [oj.PC.Div(classes="block transition hover:text-gray-700",
                                             childs = [
                                                 oj.PC.Span(classes="sr-only", text="home"),
                                                 oj.icons.FontAwesomeIcon(label="faHouse",
                                                                       classes="w-5 h-5")
                                                 ]

                                             )
                           

                           ]
                 )
        
        self.arrows = [house, 
                       *[oj.AD.Button(
                key=f"btn{i}",
                value=i,
                childs = [oj.icons.FontAwesomeIcon(label="faAngleRight",
                                                   classes="w-5 h-5 bg-white",
                                                   )

                          ],
                           classes="bg-white p-0",
                           
                on_click=on_click_eh
            )
            for i in range(1, num_steps)]
        ]
        self.labels = [
            ArrowSpan_HCType(key=f"label{i}", text="", twsty_tags=[mr / x / 0])
            for i in range(num_steps)
        ]
        self.steps = [
            oj.Mutable.StackH(
                key=f"item{idx}",
                childs=[self.labels[idx], self.arrows[idx]],
                twsty_tags=[
                mr / x / 0,
                noop / hidden,
                pd/2
            ],
        )
            for idx in range(num_steps)
        ]

        crumb_list =  oj.HCCMutable.Ul(classes="flex items-center gap-1 text-sm text-gray-600",
                                       childs=[*self.steps]
                                       )
        
        super().__init__(childs = [crumb_list])
        pass
    
    def get_step_at_idx(self, idx):
        return self.steps[idx]
    
    def update_step_text(self, idx, label_text, to_ms):
        label = self.labels[idx]
        label_ms = to_ms(label)
        label_ms.text = label_text
        
        
def terminal_node_callback(spath, msg):
    print ('terminal node selected', spath)
    pass

hn = ojx.HierarchyNavigator(italian_cuisine_hierarchy,
                            terminal_node_callback,
                            key="myhinav",
                            ui_breadcrumb_panel = ui_breadcrumb_panel
                            )
#hn_depth_selector = oj.HCCMutable.StackH(childs = hn.steps, twsty_tags=[space/x/4])

wp_endpoint = oj.create_endpoint(key="hinav",
                              childs = [hn.breadcrumb_panel,
                                        oj.Halign(hn.childpanel, content_type="mutable"),
                                   
                                        hn
                                        ],
                              title="Ofjustpy navigator cuisine",
                              twsty_tags=[space/y/4]

                              )


oj.add_jproute("/", wp_endpoint)


