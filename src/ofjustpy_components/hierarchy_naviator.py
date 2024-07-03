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


def on_childbtn_click(dbref, msg, target_of, hinav=None):
    """
    when a child  of the head is clicked
    """
    hinav_shell = target_of(hinav)
    # update the breadcrumb with new head and populate the childslots with the current
    # head's child
    hinav_shell.update_ui_on_child_select(dbref.text, msg, target_of)

    pass


def on_arrow_click(dbref, msg, target_of, hinav=None):
    """
    marker on the breadcrumb trail is clicked.
    fold the breadcrumb trail to the marker
    """
    hinav_shell = target_of(hinav)

    hinav_shell.fold(dbref.value, target_of)
    pass


class ValueMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        assert "value" in kwargs
        self.value = kwargs.get("value")
        

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


class HiNav_MutableShellMixin:
    # All the state regarding the hinav will be defined
    # here
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        self.show_path = []
        self.arrrow_pos = 0
        self.show_depth = 1
        session_manager = kwargs.get("session_manager")

        def target_of(item, stubStore=session_manager.stubStore):
            """
            item is a stub or staticCore
            supports item.id which is spath
            for the item
            """
            return dget(stubStore, item.id).target


        # make the root open
        step_shell = dget(
            session_manager.stubStore, self.staticCore.breadcrumb_panel.get_step_at_idx(0).id
        ).target  # target_of(self.staticCore.steps[0])
        step_shell.remove_twsty_tags(noop / hidden)  # root is always open
        self.update_child_panel(target_of)
        pass

    def update_child_panel(self, target_of):
        """
        repopulate the child panel when selected-path gets updated
        """
        self.staticCore.childpanel.hide_all_slots(target_of)
        showitem = dget(self.staticCore.hierarchy, "/" + "/".join(self.show_path))
        self.staticCore.childpanel.update_child_panel(showitem, target_of)
        


    def fold(self, fold_idx, target_of):
        show_depth = self.show_depth

        for i in range(show_depth, fold_idx, -1):
            #stepi = self.staticCore.steps[i - 1]
            stepi = self.staticCore.breadcrumb_panel.get_step_at_idx(i-1)
            stepi_shell = target_of(stepi)
            stepi_shell.add_twsty_tags(noop / hidden)
            self.show_path.pop()
            self.show_depth = self.show_depth - 1
            print("show path after fold = ", self.show_path, " ", self.show_depth)
        self.update_child_panel(target_of)

        pass

    def unfold(self, child_label, target_of):
        # # the unseen arrow
        if self.show_depth == self.staticCore.max_depth:
            print("already at max_depth")
            return

        step_last = self.staticCore.breadcrumb_panel.get_step_at_idx(self.show_depth)
        step_shell = target_of(step_last)
        step_shell.remove_twsty_tags(noop / hidden)
        step_shell.add_twsty_tags(db.f)  # When hiding flex get taken out
        # eop: end-of-path
        self.staticCore.breadcrumb_panel.update_step_text(self.show_depth, child_label, target_of)

        self.show_depth += 1
        self.show_path.append(child_label)
        self.update_child_panel(target_of)

        pass

    def update_ui_on_child_select(self, selected_child_label, msg, target_of):
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            self.unfold(selected_child_label, target_of)
            self.staticCore.callback_child_selected(terminal_path, msg)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            self.staticCore.callback_child_selected(terminal_path, msg)

        pass


HinavBaseType = gen_Div_type(
    HCType.mutable, "Div", TR.DivMixin, mutable_shell_mixins=[HiNav_MutableShellMixin]
)

class ui_breadcrumb_panel(oj.HCCMutable.StackH):

    def __init__(self, num_steps, on_click_eh):
        self.arrows = [
            oj.AC.Button(
                key=f"btn{i}",
                text=">",
                value=i,
                twsty_tags=[bg / pink / 100, boxtopo.bd, bds.none, outlinesty.none, mr / x / 1],
                on_click=on_click_eh
            )
            for i in range(1, num_steps + 1)
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
                bg / pink / 100,
                boxtopo.bd,
                bd / rose / 600,
                bds.solid,
                bd / 2,
                bdr.xl2,
                pd/2
            ],
        )
            for idx in range(num_steps)
        ]

        super().__init__(childs = self.steps)
        pass
    
    def get_step_at_idx(self, idx):
        return self.steps[idx]
    
    def update_step_text(self, idx, label_text, to_ms):
        label = self.labels[idx]
        label_ms = to_ms(label)
        label_ms.text = label_text


class DefaultChildPanel:

    def __init__(self):
        pass
    
def HierarchyNavigator_TF(breadcrumb_panel_type, childpanel_type):
    """
    TF: class factory akin to template parametrization and specialization
    
    breadcrumb_panel_type, childpanel_type: should be class that supports oj.htmlcomponent interface
       - childs
       - classes
       - to_json_dict
       - etc.
    
    """
    class HierarchyNavigator(HinavBaseType):
        def __init__(self,
                     hierarchy,
                     callback_child_selected,
                     max_childs=20,
                     max_depth=6,
                     *args,
                     **kwargs,
                     ):
            """
            callback_child_selected: notify caller when a child/member of a node in the hierarchy is selected
            """
            # TODO: Don't use MButton; use custom button type where both twsty and text is mutable
            self.max_depth = max_depth
            self.hierarchy = hierarchy

            self.callback_child_selected = callback_child_selected
            on_childslot_clicked_event_handler = lambda *args, hinav=self: on_childbtn_click(*args, hinav)
            self.childpanel = childpanel_type(on_childslot_clicked_event_handler,
                                              max_childs=max_childs)
            self.breadcrumb_panel = breadcrumb_panel_type(max_depth,
                                                          lambda *args, hinav=self: on_arrow_click(*args, hinav))

            super().__init__(*args, childs=[], **kwargs)


    HierarchyNavigator = assign_id(HierarchyNavigator)
    return HierarchyNavigator
