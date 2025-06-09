from ofjustpy.MHC_types import (
    Label as MLabel,
    HCCMutable,
    Button as MButton,
    HCCStatic,
    StackH as MStackH,
)
import ofjustpy as oj
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.SHC_types import PassiveComponents as PC, ActiveComponents as AC
from py_tailwind_utils import *
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy_engine.HCType import HCType
from ofjustpy.ui_styles import sty
from ofjustpy import ui_styles
from ofjustpy.Div_TF import gen_Div_type

# require for arrow button which is special type of mutable
# the text is mutable; but the twsty-tags remains the same

from ofjustpy.HC_TF import gen_HC_type
from ofjustpy.htmlcomponents import MDiv

import traceback
import sys
class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")


SlotBtn_DivType =     gen_Div_type(
        HCType.mutable,
        "Button",
        TR.ButtonMixin,
        mutable_shell_mixins=[TR.HCTextMixin,  ValueMixin], # value, style, and text : all is mutable
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
    
MSlotBtn_DivType = assign_id(SlotBtn_DivType

)

class VarListDiv_MutableShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys  = [noop/hidden]
    def __init__(self, **kwargs):
        self.hide_all_slots()
        
        pass
    
    def hide_all_slots(self):
        for cs in self.components:
            #shell = target_of(cs)
            shell = cs
            shell.add_twsty_tags(noop / hidden)

    #def update_child_panel(self, showitems, values):            
    def update_child_panel(self, showitems, values):
        for cs, clabel, cvalue in zip(self.components,
                              showitems,
                              values
                              ):
            cs_shell = cs #target_of(cs)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.text = clabel
            cs_shell.value = cvalue
            
            
        pass



def top_container_ev(dbref, msg, to_ms):
    pass
def TF(SlotType = MSlotBtn_DivType,
       runtime_behaviour_type = HCType.mutable,
       ContainerMixin = TR.DivMixin
       ):

    _StaticCore = gen_Div_type(runtime_behaviour_type,
                               "VarListDiv",
                               ContainerMixin,
                               mutable_shell_mixins=[VarListDiv_MutableShellMixin], # value, style, and text : all is mutable
                               stytags_getter_func=lambda m=ui_styles: m.sty.varlistdiv,
                               )

    class _VarListDiv(_StaticCore):
        def __init__(self, *args,
                     max_slots = 20,
                     slot_event_handlers = None,
                     **kwargs):

            if slot_event_handlers is None:
                slot_event_handlers = {}

            key = kwargs.get("key")
            with oj.uictx(f"VL_{key}"):
                self.slots = [SlotType(key=f"slot_{i}",
                                       text=str(i),
                                       value=i,


                                       extra_classes="hover:border-s-[3px] hover:border-gray-100 border-s-[3px]  border-s-pink-50/10",
                                       **slot_event_handlers


                                       )
                              for i in range(max_slots)
                              ]
                    
            #menu_box = oj.HCCMutable.Div(classes="mt-6 flex-1 space-y-4 flex flex-col p-2", childs = self.slots)

            # twsty_tags = encode_twstr("mt-6 space-y-4 flex flex-col p-2")
            # twsty_tags = conc_twtags(*kwargs.pop("twsty_tags", []), *twsty_tags)
            
            
            super().__init__(
                             childs = self.slots,
                             **kwargs
                             )
            

    #VarListDiv = assign_id(_VarListDiv)
    return _VarListDiv

# super().__init__(classes = "flex overflow-y-auto min-w-fit  flex-col justify-between border-e bg-white",
#                  childs = [menu_box],
#                  )
