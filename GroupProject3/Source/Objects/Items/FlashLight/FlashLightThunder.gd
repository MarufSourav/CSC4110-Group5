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
		bodyOnTrigger = false
		GlobalVar.invArray.append("flashlight")
		GlobalVar.invAmmount += 1
		GlobalVar.haveFlashLight = true
		$DirectionalLight3D.visible = true
		Confirmation.play()
		Thunder.play()
		$Timer.start()


func _on_timer_timeout():
	$DirectionalLight3D.visible = false
	queue_free()
