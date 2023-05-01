extends Node3D
var moveSound = false
@onready var enemy = preload("res://Objects/Zombie/enemy.tscn")
var enemyInstantiate

func addEnemy(position):
	enemyInstantiate = enemy.instantiate()
	enemyInstantiate.global_position = position
	add_child(enemyInstantiate)

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
		addEnemy(Vector3(20.5, 8.5, 21))
		addEnemy(Vector3(-20.5, 8.5, 21))
		$EventTrigger/Event3.queue_free()

func _on_event_4_body_entered(body):
	if body is CharacterBody3D:
		addEnemy(Vector3(-13.8, 0.5, 4.1))
		addEnemy(Vector3(-13.8, 0.5, 15))
		$EventTrigger/Event4.queue_free()
func _on_event_5_body_entered(body):
	if body is CharacterBody3D:
		addEnemy(Vector3(0.5, 0.5, 12))
		$EventTrigger/Event5.queue_free()
func _on_event_6_body_entered(body):
	if body is CharacterBody3D:
		addEnemy(Vector3(-27, 0.5, -20.5))
		$EventTrigger/Event6.queue_free()
func _on_event_7_body_entered(body):
	if body is CharacterBody3D:
		addEnemy(Vector3(-4, 0.5, -6.5))
		addEnemy(Vector3(4, 0.5, -6.5))
		$EventTrigger/Event7.queue_free()
func _on_event_final_body_entered(body):
	if body is CharacterBody3D:
		$Door1.doorLocked = false
		$Door1.isOpen = true
		$Door1/DialogTrigger3.queue_free()
		addEnemy(Vector3(0, 0.5, -10))
		addEnemy(Vector3(27, 0.5, -21))
		addEnemy(Vector3(23, 0.5, -21))
		$EventTrigger/EventFinal.queue_free()


func _on_win_ready_body_entered(body):
	if GlobalVar.winReady and (body is CharacterBody3D):
		GlobalVar.freezePlayer = false
		GlobalVar.canOpenInventory = true
		GlobalVar.haveFlashLight = false
		GlobalVar.haveGun = false
		GlobalVar.invAmmount = 0
		GlobalVar.invArray = []
		get_tree().change_scene_to_file("res://Scene/WinScene.tscn")
		


func _on_event_8_body_entered(body):
	if body is CharacterBody3D and GlobalVar.winReady:
		addEnemy(Vector3(13, 0.5, 28))
		addEnemy(Vector3(0.3, 0.5, 28))
		addEnemy(Vector3(-13, 0.5, 28))
		$EventTrigger/Event8.queue_free()
