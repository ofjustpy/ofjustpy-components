import ofjustpy as oj
from ofjustpy.htmlcomponents_impl import assign_id
from py_tailwind_utils import * 
from ofjustpy_components import VarLenghtList_TF
from ofjustpy_components.variable_length_list_TF import SlotBtn_DivType

class SlotBtnWithIcon(SlotBtn_DivType):
    def __init__(self, **kwargs):
        print ("HHHHHHHHHHHHHH")
        super().__init__(childs=[oj.PC.Span(key="X", text="HHHH")],
                         **kwargs
                         )
        
        pass
    
    pass

SlotBtnWithIcon_idgen = assign_id(SlotBtnWithIcon)
app = oj.load_app()
#VarLenghtList = VarLenghtList_TF(SlotType = SlotBtnWithIcon_idgen)
VarLenghtList = assign_id(VarLenghtList_TF())


def on_slot_clicked(dbref, msg, to_ms):
    pass
varlenghtlist = VarLenghtList(key="varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )

items =  []

async def on_add_item(dbref, msg, to_ms):
    global items
    items.append(str(len(items)))
    ms = to_ms(varlenghtlist)
    print(ms)
    ms.hide_all_slots()
    ms.update_child_panel(items)
    pass

add_item_btn =  oj.AD.Button(key="add_item_btn",
                             text="add new item",
                             on_click = on_add_item,
                             twsty_tags = [H/16, W/32]
                             )

async def on_del_item(dbref, msg, to_ms):
    global items
    
    #items.append(str(len(items)))
    items.pop()
    print (items)
    ms = to_ms(varlenghtlist)
    
    print(ms)
    ms.hide_all_slots()
    ms.update_child_panel(items)
    pass

del_item_btn =  oj.AD.Button(key="del_item_btn",
                             text="del item",
                             on_click = on_del_item,
                             twsty_tags = [H/16, W/32]
                             )
             
wp_endpoint = oj.create_endpoint(key="varlistdiv",
                                    childs = [oj.HCCMutable.StackH(childs = [varlenghtlist,
                                                                             oj.PC.StackV(childs = [add_item_btn, del_item_btn]
                                                                                          )

                                                                                          ],
                                                                   twsty_tags= [W/96]
                                                                   )
                                              ],
                                    title="VarLenghtList"
                                    )

oj.add_jproute("/", wp_endpoint)

