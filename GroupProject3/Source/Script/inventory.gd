extends Node2D
var panelNode
var updatedInventory = false
@onready var inventory_slots = $GridContainer
@onready var flashlight = preload("res://Texture/ItemSprite/flashlightSprite.tscn")
@onready var gun = preload("res://Texture/ItemSprite/gunSprite.tscn")
@onready var ammo = preload("res://Texture/ItemSprite/ammoSprite.tscn")
@onready var key = preload("res://Texture/ItemSprite/keySprite.tscn")
var itemInstantiate
func updateInventory():
	print("Updated")
func onPanelInteraction(location):
	if(Input.is_action_just_pressed("FIRE")):
		print(location + 1)
		#GlobalVar.invArray.erase(GlobalVar.invArray[location])
		updatedInventory = false

func _process(_delta):
	if Input.get_mouse_mode() == Input.MOUSE_MODE_VISIBLE and !updatedInventory:
		updatedInventory = true
		updateInventory()
	if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		updatedInventory = false
















func _on_1_gui_input(_event):
	onPanelInteraction(0)
func _on_2_gui_input(_event):
	onPanelInteraction(1)
func _on_3_gui_input(_event):
	onPanelInteraction(2)
func _on_4_gui_input(_event):
	onPanelInteraction(3)
func _on_5_gui_input(_eventt):
	onPanelInteraction(4)
func _on_6_gui_input(_event):
	onPanelInteraction(5)
