

from addict_tracking_changes import Dict
import ofjustpy as oj
from py_tailwind_utils import *
from ofjustpy_components.hierarchy_naviator_refactored_try3 import HierarchyNavigator_TF, BaseChildsPanelMixin
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
app = oj.load_app()
italian_cuisine_hierarchy = {
    "Cuisine: Italian": {
        "Regions": {
            "Northern Italian cuisine": {
                "Description": "Characterized by less use of olive oil, tomatoes and pasta, and more use of butter, rice, corn (polenta), and cheeses for cream sauces. Includes regions like Lombardy, Piedmont, Veneto, Emilia-Romagna, Liguria.",
                "Dishes": {
                    "Risotto alla Milanese": {
                        "Ingredients": {
                            "Arborio or Carnaroli rice": 1,
                            "Saffron": 1,
                            "Parmesan cheese": 1,
                            "Beef or Chicken stock": 1,
                            "Butter": 1,
                            "Onion or Shallot": 1,
                            "White Wine": 1,
                            "Beef marrow (traditional)": 1
                        },
                        "Techniques": {
                            "Making Soffritto": 1,
                            "Toasting rice (Tostatura)": 1,
                            "Deglazing with wine": 1,
                            "Gradually adding hot stock": 1,
                            "Adding saffron": 1,
                            "Mantecatura (Finishing with butter and Parmesan)": 1
                        },
                        "Utensils": {
                            "Heavy-bottomed pan or pot": 1,
                            "Wooden spoon": 1,
                            "Ladle": 1
                        }
                    },
                    "Osso Buco": {
                        "Description": "Braised veal shanks, often served with Risotto alla Milanese.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Polenta": {
                        "Description": "Boiled cornmeal dish, served soft or allowed to set and then fried or grilled.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Lasagne alla Bolognese": {
                        "Description": "Layered pasta dish with Ragù Bolognese, Béchamel sauce, and Parmesan cheese.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Pesto alla Genovese": {
                        "Description": "Sauce originating from Genoa (Liguria) made with basil, pine nuts, garlic, Parmesan, Pecorino Sardo, and olive oil.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Tiramisu": {
                        "Description": "Coffee-flavored dessert with ladyfingers, mascarpone cheese, eggs, and cocoa. Origins debated, often associated with Veneto.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                }
            },
            "Central Italian cuisine": {
                "Description": "Features simple preparations, emphasizing high-quality local ingredients like olive oil, pecorino cheese, cured meats, legumes, and seasonal vegetables. Includes regions like Tuscany, Umbria, Lazio, Marche.",
                "Dishes": {
                    "Spaghetti alla Carbonara": {
                        "Ingredients": {
                            "Spaghetti or Rigatoni pasta": 1,
                            "Guanciale (cured pork jowl - traditional)  or  Pancetta": 1,
                            "Eggs (yolks often preferred)": 1,
                            "Pecorino Romano cheese": 1,
                            "Black pepper": 1
                        },
                        "Techniques": {
                            "Cooking pasta al dente": 1,
                            "Rendering Guanciale or Pancetta": 1,
                            "Creating sauce emulsion with egg, cheese, pepper, and pasta water off heat": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet for cooking meat": 1,
                            "Bowl for mixing sauce": 1
                        }
                    },
                    "Bistecca alla Fiorentina": {
                        "Description": "Thick-cut T-bone steak (Chianina cattle traditionally) grilled rare.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Saltimbocca alla Romana": {
                        "Description": "Veal cutlets topped with prosciutto and sage, pan-fried.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Pasta Cacio e Pepe": {
                        "Description": "Simple pasta dish with Pecorino Romano cheese and black pepper.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Panzanella": {
                        "Description": "Tuscan bread salad with stale bread, tomatoes, onions, basil, olive oil, and vinegar.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Fettuccine Alfredo (Italian origin: Fettuccine al Burro)": {
                        "Description": "Pasta dish with butter and Parmesan cheese. The cream-heavy version is more Italian-American.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                }
            },
            "Southern Italian cuisine": {
                "Description": "Known for its vibrant flavors, extensive use of olive oil, tomatoes, fresh vegetables (like eggplant, peppers), seafood, and dried pasta shapes. Includes mainland regions like Campania, Puglia, Calabria, Basilicata, and the islands.",
                "Dishes": {
                    "Pizza Margherita": {
                        "Ingredients": {
                            "Pizza dough (flour, water, yeast, salt)": 1,
                            "San Marzano Tomatoes (or other high-quality tomatoes)": 1,
                            "Mozzarella di Bufala Campana (or Fior di Latte Mozzarella)": 1,
                            "Fresh Basil": 1,
                            "Olive oil": 1
                        },
                        "Techniques": {
                            "Kneading and proofing dough": 1,
                            "Stretching and shaping the dough": 1,
                            "Making simple tomato sauce": 1,
                            "Topping and baking (traditionally in a wood-fired oven)": 1
                        },
                        "Utensils": {
                            "Oven (preferably high-temperature)": 1,
                            "Pizza stone or baking steel or sheet": 1,
                            "Pizza peel": 1
                        }
                    },
                    "Pasta alla Puttanesca": {
                        "Ingredients": {
                            "Spaghetti or Linguine pasta": 1,
                            "Tomatoes (canned or fresh)": 1,
                            "Black Olives (Gaeta traditionally)": 1,
                            "Capers": 1,
                            "Garlic": 1,
                            "Anchovies": 1,
                            "Red pepper flakes (optional)": 1,
                            "Olive oil": 1
                        },
                        "Techniques": {
                            "Making a quick, pungent tomato sauce": 1,
                            "Cooking pasta al dente": 1,
                            "Tossing pasta with sauce": 1
                        },
                        "Utensils": {
                            "Large pot for boiling pasta": 1,
                            "Skillet or Sauté pan for making sauce": 1
                        }
                    },
                    "Parmigiana di Melanzane (Eggplant Parmesan)": {
                        "Description": "Layered dish of fried eggplant slices, tomato sauce, mozzarella, Parmesan, and basil.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    },
                    "Orecchiette con Cime di Rapa": {
                        "Description": "Ear-shaped pasta with broccoli rabe, often includes anchovies and garlic. Signature dish of Puglia.",
                        "Ingredients": 1,
                        "Techniques": 1,
                        "Utensils": 1
                    }
                },
                "Subregions": {
                     "Sicilian cuisine": {
                        "Description": "Influenced by various cultures (Greek, Arab, Norman, Spanish), featuring unique ingredients like pistachios, almonds, citrus, tuna, swordfish, ricotta, and eggplant.",
                        "Dishes": {
                            "Pasta alla Norma": {
                                "Description": "Pasta (often Maccheroni) with tomatoes, fried eggplant, salted ricotta cheese (Ricotta Salata), and basil.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Arancini": {
                                "Description": "Fried rice balls, usually stuffed with ragù, mozzarella, and peas, or other variations.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Caponata": {
                                "Description": "Sweet and sour eggplant relish with celery, olives, capers, and tomatoes.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                             "Cannoli": {
                                "Description": "Tube-shaped fried pastry shells filled with sweet, creamy ricotta filling.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                            "Cassata Siciliana": {
                                "Description": "Elaborate sponge cake soaked in liqueur or fruit juice, layered with ricotta cheese filling, covered in marzipan and decorated with candied fruit.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            },
                           "Pasta con le Sarde": {
                                "Description": "Pasta dish with sardines, wild fennel, pine nuts, raisins, and saffron.",
                                "Ingredients": 1,
                                "Techniques": 1,
                                "Utensils": 1
                            }
                        }
                    }
                }
            }
        }
    }
}

async def terminal_node_callback(spath, msg):
    print ('terminal node selected', spath)
    pass

class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")


        

# ChildSlot: Button with Mutable text type
ChildSlotBtn_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Button",
        TR.SpanMixin,
        staticCoreMixins=[],
        mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin], # value, style, and text : all is mutable
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
)

childslot_event_handlers = {'on_click': terminal_node_callback,

}

class ChildsPanelMixin(BaseChildsPanelMixin):
    def get_childslots(self):

        return self.childslots
    
ChildsPanelDiv = gen_Div_type(HCType.hcc_mutable_div, "HCCMutableDiv", TR.DivMixin,
                   static_addon_mixins = [ChildsPanelMixin]
                   )
class ChildSlotsPanel(ChildsPanelDiv):
    # modify on_child_slot_clicked shouldn't be the first argument
    def __init__(self,
                 childslot_event_handlers,
                 *args,
                 max_childs=20,

                 **kwargs):
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
                    **childslot_event_handlers
                    #on_click=on_child_slot_clicked,
                )
                for i in range(max_childs)
            ]
        menu_box = oj.HCCMutable.Div(classes="mt-6 flex-1 space-y-4 h-screen", childs = self.childslots)
        super().__init__(childs = [menu_box],
                         classes = "flex overflow-y-auto min-w-fit h-screen flex-col justify-between border-e bg-white"
                         )



def childslots_panel_gen(event_handlers):
    # Panel specific parameters like max_childs  go here
    return ChildSlotsPanel(event_handlers,  
                           max_childs=20,)

HierarchyNavigator = assign_id(HierarchyNavigator_TF(childslots_panel_gen))
hn = HierarchyNavigator(italian_cuisine_hierarchy,
                        childslot_event_handlers,
                        max_depth = 13,
                        key="myhinav")
#hn_depth_selector = oj.HCCMutable.StackH(childs = hn.steps, twsty_tags=[space/x/4])

wp_endpoint = oj.create_endpoint(key="hinav",
                              childs = [hn.breadcrumb_panel,
                                        oj.Halign(hn.childslots_panel, content_type="mutable"),
                                   
                                        hn
                                        ],
                              title="Ofjustpy navigator cuisine",
                              twsty_tags=[space/y/4],
                              csr_bundle_dir="skeletonui_bundle",

                              )


oj.add_jproute("/", wp_endpoint)

