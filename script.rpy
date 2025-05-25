##this is the script for "First trial renpy" It is a good example of various things

define s = Character('Sylvie', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")

image bg meadow = "stormyfield_wallpaper" 
image sylvie neutral = "sylvie_004" 
image sylvie happy = "sylvie_002"
image me neutral = "trex_character"

transform half_size: 
    zoom 0.5 

##this splash screen will alsways start before the Renpy Start menu
label splashscreen:
    scene black
    with Pause(1)

    show text "A Useful Example" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene bg meadow
    show me neutral at left
    show  sylvie neutral
  
    "After a short while, we reach the meadows just outside the neighborhood where we both live."

    "When we were children, we played in these meadows a lot, so they're full of memories."

    m"Hey... Umm..."

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    show sylvie neutral at right

    m "Ummm... Will you..."
    "Will you be my artist for a visual novel?"

menu : 
    m"Well, will you? \n Will you be my artist for a visual novel?"
    "Yes": 
        jump yes
    "No":
        jump no

label yes:
    show sylvie happy at right
    s "Happy happy"
    jump ending

label no:
    show sylvie neutral at right
    s "I'd end up doing all the work, so, No, thank you."
    jump ending

label ending:
    scene black
    with Pause(0.5)

    show text "The end" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return