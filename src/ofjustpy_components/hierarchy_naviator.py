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
from ofjustpy.TF_impl import HCType
from ofjustpy.ui_styles import sty
from ofjustpy import ui_styles
from ofjustpy.Div_TF import gen_Div_type

# require for arrow button which is special type of mutable
# the text is mutable; but the twsty-tags remains the same

from ofjustpy.HC_TF import gen_HC_type


def on_childbtn_click(dbref, msg, target_of, hinav=None):
    hinav_shell = target_of(hinav)
    hinav_shell.update_ui_on_child_select(dbref.text, target_of)

    pass


def on_arrow_click(dbref, msg, target_of, hinav=None):
    hinav_shell = target_of(hinav)

    # hinav_shell.arrow_pos = dbref.value
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
        mutableShellMixins=[TR.TwStyMixin, TR.HCTextMixin, ValueMixin],
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

        # self.childpanel_shell = dget(session_manager.stubStore, self.staticCore.childpanel.id)
        # self.childpanel_shell = target_of(self.staticCore.childpanel)
        # self.hinav_path_shell = target_of(self.staticCore.hinav_path_shell)

        # make the root open
        step_shell = dget(
            session_manager.stubStore, self.staticCore.steps[0].id
        ).target  # target_of(self.staticCore.steps[0])
        step_shell.remove_twsty_tags(noop / hidden)  # root is always open
        self.update_child_panel(target_of)
        pass

    def update_child_panel(self, target_of):
        """
        repopulate the child panel when selected-path gets updated
        """
        for cs in self.staticCore.childpanel.childs:
            shell = target_of(cs)
            shell.add_twsty_tags(noop / hidden)

        showitem = dget(self.staticCore.hierarchy, "/" + "/".join(self.show_path))

        print ("show_path = ", self.show_path)
        print ("showitem = ", showitem.keys())
        
        for cs, clabel in zip(
            self.staticCore.childpanel.childs,
            filter(lambda x: x != "_cref", showitem.keys()),
        ):
            cs_shell = target_of(cs)
            cs_shell.remove_twsty_tags(noop / hidden)
            cs_shell.add_twsty_tags(db.f)

            cs_shell.text = clabel
            cs_shell.value = clabel
            
        pass

    def fold(self, fold_idx, target_of):
        show_depth = self.show_depth

        for i in range(show_depth, fold_idx, -1):
            stepi = self.staticCore.steps[i - 1]
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

        step_last = self.staticCore.steps[self.show_depth]
        step_shell = target_of(step_last)
        step_shell.remove_twsty_tags(noop / hidden)
        step_shell.add_twsty_tags(db.f)  # When hiding flex get taken out
        # eop: end-of-path
        eop_shell = target_of(self.staticCore.labels[self.show_depth])
        eop_shell.text = child_label
        self.show_depth += 1
        self.show_path.append(child_label)
        self.update_child_panel(target_of)

        pass

    def update_ui_on_child_select(self, selected_child_label, target_of):
        dval = dget(
            self.staticCore.hierarchy,
            "/" + "/".join([*self.show_path, selected_child_label]),
        )
        if isinstance(dval, dict):
            terminal_path = f"""{"/" +"/".join([*self.show_path, selected_child_label]) + "/_cref"}"""
            self.unfold(selected_child_label, target_of)
            self.staticCore.callback_child_selected(terminal_path)
        else:
            terminal_path = (
                f"""{"/" +"/".join([*self.show_path, selected_child_label])}"""
            )
            self.staticCore.callback_child_selected(terminal_path)

        pass


HinavBaseType = gen_Div_type(
    HCType.mutable, "Div", TR.DivMixin, mutable_shell_mixins=[HiNav_MutableShellMixin]
)


class HierarchyNavigator(HinavBaseType):
    def __init__(
        self,
        hierarchy,
        callback_child_selected,
        max_childs=20,
        max_depth=6,
        *args,
        **kwargs,
    ):
        # TODO: Don't use MButton; use custom button type where both twsty and text is mutable
        self.max_child = max_childs
        self.max_depth = max_depth
        self.hierarchy = hierarchy

        self.callback_child_selected = callback_child_selected
        self.childslots = [
            ChildSlotBtn_HCType(
                key=f"cbtn{i}",
                text=str(i),
                value=i,
                twsty_tags=[
                    pd / 0,
                    mr / y / 0,
                    noop / hidden,
                    bd / blue / 1,
                    bt.bd,
                    bd / blue / 4,
                    bd / 2,
                    bdr.xl,
                ],
                on_click=lambda *args, hinav=self: on_childbtn_click(*args, hinav),
            )
            for i in range(max_childs)
        ]

        self.childpanel = oj.HCCMutable.StackV(  # key="childpanel",
            childs=self.childslots, twsty_tags=[max / W / "md", space / y / 1]
        )

        # arrows:
        self.arrows = [
            oj.AC.Button(
                key=f"btn{i}",
                text=">",
                value=i,
                twsty_tags=[bg / pink / 1, bt.bd, bds.none, outline.none, mr / x / 1],
                on_click=lambda *args, hinav=self: on_arrow_click(*args, hinav),
            )
            for i in range(1, max_depth + 1)
        ]

        self.labels = [
            ArrowSpan_HCType(key=f"label{i}", text="", twsty_tags=[mr / x / 0])
            for i in range(max_depth)
        ]

        self.steps = [
            oj.Mutable.StackH(
                key=f"item{i}",
                childs=[self.labels[i], self.arrows[i]],
                twsty_tags=[
                    mr / x / 0,
                    noop / hidden,
                    bg / pink / 1,
                    bt.bd,
                    bd / rose / 6,
                    bds.solid,
                    bd / 2,
                    bdr.xl2,
                ],
            )
            for i in range(max_depth)
        ]

        super().__init__(*args, childs=[], **kwargs)


HierarchyNavigator = assign_id(HierarchyNavigator)
