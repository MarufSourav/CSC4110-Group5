extends CharacterBody3D
var SPEED = 2.0
var REST = false
var sprinting = true;
var moving = false;
var stamina = 5
var mouse_sensitivity := 0.1

@export var walkSoundLoader = ""
@export var runSoundLoader = ""
@onready var walkAudio = $Walk
@onready var runAudio = $Run
@onready var restAudio = $Rest
@onready var handGun = $CameraHolder/Camera3D/Fire/HandGun
@onready var fireMovement = $CameraHolder/Camera3D/Fire

var movingState = false
var sprintingState = false
var restState = false
var stateChanged = false;

@onready var flashlightSound := $Flashlightclick

var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")
@onready var camera := $CameraHolder
@onready var flashlight = $CameraHolder/Camera3D/SpotLight3D

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
	

func _unhandled_input(event) -> void:
	if(event.is_action_pressed("restart")):
		GlobalVar.freezePlayer = false
		GlobalVar.canOpenInventory = true
		GlobalVar.keyID = ""
		GlobalVar.haveFlashLight = false
		get_tree().reload_current_scene()
	if(event.is_action_pressed("ui_cancel")):
		get_tree().quit()
	if event.is_action_pressed("inventory") and GlobalVar.canOpenInventory:
		if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
			Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
			GlobalVar.freezePlayer = true
		else:
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)
			GlobalVar.freezePlayer = false
	if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		if event is InputEventMouseMotion:
			if !GlobalVar.freezePlayer:
				camera.rotate_z(deg_to_rad(-event.relative.y * mouse_sensitivity))
				rotate_y(deg_to_rad(-event.relative.x * mouse_sensitivity ))
				camera.rotation_degrees.z = clamp(camera.rotation_degrees.z, -75, 75)
		if Input.is_action_just_pressed("flashlight") and GlobalVar.haveFlashLight:
			flashlight.visible = !flashlight.visible
			flashlightSound.play()


func soundPass():
	if moving != movingState:
		stateChanged = true
		movingState = moving
	if sprinting != sprintingState:
		stateChanged = true
		sprintingState = sprinting
	if REST != restState:
		if REST:
			restAudio.play()
		restState = REST
	
	if stateChanged:
		walkAudio.stream = load(walkSoundLoader)
		runAudio.stream = load(runSoundLoader)
		if moving:
			$CameraHolder/Camera3D/AnimationPlayer.play("HeadBob")
			if sprinting:
				$CameraHolder/Camera3D/AnimationPlayer.play("HeadBobFAST")
				walkAudio.stop()
				runAudio.play()
			else:
				walkAudio.play()
				runAudio.stop()
		else:
			$CameraHolder/Camera3D/AnimationPlayer.stop()
			walkAudio.stop()
			runAudio.stop()
		stateChanged = false


func _process(delta):
	soundPass()
	if(Input.is_action_pressed("ADS")):
		handGun.position = lerp(handGun.position, Vector3(0,-0.155, -0.35), 7 * delta)
		handGun.rotation_degrees = lerp(handGun.rotation_degrees, Vector3(0,-180, 0), 7 * delta)
	else:
		handGun.position = lerp(handGun.position, Vector3(0,-0.25, -0.35), 7 * delta)
		handGun.rotation_degrees = lerp(handGun.rotation_degrees, Vector3(0,-180, -30), 7 * delta)
		
	if(Input.is_action_just_pressed("FIRE")):
		print("Fired")
		$CameraHolder/Camera3D/Fire/HandGun.gunFlash = true
		$CameraHolder/Camera3D/AnimationPlayer.play("screenShake")
		fireMovement.position = lerp(fireMovement.position, Vector3(0, -0.05, 0.6), 10 * delta)
		fireMovement.rotation_degrees = lerp(fireMovement.rotation_degrees, Vector3(7, 0, 0), 70 * delta)
	else:
		fireMovement.position = lerp(fireMovement.position, Vector3(0, 0, 0), 10 * delta)
		fireMovement.rotation_degrees = lerp(fireMovement.rotation_degrees, Vector3(0, 0, 0), 10 * delta)
	
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
	if not is_on_floor():
		velocity.y -= gravity * delta
	
	if(!GlobalVar.freezePlayer):
		var input_dir = Input.get_vector("move_backward", "move_forward", "move_left", "move_right")
		var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
		if direction:
			velocity.x = direction.x * SPEED
			velocity.z = direction.z * SPEED
		else:
			velocity.x = move_toward(velocity.x, 0, SPEED)
			velocity.z = move_toward(velocity.z, 0, SPEED)
		move_and_slide()
	else:
		moving = false
		sprinting = false
