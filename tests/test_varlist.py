import pytest
from addict import Dict
from starlette.testclient import TestClient
import kavya as kv
from py_tailwind_utils import W, H, dget
from kavya_components import VarLenghtList_TF
from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
# --- Setup Global State (as per your snippet) ---
items = []
varlenghtlist_id = "/varlenghtlist"

async def on_slot_clicked(dbref, msg, wp, request):
    pass
async def on_del_item(dbref, msg, wp, request):
    global items
    to_ms = wp.session_manager.target_of
    #items.append(str(len(items)))
    items.pop()
    ms = to_ms(varlenghtlist_id)
    ms.hide_all_slots()
    ms.update_child_panel(items, items)
    pass

async def on_add_item(dbref, msg, wp, request):
    global items
    items.append(str(len(items)))
    to_ms = wp.session_manager.target_of
    ms = to_ms(varlenghtlist_id)
    ms.hide_all_slots()
    ms.update_child_panel(items, items)
    pass

# Assuming these are available in your environment:
# VarLenghtList = assign_id(VarLenghtList_TF())
# For the purpose of the test, we assume they are imported/defined.

# build the app only once
kv.build_app()


@pytest.fixture
def fixture_starlette_kavya_app():
    return kv.load_app()


@pytest.fixture
def fixture_starlette_testclient(fixture_starlette_kavya_app):
    return  TestClient(fixture_starlette_kavya_app)
    
def tracking_post_init(*args, session_manager=None, **kwargs):
    """Real function to track execution without mocks"""
    session_manager.appstate.post_init_run = True


def post_init_callback(*args, session_manager=None, **kwargs):
    print(" post_init_callback = ", varlenghtlist_id)
    print("ttt = ",
          dget(session_manager.stubStore, varlenghtlist_id)
          )
    # session_manager.stubStore.
    pass

@pytest.fixture
def fixture_varlist_endpoint():
    """
    Fixture that defines the Page Endpoint configuration.
    """
    add_item_btn =  kv.AD.Button(key="add_item_btn",
                             text="add new item",
                             on_click = on_add_item,
                             twsty_tags = [H/16, W/32]
                             )



    del_item_btn =  kv.AD.Button(key="del_item_btn",
                             text="del item",
                             on_click = on_del_item,
                             twsty_tags = [H/16, W/32]
                             )
    VarLenghtList = assign_id(VarLenghtList_TF())
    varlenghtlist = VarLenghtList(key="varlenghtlist",
                              max_slots = 20,
                              on_slot_clicked = on_slot_clicked
                              )


 

    wp_endpoint = kv.create_endpoint(key="varlistdiv",
                                    childs = [kv.HM.StackH(childs = [varlenghtlist,
                                                                     kv.PD.StackV(childs = [add_item_btn, del_item_btn]
                                                                                          )

                                                                                          ],
                                                                   twsty_tags= [W/96]
                                                                   )
                                              ],
                                    title="VarLenghtList",
                                    post_init_callback = post_init_callback,
                                    svelte_bundle_dir = "ssr",
                                    rendering_type="MutableSSR",
                                    )

    return wp_endpoint
  

@pytest.fixture
def fixture_setup_app(fixture_starlette_kavya_app, fixture_varlist_endpoint):
    """
    Fixture that attaches the endpoint to the app and returns the app.
    """
    app = fixture_starlette_kavya_app
    #app.state.post_init_run = False # Reset state
    kv.add_route("/test-page", fixture_varlist_endpoint)
    return app




@pytest.mark.asyncio
async def test_varlengthlist_add_delete_flow(fixture_setup_app):
    """
    Verifies that clicking 'Add' increases list size and clicking 'Delete' 
    decreases it, triggering the component's update methods.
    """
    global items
    items = []  # Reset global state for the test
    app = fixture_setup_app

    # 1. Component Definitions



    # 2. Trigger initial request to setup the iobjs
    with TestClient(app) as client:
        response = client.get("/test-page")
        
        assert response.status_code == 200
        
        # Verify the side-effect defined in tracking_post_init
        pageId_pageComp_map = kv.starlette_app.app_state.pageId_pageComp_map
        # iobj: instance object
        target_wp_iobj = next(iter(pageId_pageComp_map.values()))
        to_ms = target_wp_iobj.session_manager.target_of
        # Resolve components from the live webpage iobj
        # Since they are nested in StackH and StackV, we find by key
        stubStore = target_wp_iobj.session_manager.stubStore
        live_add_btn = dget(stubStore, "/add_item_btn").target
        live_del_btn = dget(stubStore, "/del_item_btn").target
        live_v_list = dget(stubStore, "/varlenghtlist").target
        
        request = target_wp_iobj.session_manager.request

        # --- SCENARIO 1: ADD ITEM ---
        add_click_eh = live_add_btn.get_event_handler('click')
        
        # First Add
        await add_click_eh(live_add_btn, Dict(), target_wp_iobj, request)
        assert len(items) == 1
        assert items[0] == "0"

        # check the slots
        assert len(items) == 1
      
        first_slot =  to_ms(live_v_list.staticCore.slots[0].id)
        
        # Verify Visibility and Text
        assert first_slot.text == "0", f"Expected slot text '0', got {first_slot.text}"
     
        # Second Add
        await add_click_eh(live_add_btn, Dict(), target_wp_iobj, request)
        assert len(items) == 2
        second_slot =  to_ms(live_v_list.staticCore.slots[1].id)
        assert 'hidden' not in second_slot.classes 
        assert second_slot.text == "1", "Second slot text should match items[1]"
        
        
        # Verify that the 'ms' (MutableShell) logic worked. 
        # Typically, update_child_panel modifies the slots inside the v_list.
        # We check if the list of visible slots or child data matches our 'items'.
        # (Replace '.slots' with the actual attribute your VarLenghtList uses)
        # assert len(live_v_list.active_slots) == 2 

        # --- SCENARIO 2: DELETE ITEM ---
        del_click_eh = live_del_btn.get_event_handler('click')
        
        await del_click_eh(live_del_btn, Dict(), target_wp_iobj, request)
        
        # Assertions
        assert len(items) == 1
        assert items == ["0"]
        assert "hidden" in second_slot.classes
        
        
        # Verify state reset
        await del_click_eh(live_del_btn, Dict(), target_wp_iobj, request)
        assert len(items) == 0
        assert "hidden" in first_slot.classes
        print("VarLenghtList add/del sequence verified successfully.")
