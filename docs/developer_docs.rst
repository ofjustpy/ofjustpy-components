Design and Architecture
^^^^^^^^^^^^^^^^^^^^^^^^

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



