extends MeshInstance3D
var bodyOnTrigger
@export var ammo_ammount = 0
var changedAmmoAmmount = false
# Called when the node enters the scene tree for the first time.
func _ready():
	set_as_top_level(true)
func _on_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true

func _on_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if(bodyOnTrigger and Input.is_action_just_pressed("interact")):
		for i in GlobalVar.invArray:
			if i[0] == "ammo" and i[1] < 4:
				changedAmmoAmmount = true
				if i[1] + ammo_ammount <= 4:
					i[1] += ammo_ammount
					ammo_ammount = 0
				else:
					var ammoRequest = 4 - i[1]
					i[1] = 4
					ammo_ammount -= ammoRequest
					

		
		
		if ammo_ammount == 0:
			Confirmation.play()
			queue_free()
		else:
			if GlobalVar.invAmmount < 6:
				Confirmation.play()
				if ammo_ammount <= 4:
					GlobalVar.invArray.append(["ammo", ammo_ammount])
					GlobalVar.invAmmount += 1
					queue_free()
				else:
					GlobalVar.invArray.append(["ammo", 4])
					GlobalVar.invAmmount += 1
					ammo_ammount -= 4
			else:
				if changedAmmoAmmount:
					Confirmation.play()
					changedAmmoAmmount = false
				else:
					Declined.play()
