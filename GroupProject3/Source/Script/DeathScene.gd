extends Node2D
func _process(delta):
	if Input.is_action_just_pressed("restart"):
		get_tree().change_scene_to_file("res://Scene/World.tscn")
	if Input.is_action_just_pressed("ui_cancel"):
		get_tree().quit()
