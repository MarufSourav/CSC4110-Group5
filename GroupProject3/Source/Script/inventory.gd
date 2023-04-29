extends Node2D
var panelNode
@onready var inventory_slots = $GridContainer

func onPanelInteraction(panelNodes):
	if(Input.is_action_just_pressed("ADS")):
		if panelNodes.get_children():
			for n in panelNodes.get_children(): 
				panelNodes.remove_child(n) 

func _on_1_gui_input(_event):
	panelNode = get_node("GridContainer/1")
	onPanelInteraction(panelNode)
func _on_2_gui_input(_event):
	panelNode = get_node("GridContainer/2")
	onPanelInteraction(panelNode)
func _on_3_gui_input(_event):
	panelNode = get_node("GridContainer/3")
	onPanelInteraction(panelNode)
func _on_4_gui_input(_event):
	panelNode = get_node("GridContainer/4")
	onPanelInteraction(panelNode)
func _on_5_gui_input(_eventt):
	panelNode = get_node("GridContainer/5")
	onPanelInteraction(panelNode)
func _on_6_gui_input(_event):
	panelNode = get_node("GridContainer/6")
	onPanelInteraction(panelNode)
