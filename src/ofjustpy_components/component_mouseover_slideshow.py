import ofjustpy as oj
from ofjustpy.ui_styles import sty
from py_tailwind_utils import *
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType

from ofjustpy.HC_wrappers import StackH_Aligned

from ofjustpy.htmlcomponents_impl import assign_id


# all mutable variable declarations goes here
class SlideShow_MutableShellMixin:
    attr_tracked_keys = []
    domDict_tracked_keys = []
    def __init__(self, *args, **kwargs):
        pass


SlideShowBase = gen_Div_type(
    HCType.mutable,
    "Div",
    TR.DivMixin,
    mutable_shell_mixins=[SlideShow_MutableShellMixin],
)


def on_mouseover_action(dbref, msg, target_of, slideshow=None):
    # a button has been clicked
    # get the spath/id and the value of the button

    deck_shell = target_of(slideshow.slide_deck)
    slide = slideshow.slides[dbref.value]
    deck_shell.bring_to_front(slide.id)

    pass


class SlideShow(SlideShowBase):
    def __init__(
        self, key, slide_labels, slide_info, height_anchor_label, *args, **kwargs
    ):
        """
        The height_anchor_label controls the height of the resulting slideshow panel.
        We need to give grid panel height since
        """

        doorcards = []
        self.slides = {}

        for sl in slide_labels:
            # create the panel for slide_info
            # The slide needs to be css-mutable
            # as it will hidden/unhidden via deck
            slide = oj.HCCStatic.StackV(
                key=f"slide_{sl}",
                childs=[
                    oj.PC.SubheadingBanner(slide_info[sl][0]),
                    oj.PC.Halign(
                        slide_info[sl][1],
                        align="start",
                        twsty_tags=[pd / x / 4],
                    ),
                ],
            )

            # create the corresponding doorcard
            doorcard = oj.AC.Button(
                key=f"{sl}_doorcard",
                twsty_tags=[
                    fc / rose / 300,
                    ta.center,
                    bdr.lg,
                    bd / gray / 300,
                    boxtopo.bd,
                    fw.medium,
                    *build_gradient_expr(gray / 200, gray / 200, gray / 100),
                    shadow / gray / 200,
                    shadow.md,
                ],
                text=slide_info[sl][0],
                value=sl,
                on_click=lambda *args, slideshow=self: on_mouseover_action(
                    *args, slideshow=slideshow
                ),
            )
            doorcards.append(doorcard)
            self.slides[sl] = slide

        doorcards_panel = oj.PC.StackG(
            num_cols=1,
            num_rows=2,
            childs=doorcards,
            twsty_tags=[
                W / "1/2",
                *variant(G / cols / 1, rv="sm"),
                *variant(G / cols / 2, rv="md"),
                *variant(G / cols / 3, rv="lg"),
            ],
        )

        self.slide_deck = oj.Mutable.StackD(
            key=f"deck_{key}",
            childs=self.slides.values(),
            twsty_tags=[W / "1/2"],
            height_anchor_key=f"slide_{height_anchor_label}",
        )

        # flx.one because we want both left and right div to expand and occupy
        # equal space
        twsty_tags = conc_twtags(*sty.stackh, *kwargs.pop("twsty_tags", []), flx.one)

        # super().__init__(*args, key=key,
        #                  childs=[StackH_Aligned(doorcards_panel, content_type="mutable"),
        #                          StackH_Aligned(self.slide_deck, content_type="mutable")
        #                          ],
        #                  twsty_tags=twsty_tags,
        #                  **kwargs
        #                  )

        super().__init__(
            *args,
            key=key,
            childs=[doorcards_panel, self.slide_deck],
            twsty_tags=twsty_tags,
            **kwargs,
        )

        # super().__init__(*args, childs=[aligned_doorcards_panel,
        #                                 aligned_slide_deck
        #                                 ],
        #                  twsty_tags=twsty_tags,
        #                  **kwargs
        #                  )

        pass


SlideShow = assign_id(SlideShow)
