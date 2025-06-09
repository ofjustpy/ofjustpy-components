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

class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")

        
SlotBtn_HCType = assign_id(
    gen_HC_type(
        HCType.mutable,
        "Slot",
        TR.SpanMixin,
        staticCoreMixins=[],
        mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin], # value, style, and text : all is mutable
        stytags_getter_func=lambda m=ui_styles: m.sty.button,
    )
)

# Ideally, use Div_TF to generate a mutable div with
# mixins for update_child_panel, hide_all_slots as part of
# mutable shells
class _VarListDiv(MDiv):
    def __init__(self,
                 key,
                 on_slot_clicked,
                 *args,
                 max_slots=20,
                 **kwargs):
        """
        event handler when childslot is clicked
        """

        
        self.slots = [
                SlotBtn_HCType(
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
                    
                    on_click=on_slot_clicked,
                )
                for i in range(max_slots)
            ]


        menu_box = oj.HCCMutable.Div(classes="mt-6 flex-1 space-y-4 flex flex-col p-2", childs = self.slots)
        

            
        super().__init__(key=key, childs = [menu_box],
                         classes = "flex overflow-y-auto min-w-fit  flex-col justify-between border-e bg-white"
                         #twsty_tags = [max / W / "md", space / y / 2]
                         
                         )
        

    def hide_all_slots(self, target_of):
        for cs in self.slots:
            shell = target_of(cs)
            shell.add_twsty_tags(noop / hidden)

    def update_child_panel(self, showitems, target_of):
        for cs, clabel in zip(
            self.slots,
                showitems
        ):
            cs_shell = target_of(cs)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.add_twsty_tags(db.f) # some bug about flex being removed if component is hidden 

            cs_shell.text = clabel
            cs_shell.value = clabel
            
        pass

    
VarListDiv = assign_id(_VarListDiv)
