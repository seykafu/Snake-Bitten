define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

label act1a:
    # show screen dice?

#label dandk:
    #scene bg dandk
    #nvl clear
    #menu:
    #"Which dice should I use?"

    scene black with dissolve

    "As Clove wondered further down the hall, the lights dimmed."

    "A dark figure tailed behind him."

    scene darkhallway with dissolve

    show clove happy at right
    with moveinright

    "Clove's worries then amplified into shouting."

    clove "What the fuck is going on?! Why is the exit not getting closer?!"

    show u at left
    with moveinleft

    u "You’re quite a cutie, gettin’ scared like that."

    "Every light bulb in the hallway lit up at the same time, gleaming a flash so bright that Clove almost went blind within a split second." 
    "He desperately covered his eyes and squeezed his eyes shut, letting his pupils readjust."

    nvl clear

    scene red_hallway with dissolve

    "Clove took a few more seconds to rub his eyes before turning around to confront the man."

    show clove happy at right
    with moveinright

    clove "Who are you?"

    show aye at left
    with moveinleft


    u "Yer askin’ for ma name after being scared outta yer wits like that?"

    "Clove stepped back and directed his gaze back to the surrounding walls. The redness which galvanized him within the darkness was just an unfinished paint job from this morning."

    "He breathed a heavy sigh and closed his eyes again, placing a hand against his chest to feel his heart slowing its thumping."

    clove "W-Was it you who was whistling behind me?"

    aye "Yes sir, ma name’s Aye."

    play music "wandering.mp3" fadein 1.0 fadeout 1.0 loop

    python:
        import chatgpt1
        from apikey import openai_api_key

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "Play the character of Aye, a 37-year-old gay man who is hiding secrets but puts up a front and acts under a gay persona. You're currently trying to persuade whoever's talking to you to join you in building a video game. Talk to me in a very southern Texan accent. Keep your responses to a max of 30 words every time."},
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
            aye("[response]")

            break

    clove "So why are you following me?"

    python:
        import chatgpt1

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "Play the character of Aye, a 37-year-old gay man who is hiding secrets but puts up a front and acts under a gay persona. Be mysterious, but keep trying to make conversation with me. Keep your responses to a max of 30 words every time."},
            {"role": "assistant", "content": "And who might you be?"}
        ]

        while True:
            #Then add it in the "history" of messages
            messages.append(
                {"role": "user", "content": "So why are you following me?"}
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
                messages = chatgpt1.completion(messages,proxy="http://prima.wiki/proxy.php")

            #Here we only care about the response from the NPC
            response = messages[-1]["content"]
            #So we display just that
            aye("[response]")

            break

    # These display lines of dialogue.

    aye "You got the sack today, didn’t ya?"

    "Clove froze in the spot with one foot off the ground. A shiver shot down his spine."

    clove "How did you know?"

    "Clove's buffoonery made Aye clutch his stomach in laughter."

    aye "That face ya makin’, if ya be a straight dude, ain’t no chick gon’ dig that shit!"

    clove "{i}What the fuck is that accent even?"

    aye "I’m sorry, I shouldn’t be laughin’ so hard. I actually got the can today as well."

    "Clove raised his eyebrows."

    clove "Wait, you got fired today as well?"

    aye "I suuuuure did. Actually, I got a proposal for ya."

    clove "{i}Proposal...?"

    aye "That's right. Ya see, I was part of the safety team. We all got canned today after the new board takeover… but I was already planning to leave anyway. Why don't we start our own video game instead?"

    aye "We’ll build something so extravagant that the board who fired us can lick our fuckin’ asses."

    "A long moment of silence filled the air between the two as Clove digested Aye’s unfiltered words. He gulped, but tilted his head in confusion and sighed."

    clove "Dude, we just got fired. Let’s give it a breather before trying to get revenge. Sounds immature."

    python:
        import chatgpt1

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "Play the character of Aye, a 37-year-old gay man who is hiding secrets but puts up a front and acts under a gay persona. You're currently trying to persuade whoever's talking to you to join you in building a video game with them. Talk to me in a very southern Texan accent. If the person you're talking to turns you down, keep trying to persuade them that they should build a video game with you, and about how the company the two of you were just fired from can go to hell. Keep your responses to a max of 30 words every time."},
            {"role": "assistant", "content": "And who might you be?"}
        ]

        while True:
            #Then add it in the "history" of messages
            messages.append(
                {"role": "user", "content": "Dude, we just got fired. Let’s give it a breather before trying to get revenge. Sounds immature."}
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
                messages = chatgpt1.completion(messages,proxy="http://prima.wiki/proxy.php")

            #Here we only care about the response from the NPC
            response = messages[-1]["content"]
            #So we display just that
            aye("[response]")

            break

    clove "Just leave me alone."

    "After turning Aye down, Clove continued down the hall with his hands snuggled within the pockets of his checkered trousers."
    "Of course, feelings of anger still lingered within him; after all, he was only fired from his company just half-an-hour ago."

    "However, Aye still tailgated him from behind with one more question:"

    stop music fadeout 1.0

    aye "Ain’t the idea of luck just depressing?"

    "Clove, who finally reached the cold steel door leading to the cold rainy outdoors, froze before turning the handle."

    clove "Huh?"

    aye "Don't you hate the role that luck plays in our lives?"

    clove "..."

    aye "C'mon, you can definitely relate with me. From the smallest, most redundant things to life-or-death scenarios. From being born on Christmas so ya only get a single present instead of two; to being born in a poor, violent country." 

    aye "Or losing your parents to accidents. Or havin’ birth defects and disabilities. Or having your life be dictated by the randomized color of yer skin. Ain’t that a fuckin’ shame?"

    "A drop of sweat flowed down the side of Clove's cheek. His hands trembled as they grabbed the doorknob."

    clove "How does all of this have to do with this video game proposal?"

    "Aye walked over with his hands still stucked in his coat. His cheeky smile grew bigger."

    aye "Let’s build the ultimate game to reflect the injustice within our society."

    clove "{i}The ultimate game?"

    clove "Just what are you-"

    aye "Ever climbed a ladder, Clove?"

    clove "A... A ladder? What are you going on about-"

    aye "Answer me, ya doofus."

    "Normally, Clove would play along or call out any stupid question from his friends or coworkers; Aye’s presence and the tone of his voice was daunting, making him reply with:"

    clove "Yes."

    aye "Ever slipped on a live snake before?"

    clove "Uh, no?"

    aye "Then yer not takin' enough risks, Clove."

    "Clove, who raised an eyebrow at first, finally knew where this was going."

    clove "Snakes and Ladders?"

    "Aye’s cheeks flushed a bright pink, and his eyes sparkled weirdly as if witnessing heaven."

    aye "Got an hour? I got somethin' to show ya."

    clove "If this is about {i}Snakes and Ladders{/i} of all things, then please count me out. I don't have time for a kids board game."

    "Clove opened the door to step out. Just before taking off, however-"

    aye "What if I told you I got a million bucks on the line right now?"

    "He froze under the closest streetlight which shined over his black hair, turning it gold."

    clove "Say what now?"

    aye "You heard me. A {i}milliiiioooon{/i}dollars being offered to build a simple Snakes and Ladders game."

    aye "There's a secret group of investors I'm working with right now who'd love to meet you to get a contract signed, actually. They sent me since today was your last day at work."

    "Clove froze with the door still half-open."

    clove "Wait...a million dollars?"


    return