

from addict_tracking_changes import Dict
import ofjustpy as oj
from py_tailwind_utils import *
import ofjustpy_components as ojx
import json

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

def terminal_node_callback(spath):
    print ('terminal node selected', spath)
    pass

hn = ojx.HierarchyNavigator(italian_cuisine_hierarchy, terminal_node_callback, key="myhinav")
hn_depth_selector = oj.HCCMutable.StackH(childs = hn.steps, twsty_tags=[space/x/4])

wp_endpoint = oj.create_endpoint(key="hinav",
                              childs = [hn_depth_selector,
                                        oj.Halign(hn.childpanel, content_type="mutable"),
                                   
                                        hn
                                        ],
                              title="Ofjustpy navigator cuisine",
                              twsty_tags=[space/y/4]

                              )


oj.add_jproute("/", wp_endpoint)

