"""
bulk edit: utils to change tailwind sty of many components using single command
relies on stubStore hierarchical organization of ui-components
utils to bulk edit
"""


def hinav_edit(
    hinav_ctx_spath,
    child_btn_tags=[],
    arrow_btn_tags=[],
    arrow_label_tags=[],
):
    """
    - the path (within stubStore) of the ui context within which hinav resides
    - Assumption/restriction: there is only one hinav within a context
    -
    """

    def bulk_update_twtags(twtags, stub_iter):
        for stub in stub_iter:
            stub.target.add_twsty_tags(*twtags)

    # update the twtags for all the child labels
    if child_btn_tags:
        child_btns = (
            stub
            for key, stub in hinav_ctx_spath.___hinav.___child.items()
            if key.startswith("cbtn")
        )
        bulk_update_twtags(child_btn_tags, child_btns)

    if arrow_btn_tags:
        arrow_btns = (
            stub
            for key, stub in hinav_ctx_spath.___hinav.___arrows.items()
            if key.startswith("btn")
        )

        bulk_update_twtags(arrow_btn_tags, arrow_btns)

    if arrow_label_tags:
        arrow_labels = (
            stub
            for key, stub in hinav_ctx_spath.___hinav.___arrows.items()
            if key.startswith("label")
        )
        bulk_update_twtags(arrow_label_tags, arrow_labels)

    pass
