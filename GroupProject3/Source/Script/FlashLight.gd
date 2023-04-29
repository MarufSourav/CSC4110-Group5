extends MeshInstance3D
var bodyOnTrigger = false

func _on_area_3d_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true

func _on_area_3d_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if Input.is_action_just_pressed("interact") and bodyOnTrigger:
		GlobalVar.haveFlashLight = true
		Confirmation.play()
		queue_free()

