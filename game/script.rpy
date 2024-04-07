# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Detective Elowen Lumiereen")
define Bruntforce = Character("Bruntforce")
define Narrator = Character("")
define Rex = Character("Prosecutor Reginald “Rex” Alinpagne II")
define Unknown = Character("???")
define Judge = Character("Judge")
define Snake = Character("Azazel The Snake")
define Altheia = Character("Altheia Edenia")
define Verus = Character("Verus")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Main_Screen


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Mother_Sprite

    show Main_Character_Sprite

    # These display lines of dialogue.

    Narrator"Date: April 11, 2022 8:45am"

    p "Heart racing"

    p "Clammy hands" 
    
    p "Yep, I’m definitely back in the courtroom."

    p"I would have wished to never return to this place, but life has a way of taking unexpected turns…"

    Unknown"MA’AM!"

    show Brunt_Force

    play music "Song1.mp3" loop


    p"Gah! Bruntforce, you startled me! A softer announcement of your arrival would be much appreciated."

    Bruntforce"SORRY MA’AM! THIS IS JUST A NERVE-RACKING CASE! IT FEELS LIKE THE ENTIRE DEPARTMENT IS CRUMBLING FROM THIS CASE!"

    p" It certainly feels that way…"

    p"Damian Bruntforce, my Investigation Assistant. He can be… crass at times, but he has worked with me since I joined 20 years ago. He’s proved himself through thick and thin. We’ve been through those rough times, we’ll get through this one."

    p"…do you think that we can make it through this one, Vulga?"

    Bruntforce" … "

    Bruntforce"Now is not the time to doubt our actions. Everything up until this point has been leading us towards your dream. To falter now would be to jeopardize"

    p" You’re right. I don’t know what came over me. I suppose we should begin the actual debriefing of the case-" 

    Narrator"Damian Bruntforce, my Investigation Assistant. He can be… crass at times, but he has worked with me since I joined 20 years ago. He’s proved himself through thick and thin. We’ve been through those rough times, we’ll get through this one."

    p"…do you think that we can make it through this one, Vulga?"

    Bruntforce"..."

    Bruntforce"Now is not the time to doubt our actions. Everything up until this point has been leading us towards your dream. To falter now would be to jeopardize "

    p"You’re right. I don’t know what came over me. I suppose we should begin the actual debriefing of the case-"

    stop music fadeout 3.0

    Narrator "Large thundering steps come from across the room"

    #enter image of Prosecutor

    Rex "I’m sorry Lady Lumiere, I’m afraid that is not possible."

    #shocking music plays here

    p"!!!"

    Rex"Because this case is dealing with heavy matters within the department, the higher ups want this trial to progress as quickly as possible. I must carry out their orders as the Chief Prosecutor."

    p"…I understand Reginald."

    Rex"That being said… I am deeply sorry for the position this puts you in. I wish for the most favorable outcome towards your endeavor. "

    p"Thank you, Rex. Let's not prolong this trial any longer."

    Rex"After you"

    Bruntforce"Here we go…"

    Narrator"No turning back now. May our skeletons stay inside of our closets."

    scene Court_Room

    Narrator"*Entering the Courtroom*"

    Narrator"*General chatter*"

    Narrator"*Bailiff announcement???*"

    Narrator"*Judge’s Seance*"

    Judge"…"
    
    Judge"*Stands above chair*"

    Judge"*sets objects down*"

    Judge"…"

    Judge"Oh my gawd. Are all of you waiting for me to start the trial? Tehe, lets fuck this bitch up-"

    Snake"Altheia! Courtroom! Please, your etiquette!"
    
    Altheia"Oh shit you’re totally right!... oh uhh"
    
    Snake"…"

    Snake"Is the defense ready?"

    p"The defense is ready, Azazel."  

    Snake"Is the prosecution ready?"

    Rex"Of course, Your Excellence."

    Judge"Unghhh, sorry Azzy… (pouty emote)"

    Judge"Wait, Lumiere? Elowen Lumiere? Aren’t you like, a detective now? Why are you with the defense for today’s trial?"

    p"…."

    p"Considering the weight this trial carries for my entire department, I found it necessary to take on the responsibility of defending its integrity. Whatever may come, I will take on the consequences that come from the truth of this trial."

    Judge"Woahh, sick! No issues from me then! Please carry on, Azzy!"

    Snake"Would the Prosecution please begin its opening statement"

    Rex"Of course, right away."

    Rex"Let’s begin with a summarization of the incident of the events that transpired over the past 24 hours. The victim of this case is one Myra Ereuno, a rising author who has been taken before her grandiose debut. To add to the tragedy, the incident occurred within the safety of her own home. Out in the Forest of Evocation, her residence provided the perfect environment for curing her writer’s block, but also the scene of the crime."

    Snake"Ah yesss, I do remember reading her novel, “The Secrets Behind Their Leaves”."

    Judge"Aww, that’s the victim? I read her short series, “Palace of Haunting Wonders”. I love the allusions to the reader to start their own journeys. She was totally topping the charts in the young adult category."

    Rex"Truly a great loss for our young scholars, however, we must press onwards with the trial. We have a photo of the crime scene."

    Rex"This photo depicts the state the body was in when it was discovered."

    #insert image of autopsy report

    Judge"Oh wow that’s awful. Kinda looks like she went through a lot before she left us."

    Rex"The autopsy report depicts the cause of death as blunt force trauma to the front and back of the head."

    Rex"However, they also discovered bruises around her neck, suggesting she was strangled some point before her untimely demise."

    Snake"Sneaking up on her and taking her out while her guard was down… what an underhanded tactic from an unsavory individual."

    Judge"Who IS this supposed unsavory?"

    Rex"…"

    p"… (Here it comes)"

    Rex"The prosecution wishes to call the defendant themself to take the stand and testify to the scene of the crime."

    Narrator"*The Defendant takes the stand*"

    Rex"Would you be so kind as to state your name and occupation to the courtroom?"

    Unknown"…sure. I suppose I don’t mind."

    Verus"My name is Verus. Verus Lumiere. As for my occupation, I suppose I was a college student studying environmental sciences, until about 8:10pm last night, when I was apprehended by officers and taken to the detention center. I guess my profession now would be best described as the “defendant”."

    Judge"Oh no. You’re the Detective’s kid, aren’t you?"

    Verus"I am the child of the soon-to-be District Detective, Elowen Lumiere."

    # (some gap for relevance sake)

    # Cross-Examination

    Verus"“I received a text from Myra at around 6:30pm. We haven’t spoken for some years, so I was caught off guard by her message. She wanted to talk, expressing a desire to reconnect. She said to meet her at her new estate in the Forest of Evocation at 8:30pm. However, I could not wait that long. It was about 7:45pm when I knocked on her door. She didn’t answer, so I tried the door handle, which worked to my surprise. I walked in, searched for her, and discovered her body in her study.”
    The shock, the uncanniness, I was frozen in place."



    menu:
        "Try out a forking paths!":
            p "Nice! Good job trying out a path!"
            jump next  # Corrected line
        "Try this forking path.":
            p "Good job, you're trying out a new path!"
            jump next  # Corrected line

label next:
    scene Menu_Screen
    show Mother_Sprite
    menu:
        "End the game":
            p "Good job! You ended the game!"
            return
        # This ends the game.
