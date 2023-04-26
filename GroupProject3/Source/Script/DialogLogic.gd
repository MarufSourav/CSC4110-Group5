extends Area3D
var bodyOnTrigger
@export var oneShot = false #Only Tigger Once
@export var freeze = false #Freeze Player On Trigger
@export var needInteract = false #Needs Interaction For Trigger
@export var textString = "" #User Input Dialog

func _ready():
	##Setting Up the Text Instance
	$Label.text = textString
	$Label.visible = false
	pass
	
func _unhandled_input(event) -> void:
	##Dialog End Logic For When Player is Frozen
	if event is InputEventMouseButton:
		if bodyOnTrigger:
			GlobalVar.freezePlayer = false
			GlobalVar.canOpenInventory = true
			if $Label.visible and oneShot:
				queue_free() ##Delete's Node for OneShot
			$Label.visible = false

func _on_body_entered(body):
	if body is CharacterBody3D: ##When the body that entered is Player
		bodyOnTrigger = true
		if !needInteract: ##Dialog Trigger Logic for Non-Interact
			if freeze: ##Freeze Flag
				GlobalVar.freezePlayer = true
				GlobalVar.canOpenInventory = false
			else: ##Timer (line 54)
				$Timer.start()
			$Label.visible = true
			
			##Dialog Sound
			$Dialog.stop()
			$Dialog.play()

func _on_body_exited(body):
	if body is CharacterBody3D:
		bodyOnTrigger = false

func _process(_delta):
	if($Label.text != textString):
		$Label.text = textString
	if bodyOnTrigger:
		##Dialog Trigger Logic for INTERACTION
		if (Input.is_action_just_pressed("interact") and needInteract): 
			if freeze:
				GlobalVar.freezePlayer = true
				GlobalVar.canOpenInventory = false
			else:
				$Timer.start()
			$Label.visible = true
			
			##Dialog Sound
			$Dialog.stop()
			$Dialog.play()

func _on_timer_timeout(): ##Dialog End Logic For When Player is NOT FROZEN
	if oneShot:
		queue_free()
	$Label.visible = false
	$Timer.stop()
