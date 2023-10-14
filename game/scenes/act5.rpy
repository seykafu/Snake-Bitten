define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act5:

    nvl clear
    scene clove_room with fade

    show clove happy at center 
    with moveinleft

    clove "..."

    clove "I can't believe I got involved with this whole project..."

    clove "I mean the money is nice, but why does it have to be a 'Snakes and Ladders' type of game?"

    clove "Can't I at least change some things about it?"

    "{i}Knock knock"

    clove "Huh? {i} Who could this be..."

    "Clove paced over to his door and peeked into the doorhole. His eyes widened in surprise to find a pretty lady standing by herself in the hallway."

    clove "Um, who are- {i}Wait, it's that girl I saw back in the old Hundred building!"

    show enpa happy at left
    with moveinleft
    
    enpa "Let me in. I have something to discuss with you."

    python:
        import chatgpt1
        from apikey import openai_api_key

        api_key=openai_api_key

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "First, play the character of Clove, a 26-year-old smart and witty game developer who was recently laid off from his company, Hundred. Now, he's working on a new project that will earn him 1 million dollars upon completion. He's working in his own luxury office but is baffled when his new manager tells him to make a basic snakes and ladders game for the PC. If anyone wants to come into his office room, he greets them cautiously and only lets them in if he's convinced they have good intentions. He doesn't know what else is doing on with the project, since his manager only told him what he needs to work on and nothing else. Keep your answers to 40 words maximum and don't cut any responses out abruptly. A girl named Enpa is knocking on your door, and you've seen her before at your old company building. Finish the sentences appropriately within the word limit."},
            {"role": "assistant", "content": "And who might you be?"}
        ]

        while True:

            #Then add it in the "history" of messages
            if len(messages) < 7:
                    content = "My name is Enpa. Let me in. I have something to discuss with you."
            else:
                    content = response2

            messages.append(
                {"role": "user", "content": content}
            )
            
            messages = chatgpt1.completion(messages=messages,api_key=openai_api_key)
            response1 = messages[-1]["content"]

            clove("[response1]")

            messages.append({"role": "user", "content": content})

            #Switch to Enpa
            messages.append({"role": "system", "content": "Now, Play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred Studios. The reason why you were laid off was because you were being racist toward a colleague. You're quite arrogant and spoilted, and you think you deserve better. You're interested in a project proposal with your former company because they're offering you a million dollars. They want you to build an 'AR tool' that will help enable a real-life version of Snakes and Ladders. You're entering the office of Clove, someone who you've recently discovered has also been paid a million dollars to build a Snakes and Ladders game on the PC for the same company as yours. You decide you want to steal his game code, so you greet him carefully and ask to see his computer screen. Act stoic but keep pestering to see his screen. You only need a second to memorize his code. Once you get a look, quickly excuse yourself and leave his office. Keep your answer to less than 40 words."})
            messages.append({"role": "user", "content": response1})

            messages = chatgpt1.completion(
            messages=messages,api_key=openai_api_key
            )

            response2 = messages[-1]["content"]
            
            enpa("[response2]")

            content = response2
        
            messages.append({"role": "user", "content": content})
            
            if len(messages) > 20:   # Stop conversation after 6 rounds
                break