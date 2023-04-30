extends MeshInstance3D
var bodyOnTrigger = false
func _ready():
	set_as_top_level(true)
func _on_area_3d_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true

func _on_area_3d_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if Input.is_action_just_pressed("interact") and bodyOnTrigger:
		if GlobalVar.invAmmount == 6:
			Declined.play()
		else:
			GlobalVar.invArray.append("flashlight")
			GlobalVar.invAmmount += 1
			GlobalVar.haveFlashLight = true
			queue_free()
			Confirmation.play()

