Design and Architecture
^^^^^^^^^^^^^^^^^^^^^^^^
#. Top Level class: HierarchyNavigator
   - Is derived from : HinavBaseType
     - is a mutable div type with  mixin
       - HiNav_MutableShellMixin

#. HiNav_MutableShellMixin
   - most of core hinav disply logic is here
   - provides
     - update_child_panel
     - fold
     - unfold
     - update_ui_on_child_select


#. ui_breadcrumb_panel
   - a class to hold the bredcrumb trail
   - has
     - arrows : as AC.Button # make this configurable
     - labels : ArrowSpan_HCType # make this configurable
     - steps : A pair of arrow and label clubbed together by Mutable.StackH

   - provides
     - get_step_at_idx
     - update_step_text
       
       
#. HierarchyNavigator:
   - __init__
     - create child slots #. make visuals configurable
     - 



HierarchyNavigator
+++++++++++++++++++
- The chain-reaction that invokes the callback:

  callback_child_selected is-called-by
  update_ui_on_child_select is-called-by
  on_childbtn_click which is linked to the childslots.
  
  

- Used expressions involving childbtn, childslots, arrows, etc.

.. code-block:: python

   for cs in self.staticCore.childpanel.childs:
      shell = target_of(cs)
      shell.add_twsty_tags(noop / hidden)

  

Code layout
^^^^^^^^^^^^

Tests
+++++

- tests/test_create_webpage_instance.py
Test level 1: creation of webpage instances containing components



