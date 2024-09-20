#. Construct in terms of service provider and consumer
   - Hinav is service provider P
   - The module/entity that calls Hinav is a consumer C

     
#. C defines callbacks for events on childslots
   
   .. code-block::
      async def callback_hinav_terminal_selector(terminal_path, msg):
      async def callback_childslot_mouseenter(terminal_path, msg):
      async def callback_childslot_mouseleave(terminal_path, msg):

#. When user clicks on the childslot, its C's job to invoke the corresponding
   callback
   - invoked with the terminal path as argument 


ChildsPanel
===========

#. Consists of slots
#. constructor takes as input bunch of event handlers
   - attaches that event handler to slots
   
   

#. P creates type(C) from TF_C
   - parametrized by ChildsPanelType

#. C instantiates ChildsPanel
   - passes bunch of event handlers



   
   
