define config.rollback_enabled = False

define playlist = ["street_night.mp3"]
$ renpy.random.shuffle(playlist) 
play music playlist fadeout 1.0 fadein 1.0 # This should now play the full randomized playlist and then repeat from the begining.


init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act1b:

    play music "street_night.mp3" fadein 1.0

    nvl clear
    scene aequalis with fade

    show enpa happy at right
    with moveinright

    enpa "{i}Finally, back outside-"

    "Ring ring ring!"

    "Enpa jolted in startlement over her phone."

    enpa "Ugh, who could this be?"

    "The caller ID displayed an odd name: Mr. X."

    enpa "{i}Mr. X? Who the hell..."

    "But her curiousity got the better of her, and she answered."

    enpa "Hello, Enpa speaking, who is this and how did you get my number?" 

    "{i}AI time. It'll take a few seconds to load responses. Only click once to proceed."

    python:
        import chatgpt1
        from apikey import openai_api_key

<<<<<<< HEAD


            #The "system" message is the initial prompt of your NPC
            #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC

    python:
            import chatgpt1
            from apikey import openai_api_key

            api_key=openai_api_key

            #The "system" message is the initial prompt of your NPC
            #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
            messages = [
            {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're pretending to be kindhearted and selfless, but in reality, you're a racist old fart who buys women and holds sex parties for other rich people. You're racist and dislike minorities, but pretend you don't care. You're trying to persuade a woman named Enpa over the phone to build a new 'AR tool' that can revolutionize the next video game. You dislike being rejected or doubted, and you're fast to start threatening people if they doubt you. You also know the dark secrets of others, including Enpa's. If she doesn't agree right away, you plan to threaten her by exposing her dark past. Keep your response to a max of 35 words."},
            {"role": "assistant", "content": "And who might you be?"}
            ]

            while True:

                #Then add it in the "history" of messages
 
                if len(messages) < 7:
                     content = "Hello, Enpa speaking, who is this and how did you get my number?"
                else:
                     content = response2

                messages.append(
                    {"role": "user", "content": content}
                )
                
                messages = chatgpt1.completion(messages=messages,api_key=openai_api_key)
                response1 = messages[-1]["content"]

                allen("[response1]")

                messages.append({"role": "user", "content": response1})

                #Switch to Enpa
                messages.append({"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred Studios. You hate how the world is unfair to you despite how intelligent you are. It's made you stern and reserved. You keep your contact information to yourself, and you dislike it when people are not direct with you. You hold a dark secret in the past, where you once accidentally caused the death of a past bully - you expect that no one should know such a secret. Keep your answer to less than 30 words."})
                messages.append({"role": "user", "content": response1})
    
                messages = chatgpt1.completion(
                messages=messages,api_key=openai_api_key
                )

                response2 = messages[-1]["content"]
            
                messages.append({"role": "user", "content": response2})
                
                enpa("[response2]")

                if len(messages) > 10:   # Stop conversation after 4 rounds
                    break
=======
        api_key=openai_api_key

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC

        while True:
            messages = [
            {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're currently trying to persuade a woman named Enpa to build a new 'AR tool' that can revolutionize the next video game, but she declines. Threaten her by claiming you know her darkest secret which will be exposed if she doesn't join. Try not to lose her on the phone, and don't hang up the call. Keep your response to less than 35 words."},
            {"role": "assistant", "content": "And who might you be?"}
            ]

            #Then add it in the "history" of messages
            if len(messages) < 7:
                content = "Hello, Enpa speaking, who is this on the phone? How did you get my number?"
            else:
                content = response2

            messages.append(
                {"role": "user", "content": content}
            )
            
            messages = chatgpt1.completion(messages=messages,api_key=openai_api_key)
            response1 = messages[-1]["content"]

            allen("[response1]")

            if len(messages) > 13:   # Stop conversation after 5 rounds
                break

            messages.append({"role": "user", "content": response1})

            #Switch to Enpa
            messages.append({"role": "system", "content": "Now play the character o f Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred. You're quite arrogant and spoiled, and you think you deserve better. Someone just called you, asking for you to join their project. You declined, but they're persistent on taking you in. Act annoyed as you decline again. Keep your answer to less than 30 words."})
            messages.append({"role": "user", "content": response1})

            messages = chatgpt1.completion(
            messages=messages,api_key=openai_api_key
            )

            response2 = messages[-1]["content"]
        
            messages.append({"role": "user", "content": response2})
            
            enpa("[response2]")

            if len(messages) > 10:   # Stop conversation after 4 rounds
                break
>>>>>>> 2c0005c0bf65add6f23dbcb9badf9eca9a6acaf2

    enpa "What?! You... How could you know such a-"

    allen "Listen, besides keeping your secret, I'm also willing to award you a million dollars to join my project. It'll be a full-time commitment for about a month. You'll be free and rich after that."

    enpa "..."

    enpa "Okay, fine I'll consider it. Is there a time and date when I should meet you? And where?"

    allen "Twelve O'clock tomorrow at Hundred Studios building four. That work for you?"

    enpa "Yes."

    stop music fadeout 1.0

    "As Enpa wrapped up her bizarre call, she continued home with continued mixed feelings about the arrangement."

    jump act2b
