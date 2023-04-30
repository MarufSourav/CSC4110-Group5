extends MeshInstance3D
var bodyOnTrigger
@export var ammo_on_gun = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	set_as_top_level(true)
func _on_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true
		body.handGun.ammo = ammo_on_gun

func _on_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if(bodyOnTrigger and Input.is_action_just_pressed("interact")):
		if GlobalVar.invAmmount == 6:
			Declined.play()
		else:
			GlobalVar.invArray.append(["pistol", ammo_on_gun])
			GlobalVar.invAmmount += 1
			GlobalVar.haveGun = true
			queue_free()
			Confirmation.play()
