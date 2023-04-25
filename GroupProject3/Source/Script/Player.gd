extends CharacterBody3D
var SPEED = 2.0
var REST = false
var sprinting = true;
var moving = false;
var stamina = 5
var mouse_sensitivity := 0.1
@export var keyID = ""
@onready var flashlightSound := $Flashlightclick
#const JUMP_VELOCITY = 4.5

var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")
@onready var camera := $Camera3D
@onready var walkAudio = $Walk
@onready var runAudio = $Run
@onready var flashlight = $Camera3D/SpotLight3D
func _unhandled_input(event) -> void:
	if event is InputEventMouseButton:
		Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	elif event.is_action_pressed("ui_cancel"):
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		
	if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		if event is InputEventMouseMotion:
			camera.rotate_z(deg_to_rad(-event.relative.y * mouse_sensitivity))
			rotate_y(deg_to_rad(-event.relative.x * mouse_sensitivity ))
			camera.rotation_degrees.x = clamp(camera.rotation_degrees.x, -75, 75)
		if Input.is_action_just_pressed("flashlight"):
			flashlight.visible = !flashlight.visible
			flashlightSound.play()

func _process(delta):
	if velocity.x != 0 or velocity.z != 0:
		moving = true
	else:
		moving = false
	if Input.is_action_pressed("sprint"):
		sprinting = true
	else:
		sprinting = false
	
	if sprinting and moving and !REST:
		SPEED = 4
		stamina -= 1 * delta
		if stamina < 0:
			stamina = 0
			REST = true
	else:
		if REST:
			SPEED = 0.5
		else:
			SPEED = 2
		stamina += 1 * delta
		if stamina > 5:
			stamina = 5
			REST = false

func _physics_process(delta):
	if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		if not is_on_floor():
			velocity.y -= gravity * delta
 
	# Handle Jump.
	# if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		# velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	
		var input_dir = Input.get_vector("move_backward", "move_forward", "move_left", "move_right")
		var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
		if direction:
			velocity.x = direction.x * SPEED
			velocity.z = direction.z * SPEED
		else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
			velocity.z = move_toward(velocity.z, 0, SPEED)
		move_and_slide()
