from ofjustpy_components import VarLenghtList_TF

VarLenghtList = assign_id(VarLenghtList_TF())

def on_slot_clicked(dbref, msg, to_ms):
    pass
varlenghtlist = VarLenghtList("varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )

