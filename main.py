import dearpygui.dearpygui as dpg
dpg.create_context()
"""
def link_nodes(s, data):
    dpg.add_node_link(parent=s, attr_1=data[0], attr_2=data[1])

def delink_nodes(_, data):
    dpg.delete_item(data)

def add_node_value():
    with dpg.node(parent="nde", label="terraform data"):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_input_int(width=100)
    dpg.hide_item("popup_window")

def add_node_add():
    with dpg.node(parent="nde", label="Add"):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input):
            dpg.add_input_int(width=100)
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input):
            dpg.add_input_int(width=100)
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
            dpg.add_text()
    dpg.hide_item("popup_window")
    
def add_node_print():
    with dpg.node(parent="nde", label="Print"):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Input):
            dpg.add_button(label="Get Value")
    dpg.hide_item("popup_window")

with dpg.window(tag="popup_window", no_move=True, no_close=True, no_resize=True, no_collapse=True, label="Select Item"):
    with dpg.menu(label="Terraform"):
        dpg.add_menu_item(label="init", callback=add_node_value)
        dpg.add_menu_item(label="plan", callback=add_node_value)
        dpg.add_menu_item(label="apply", callback=add_node_value)
        dpg.add_menu_item(label="destroy", callback=add_node_value)

    with dpg.menu(label="Math"):
        dpg.add_menu_item(label="Add", callback=add_node_add)
    with dpg.menu(label="Output"):
        dpg.add_menu_item(label="Print", callback=add_node_print)

def change_text(sender, app_data):
	if dpg.is_item_hovered("nde"):
	    dpg.focus_item("popup_window")
	    dpg.show_item("popup_window")
	    dpg.set_item_pos("popup_window", dpg.get_mouse_pos(local=False))
	else:
		pass
with dpg.handler_registry():
	dpg.add_mouse_click_handler(button=1,callback=change_text)
	
with dpg.window(width=500, height=300):
	with dpg.node_editor(callback=link_nodes, delink_callback=delink_nodes,width=600,height=600,tag="nde") as nde:
		pass
"""
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()