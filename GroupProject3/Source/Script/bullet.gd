extends Node3D
var SPEED = 200
@onready var destinationPosition = $destinationPosition.global_position
@onready var bulletMesh = $MeshInstance3D

func _on_area_body_entered(body):
	if body != CharacterBody3D:
		queue_free()

func _ready():
	set_as_top_level(true)
	$Timer.start()

func _on_timer_timeout():
	queue_free()

func _physics_process(delta):
	bulletMesh.global_position = bulletMesh.global_position.move_toward(destinationPosition, delta * SPEED)
