from addict_tracking_changes import Dict
import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_components as ojx
import json
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
from py_tailwind_utils import *
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.HCType import HCType
from ofjustpy.ui_styles import sty
from ofjustpy import ui_styles
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy.HC_TF import gen_HC_type

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

class BreadcrumbPanel(oj.HCCMutable.Div):
    def __init__(self, num_steps, on_click_eh):
        
        
        # first add house as root step with no text
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
    
class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")

        
ChildSlotBtn_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Button",
        TR.SpanMixin,
        staticCoreMixins=[],
        mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin], # value, style, and text : all is mutable
        stytags_getter_func=lambda m=ui_styles: m.sty.span,
    )
)

class ChildsPanel(oj.HCCMutable.Div):
    def __init__(self, on_child_slot_clicked, *args, max_childs=20,**kwargs):
        """
        event handler when childslot is clicked
        """

        
        self.childslots = [
                ChildSlotBtn_HCType(
                    key=f"cbtn{i}",
                    text=str(i),
                    value=i,
                    classes="rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hower:shadow-indigo-300 focus:bg-gradient-to-bl focus:border-indigo-500/50 focus:border",
                    
                    
                    # twsty_tags=[
                    #     db.f,
                    #     ji.center,
                    #     gap/2,
                    #     bd/blue/500,
                    #     bg/blue/50,
                    #     pd/y/3,
                    #     pd/x/4,
                    #     fc/blue/700
                        
                    # ],
                    extra_classes="border-s-[3px]",
                    
                    on_click=on_child_slot_clicked #lambda *args, hinav=self: on_childbtn_click(*args, hinav),
                )
                for i in range(max_childs)
            ]

        menu_box = oj.HCCMutable.Div(classes="mt-6 flex-1 space-y-4 h-screen", childs = self.childslots)
        

            
        super().__init__(childs = [menu_box],
                         classes = "flex overflow-y-auto w-80 h-screen flex-col justify-between border-e bg-white"
                         #twsty_tags = [max / W / "md", space / y / 2]
                         
                         )
        

    def hide_all_slots(self, target_of):
        for cs in self.childslots:
            shell = target_of(cs)
            shell.add_twsty_tags(noop / hidden)

    def update_child_panel(self, showitem, target_of):
        for cs, clabel in zip(
            self.childslots,
            filter(lambda x: x != "_cref", showitem.keys()),
        ):
            cs_shell = target_of(cs)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.add_twsty_tags(db.f) # some bug about flex being removed if component is hidden 

            cs_shell.text = clabel
            cs_shell.value = clabel
            
        pass

    
HierarchyNavigator = ojx.HierarchyNavigator_TF(BreadcrumbPanel, ChildsPanel)
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

def terminal_node_callback(spath, msg):
    print ('terminal node selected', spath)
    pass

hn = HierarchyNavigator(italian_cuisine_hierarchy,
                            terminal_node_callback,
                            key="myhinav",
                                 )
wp_endpoint = oj.create_endpoint(key="hinav",
                              childs = [hn.breadcrumb_panel,
                                        hn.childpanel,
                                   
                                        hn
                                        ],
                              title="Ofjustpy navigator cuisine",
                                 twsty_tags=[space/y/4],
                                 head_html="""<script src="https://cdn.tailwindcss.com"></script>"""

                              )


oj.add_jproute("/", wp_endpoint)
