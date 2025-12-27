from kavya_components import StackD
import kavya as kv

from py_tailwind_utils import *
app = kv.load_app()


with kv.uictx("deckdemo") as  deckdemo:
    
    btn1 = kv.MC.Button(key="mybtn1",
                        value="/mybtn2",
                        text="Click me1 ",
                        twsty_tags=[bg/primary/500],
                        #on_click = on_btn_click
                        )

    btn2 = kv.MC.Button(key="mybtn2",
                              value="/mybtn1",
                              text="Click me2 ",
                              twsty_tags=[bg/success/300],
                              #on_click = on_btn_click
                              )
            
    thedeck = StackD(key = "thedeck",
                     childs = [ btn1, btn2
                               ]
                     )


    async def on_btn_click(dbref, msg, wp, request):
        target_of = wp.session_manager.target_of
        print ("on_btn_click")
        
        target = dget(deckdemo, dbref.value)
        print (target)
        ms_thedeck = target_of(thedeck.id)
        print (ms_thedeck)
        ms_thedeck.bring_to_front(target.id)
        pass

    btn1.on("click", on_btn_click)
    btn2.on("click", on_btn_click)
    btn1.prepare_htmlRender()
    btn2.prepare_htmlRender()
    
wp_endpoint = kv.create_endpoint(key="example_008",
                                 childs = [thedeck],
                                 title="example_008",
                                 skeleton_data_theme = "seafoam",
                                 rendering_type="MutableSSR",
                                 ssr_bundle_dir = "ssr"
                                 )

kv.add_route("/", wp_endpoint)

