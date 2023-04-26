extends MeshInstance3D
@export var keyID = ""
var bodyOnTrigger
# Called when the node enters the scene tree for the first time.

func _on_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true


func _on_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if(bodyOnTrigger and Input.is_action_just_pressed("interact")):
		GlobalVar.keyID = keyID
		Confirmation.play()
		queue_free()
