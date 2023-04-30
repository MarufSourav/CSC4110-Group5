extends Node3D
@onready var doorAudio = $door
@onready var doorClick = $click
@onready var doorUnlocked = $unlocked
@onready var dialogTrigger1 = $DialogTrigger
@onready var dialogTrigger2 = $DialogTrigger2
@export var isOpen = false
@export var buttonActive = true
@export var doorLocked = false
@export var doorID = ""
var keyID = ""
var doorState = false
var onTrigger = false

func _ready():
	doorState = isOpen
	if isOpen:
		$Door.position = Vector3(0,-0.1, -2.1)
		$Collision.position = Vector3(0, -2.4, 0)
	else:
		$Door.position = Vector3(0, -0.1, 0)
		$Collision.position = Vector3.ZERO
	if !doorLocked:
		dialogTrigger1.queue_free()
		dialogTrigger2.queue_free()

func doorAudioLogic():
	if isOpen != doorState:
		if isOpen:
			doorAudio.stream = load("res://Sound/door-open1.mp3")
			doorAudio.play()
			doorState = true
		else:
			doorAudio.stream = load("res://Sound/door-close1.mp3")
			doorAudio.play()
			doorState = false

func _unhandled_input(_event) -> void:
	if Input.is_action_just_pressed("interact") and onTrigger and buttonActive:
		if doorID == keyID:
			dialogTrigger1.queue_free()
			dialogTrigger2.queue_free()
			doorUnlocked.play()
			doorLocked = false
			for i in GlobalVar.invArray:
				if i[0] == "key":
					if str(i[1]) == keyID:
						GlobalVar.invArray.erase(i)
						GlobalVar.invAmmount -= 1
						break;
			doorID = "0"
		doorClick.play()
		buttonActive = false
		$Timer.start()
		if !doorLocked:
			isOpen = !isOpen
	if !isOpen:
		$Collision.position = Vector3.ZERO

func _process(delta):
	if isOpen:
		$Door.position = lerp($Door.position, Vector3(0,-0.1, -2.1), 2.5 * delta)
	else:
		$Door.position = lerp($Door.position, Vector3(0, -0.1, 0), 2.5 * delta)
	doorAudioLogic()

func _on_area_3d_body_entered(body):
	if body is CharacterBody3D:
		onTrigger = true
		for i in GlobalVar.invArray:
			if i[0] == "key":
				if doorID == str(i[1]):
					keyID = str(i[1])
					break;
		

func _on_area_3d_body_exited(body):
	if body is CharacterBody3D:
		onTrigger = false
		keyID = ""


func _on_timer_timeout():
	$Collision.position = Vector3(0, -2.4, 0)
	buttonActive = true
	$Timer.stop()
