HiNav
-----


#. ChildSlotsPanel should inherit/implement ChildsPanelMixinBase
   - It should be of HCCMutable or Mutable type
   - implements get_childslots
     - which returns slots 
       - they support mutable  text and value
	 - i.e. they support expression
	   .. code-block::
	      # cs  is a slot
	      cs_shell = target_of(cs)
	      cs_shell.text = clabel
	      cs_shell.value = clabel


#. childslots_panel_gen
   - is a function that takes a dict of event handlers
     - and returns a ChildSlotsPanel
       - the event handlers have to be attached to all the childslots
	 
	       

#. breadcrumb_panel_gen
   - input: arrow_eh
   - returns a BreadCrumbPanel
     - that implements BreadcrumbPanelMixinBase
   - arrow_eh is to be attached to all steps/crumbs of the breadcrumb
     
