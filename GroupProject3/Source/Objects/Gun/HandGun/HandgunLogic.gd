extends MeshInstance3D 
@export var fired = false
@export var ammo = 5
@export var readyToFire = true
func _process(_delta):
	if fired and readyToFire:
		fired = false
		readyToFire = false
		$"/root/GunSoundEffect".play()
		$OmniLight3D.light_energy = 4
		$muzzleFlash.start()
		$ROF.start()

func _on_muzzle_flash_timeout():
	$muzzleFlash.stop()
	$OmniLight3D.light_energy = 0

func _on_rof_timeout():
	readyToFire = true
	$ROF.stop()

