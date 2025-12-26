import kavya as kv
from kavya.session_managment.uictx_id_assigner import assign_id
from kavya.htmlcomponents.divactive_impl import _Select
from py_tailwind_utils.skui_tags import (primary,
                                         secondary,
                                         tertiary,
                                         success,
                                         warning,
                                         surface,
                                         error
                                         
                                         )

from py_tailwind_utils import *
color_shades = [primary,
                 secondary,
                 tertiary,
                 success,
                 warning,
                 surface,
                 error
                 
                 ]

class _ColorShadeSelector(_Select):
    svelte_safelist = [bg/option/500 for option in color_shades
                       ]
    
    def __init__(self, *args, **kwargs):
        childs = [
            kv.PC.Option(
                text=str(option),
                value=str(option),
                twsty_tags=[bg / option / 500],
            )
            for option in color_shades
        ]
        super().__init__(*args, **kwargs, childs=childs)

    pass

ColorShadeSelector = assign_id(_ColorShadeSelector)
