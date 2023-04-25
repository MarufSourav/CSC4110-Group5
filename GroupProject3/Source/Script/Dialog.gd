extends Area3D
var active = false
var activatedOnce = false
var bodyOnTrigger
@export var oneShot = false
@export var needInteract = false
@export var textString = ""

func _ready():
	activatedOnce = false
	$Label.text = textString
	$Label.visible = false

func _on_body_entered(body):
	if body is CharacterBody3D:
		bodyOnTrigger = true
		if !needInteract:
			active = true
			activatedOnce = true
			Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
			$Label.visible = true
			$Dialog.stop()
			$Dialog.play()

func _on_body_exited(body):
	if body is CharacterBody3D:
		if oneShot and activatedOnce:
			queue_free()
		bodyOnTrigger = false

func _process(_delta):
	if(
Input.is_action_just_pressed("interact")
and needInteract
and bodyOnTrigger
and !active
and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED
):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		$Label.visible = true
		active = true
		activatedOnce = true
		$Dialog.stop()
		$Dialog.play()
	if(Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED and active):
		$Label.visible = false
		active = false
