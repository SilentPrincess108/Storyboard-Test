# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "The room is silent. The sun gently sets as it's rediant rays paint the room in a gentle gold."
    "Although it's warmth envelopes you and brings comfort, that feeling soon subsides as the rays hit your eyes."
    "You wince--as the gentle rays now suddenly dramatic--stun your eyes."

    # This ends the game.

    return
