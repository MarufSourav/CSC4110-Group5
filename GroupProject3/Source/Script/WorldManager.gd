extends Node3D
var moveSound = false
@onready var enemy = preload("res://Objects/Zombie/enemy.tscn")
var enemyInstantiate
func _on_event_1_body_entered(body):
	if body is CharacterBody3D:
		$EventTrigger/Event1.position = Vector3(0, -5, 0)
		body.walkSoundLoader = "res://Sound/indoor-foosteps-walk.wav"
		body.runSoundLoader = "res://Sound/indoor-foosteps-run.wav"
		$Door1.isOpen = false
		$Door9.isOpen = false
		$Door1.doorLocked = true
		$Door1.doorID = "inf"
		$Door1/DialogTrigger3.position = Vector3(0.34, 0.59, 1.36)
		moveSound = true
		$NodeFreeTimer.start()
		$giggling.play()
		$churchbell.play()
		$Enemy.queue_free()

func _process(delta):
	if moveSound:
		$giggling.position = lerp($giggling.position, Vector3(0.6, 2.3, -1.2), 4 * delta)
func _physics_process(delta):
	get_tree().call_group("Enemy", "update_target_location", $Player.global_position)

func _on_node_free_timer_timeout():
	$NodeFreeTimer.stop()
	moveSound = false
	$giggling.queue_free()
	$churchbell.queue_free()
	$EventTrigger/Event1.queue_free()


func _on_event_2_body_entered(body):
	if body is CharacterBody3D:
		LurkingSound.play()
		$EventTrigger/Event2.queue_free()


func _on_event_3_body_entered(body):
	if body is CharacterBody3D:
		enemyInstantiate = enemy.instantiate()
		enemyInstantiate.global_position = Vector3(20.5, 8.5, 21)
		add_child(enemyInstantiate)
		enemyInstantiate = enemy.instantiate()
		enemyInstantiate.global_position = Vector3(-20.5, 8.5, 21)
		add_child(enemyInstantiate)
		$EventTrigger/Event3.queue_free()


func _on_event_4_body_entered(body):
	if body is CharacterBody3D:
		enemyInstantiate = enemy.instantiate()
		enemyInstantiate.global_position = Vector3(-20.5, 0.5, 15)
		add_child(enemyInstantiate)
		enemyInstantiate = enemy.instantiate()
		enemyInstantiate.global_position = Vector3(-20.5, 0.5, 5)
		add_child(enemyInstantiate)
		$EventTrigger/Event4.queue_free()
