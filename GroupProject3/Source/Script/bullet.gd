extends Node3D
var SPEED = 70
var destinationPosition
@onready var bulletArea = $Area3D

func _ready():
	set_as_top_level(true)
	$Area3D.add_to_group("bullet")
	if GlobalVar.isADS:
		destinationPosition = $destinationPosition.global_position
	else:
		destinationPosition = $destinationPosition.global_position + Vector3(randf_range(-15,15), randf_range(-15,15), randf_range(-15,15))
	$Timer.start()

func _physics_process(delta):
	bulletArea.global_position = bulletArea.global_position.move_toward(destinationPosition, delta * SPEED)

func _timer_timeout():
	queue_free()

func _on_area_3d_body_entered(body):
	if body.name != "Player":
		queue_free()

func _on_area_3d_area_entered(area):
	queue_free()
