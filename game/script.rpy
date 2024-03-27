# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    menu:
        "Try out a forking paths!":
            e "Nice! Good job trying out a path!"
            action Jump("next")
        "Try this forking path.":
            e "Good job, you're trying out a new path!"
            action Jump("next")
label next:
    scene bg 262.jpg
    show eileen happy
    menu:
        "End the game":
            e "Good job! You ended the game!"
            return
    # This ends the game.


