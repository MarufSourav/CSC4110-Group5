extends Node3D
@export var x = 0.00
@export var y = 0.00
@export var z = 0.00
@export var xR = 0
@export var yR = 0
@export var zR = 0
func _on_area_body_entered(body):
	if body is CharacterBody3D:
		body.global_position = Vector3(x, y, z)
		body.rotation_degrees.x = xR
		body.rotation_degrees.y = yR
		body.rotation_degrees.z = zR
