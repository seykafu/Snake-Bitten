define config.rollback_enabled = False

define playlist = ["saving.mp3", "japan.mp3"]

$ renpy.random.shuffle(playlist) 

# Deleted the defines and put them into a separate file.

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label intro:

    #play music playlist fadeout 1.0 fadein 1.0 # This should now play the full randomized playlist and then repeat from the begining.

    scene aequalis
    with fade

    play music "saving.mp3" fadein 1.0

    m "Hai hai! J.X. here. Nice to meet ya! Welcome to the world of Aequalis, an island-country in the South Pacific Ocean. It's capital, Aequal, is a sprawling metropolis full of skyscrapers, busy roads, and buzzing streets."

    m "You'll find all walks of life here: homeless, businesspeople, and health professionals."

    m "The city also has a booming game development scene. The largest game company, Hundred Studios, has thousands of employees working across multiple projects."

    m "In this story, you can choose to play two different characters, which will greatly affect the POV and how the story unfolds."

    m "Please choose now - Enpa or Clove?"
    # letting the user choose between Enpa (female) or Clove (male).
   
    call screen select_character
    if _return == "MC":
        jump mc_start
    elif _return == "FMC":
        jump fmc_start

label mc_start:

    m "Cool, you'll play Clove then!"

    m "Before I go further, please start by inputing your OpenAI API key. If you don't have one, that's okay! The game will go on under its default script. You'll still have fun regardless."

    m "If you're unsure where to find your API, just search 'Where do I find my Secret OPENAI API Key?' on Google. Note that you need to create an OPENAI account."

    python:
        #We get the API Key from the User. Because you should NEVER give your API key in any form with your game let alone share it on a public repository
        #How to distribute your game with an embbed API KEY ? I'll soon make a special server system to make it possible
         apikey = renpy.input("What is your OPENAI API Key? (leave empty if you don't have any)", length=64)

    if apikey != "":
        m "Success!"
    else:
        m "If you don't have any, I'll be using my proxy to give you the best experience possible."

    m "Oh! And last but not least! When conversing with the AI, please keep your convos civil. Don't say anything impudent please..."

    m "Okie, let's go. Welcome... to {i}'Snake Bitten!'{/i}"

    scene black with dissolve

    play music "dramatic.mp3" fadeout 1.0 fadein 1.0

    "The hallway was as dark as a blackhole, and its walls were slathered with an unfinished crimson red paint job that reminded Clove of blood. "

    "He kept pacing to the exit at the end, hoping for more light to emerge."

    nvl clear

    scene red_hallway
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show clove happy at right
    with moveinright

    # These display lines of dialogue.

    clove "In the two years I was here, I've never seen this hallway before. Is this new?"

    clove "{i}This paint... is it really even paint?{/i} What the hell even happened here?!"

    clove "{i}Man, fuck this company. Maybe I should be glad we're parting ways.{/i}"

    clove "Wait, is someone there?"

    show enpa happy at left
    with moveinleft 

    enpa "..."

    python:
        import chatgpt1

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "Play the character of Enpa, a 28-year-old woman who's currently working for {i}Hundred Studios{/i}, the largest game company in Aequal. You're incredibly intelligent, but sometimes lack social skills. You're on your way out of the office in a hurry, hoping to find dinner somehwere nearby. If someone tries to talk to you, please excuse yourself immediately and leave wherever you are. Don't be nice, act insolent and busy. Keep your responses to a max of 20 words every time."},
            {"role": "assistant", "content": "And who might you be?"}
        ]

        while True:
            #We ask the user for an input
            user_input = renpy.input("As Clove, feel free to say something: ", length=100)
            #Then add it in the "history" of messages
            messages.append(
                {"role": "user", "content": user_input}
            )

            if apikey != '':
                #We ask ChatGPT to "complete" the conversation by adding a response
                #If you have an API key, let's use that
                messages = chatgpt1.completion(messages,api_key=apikey)
            else :
                #If you don't provide an API key, we'll use my proxy
                #This proxy only allows a set of NPCs, and serves to "hide" my API key
                #Check the README.md to know more about it
                #Of course if you modify the NPC in any way, it won't work, you'll have to use your own API key instead.
                messages = chatgpt1.completion(messages,openai_api_key)

            #Here we only care about the response from the NPC
            response = messages[-1]["content"]
            #So we display just that
            enpa("[response]")

            break

    hide enpa happy with moveoutleft

    clove "I.. I see. Well, nevermind that, I guess. Gotta get out of this scary-looking hallway first."