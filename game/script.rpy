# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alice", color = "#FFD1DC")


# The game starts here.

label start:

    python:
        name = renpy.input("What is your name: ")
        name = name.strip() or "Player"
    
    define p = Character("[name]")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "The room is silent. The sun gently sets as it's radiant rays paint the room in a gentle gold."
    "Although it's warmth envelopes you and brings comfort, that feeling soon subsides as the rays hit your eyes."
    "Wincing, you let out a long yawn, throwing your back against your chair."
    "A series of cracks echoes throughout the classroom and you sigh in relief, slumping in your chair."

    p "I'm still in class...?"

    "You glace at the clock at the front of the classroom."
    "It's 4:30 pm."

    "Behind you, you hear the classroom door open, followed by gentle steps that slowly grow closer."

    show alice_default:
        zoom 0.7
        xalign 0.5

    a "Hey [name], are you ok?"

    p "This is Alice. We've been friends"

    # This ends the game.

    return
