extends CharacterBody3D
@export var health = 4
var SPEED = 4.5
@export var enabled = true
@onready var nav_agent = $NavigationAgent3D
func _physics_process(delta):
	var current_location = global_position
	var next_location = nav_agent.get_next_path_position()
	#print(current_location , " ", next_location)
	var new_velocity = (next_location - current_location).normalized() * SPEED
	
	velocity = new_velocity
	if enabled:
		move_and_slide()

func update_target_location(target_location) -> void:
	nav_agent.target_position = target_location
	look_at(target_location)

func _process(delta):
	if health <= 0:
		queue_free()

func _on_area_3d_area_entered(area):
	if area.is_in_group("bullet"):
		health -= 1
		Hit.play()


func _on_navigation_agent_3d_target_reached():
	GlobalVar.freezePlayer = false
	GlobalVar.canOpenInventory = true
	GlobalVar.haveFlashLight = false
	GlobalVar.haveGun = false
	GlobalVar.invAmmount = 0
	GlobalVar.invArray = []
	get_tree().change_scene_to_file("res://Scene/DeathScene.tscn")
