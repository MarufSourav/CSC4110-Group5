extends Node3D
var moveSound = false

func _on_event_1_body_entered(body):
	if body is CharacterBody3D:
		$EventTrigger/Event1.position = Vector3(0, -5, 0)
		body.walkSoundLoader = "res://Sound/indoor-foosteps-walk.wav"
		body.runSoundLoader = "res://Sound/indoor-foosteps-run.wav"
		$Door10.isOpen = false
		$Door10.doorLocked = true
		$Door10.doorID = "inf"
		$Door7.isOpen = false
		$Door10/DialogTrigger3.position = Vector3(0.34, 0.59, 1.36)
		moveSound = true
		$NodeFreeTimer.start()
		$giggling.play()
		

func _process(delta):
	if moveSound:
		$giggling.position = lerp($giggling.position, Vector3(0.6, 2.3, -1.2), 4 * delta)
		
func _on_node_free_timer_timeout():
	$NodeFreeTimer.stop()
	moveSound = false
	$giggling.queue_free()
	$EventTrigger/Event1.queue_free()
