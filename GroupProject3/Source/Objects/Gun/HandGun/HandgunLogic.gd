extends MeshInstance3D
@export var gunFlash = false
var activated = false

func _process(_delta):
	if gunFlash and !activated:
		$OmniLight3D.light_energy = 10
		activated = true
		$Timer.start()

func _on_timer_timeout():
	$Timer.stop()
	$OmniLight3D.light_energy = 0
	gunFlash = false
	activated = false
