extends Node3D
@export var isOpen = false
@export var onTrigger = false
@export var buttonActive = true
@onready var doorAudio = $door
@onready var doorClick = $click
@export var doorLocked = false
@export var doorID = ""
var keyID = ""

func _ready():
	if isOpen:
		$Door.position = Vector3(0,-0.1, -2.1)
		$Collision.position = Vector3(0, -2.4, 0)
	else:
		$Door.position = Vector3(0, -0.1, 0)
		$Collision.position = Vector3.ZERO
	if !doorLocked:
		$DialogTrigger.queue_free()
		$DialogTrigger2.queue_free()
func doorAudioLogic():
	if isOpen:
		doorAudio.stream = load("res://Sound/door-open1.mp3")
		doorAudio.play()
	else:
		doorAudio.stream = load("res://Sound/door-close1.mp3")
		doorAudio.play()
func _unhandled_input(event) -> void:
	if Input.is_action_just_pressed("interact") and onTrigger and buttonActive:
		if doorID == keyID:
			$DialogTrigger.queue_free()
			$DialogTrigger2.queue_free()
			doorLocked = false
			doorID = ""
		doorClick.play()
		buttonActive = false
		$Timer.start()
		if !doorLocked:
			isOpen = !isOpen
			doorAudioLogic()
	if !isOpen:
		$Collision.position = Vector3.ZERO

func _process(delta):
	if isOpen:
		$Door.position = lerp($Door.position, Vector3(0,-0.1, -2.1), 2.5 * delta)
	else:
		$Door.position = lerp($Door.position, Vector3(0, -0.1, 0), 2.5 * delta)

func _on_area_3d_body_entered(body):
	if body is CharacterBody3D:
		onTrigger = true
		keyID = body.keyID
		if(keyID == doorID):
			$DialogTrigger.position = Vector3(0,1.8,0)
			$DialogTrigger2.position = Vector3(0,1.8,0)

func _on_area_3d_body_exited(body):
	if body is CharacterBody3D:
		onTrigger = false
		keyID = ""
		if doorLocked:
			$DialogTrigger.position = Vector3(0.26,0.42,1.34)
			$DialogTrigger2.position = Vector3(-0.2,0.37,-1.36)


func _on_timer_timeout():
	$Collision.position = Vector3(0, -2.4, 0)
	buttonActive = true
	$Timer.stop()
