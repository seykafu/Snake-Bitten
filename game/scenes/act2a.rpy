define config.rollback_enabled = False

define playlist = ["saving.mp3", "japan.mp3"]
$ renpy.random.shuffle(playlist) 
play music playlist fadeout 1.0 fadein 1.0 # This should now play the full randomized playlist and then repeat from the begining.

label act2a:
    show screen dice
    scene office_lobby with dissolve

    show clove happy at right
    with moveinright

    clove "I can't believe I signed up for this garbage project. I mean who wants to build a Snakes and Ladders game of all things? A stupid basic game of pure luck."

    show allen at left
    with moveinleft

    allen "You must be Clove. Aye told me all about you. I heard you're a game developer with an impressive repetoire, am I right?"

    clove "Um, not sure if that's how I'd put it... what's your name?"

    allen "Ah, how rude of me."

    "{i}AI time. Only click once and wait patiently for the responses to load!"

    python:
        import chatgpt1
        from apikey import openai_api_key

        api_key=openai_api_key

        #The "system" message is the initial prompt of your NPC
        #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
        messages = [
            {"role": "system", "content": "First, play the character of Clove, a 26-year-old smart and witty game developer who was recently laid off from his company, Hundred. You've been persuaded by a man named Aye the other day to help work on this new 'exciting project' to help build a new video game, but in reality, it's just Snakes and Ladders for the PC. You're baffled as to why you're being offered a million dollars to build a Snakes and Ladders video game, but you already signed the contract and decided to earn the money. Today's your first day, and you're at the ground floor to meet the manager, Allen, who you suspect has ulterior motives. You're skeptical of the project intentions and curious as to why you'd be paid so much money for just a luck-based video game. In 35 words or less, provide perfect dialogue responses to while acting as Clove."},
            {"role": "assistant", "content": "And who might you be?"}
        ]

        while True:
            if len(messages) % 2 == 0:
                # Switch from Clove to Enpa
                messages.append({"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're pretending to be kindhearted and selfless, but in reality, you're a racist old fart who buys women and holds sex parties for other rich people. You're racist and dislike minorities, but pretend you don't care. You're hiring people to help build a new real life game of Snakes and Ladders, and you're guiding people (game developers and AR researchers) who you're just meeting at the ground floor of a secret office to their new secret floors where they can work on this project in private. You're rewarding them a million dollars to complete this game within one month. You like to fake acting happy, but you have dark intentions - you plan to use the completed project to one day trap all minorities who live in the city of Aequalis (The city of this fictional setting) in a real-life game of Snakes and Ladders, which is the game you hired people to help you build. Keep your response to a max of 35 words, but make sure the sentences are not cut off."})
            else:
                # Switch from Enpa to Clove
                messages.append({"role": "system", "content": "Play the character of Clove, a 26-year-old smart and witty game developer who was recently laid off from his company, Hundred. You've been persuaded by a man named Aye the other day to help work on this new 'exciting project' to help build a new video game, but in reality, it's just Snakes and Ladders for the PC. You're baffled as to why you're being offered a million dollars to build a Snakes and Ladders video game, but you already signed the contract and decided to earn the money. Today's your first day, and you're at the ground floor to meet the manager, Allen, who you suspect has ulterior motives. You're skeptical of the project intentions and curious as to why you'd be paid so much money for just a luck-based video game. In 35 words or less, provide perfect dialogue responses to while acting as Clove."})

            messages = chatgpt1.completion(messages=messages, api_key=openai_api_key)
            response = messages[-1]["content"]
            
            # Extract and store the role-specific responses
            if len(messages) % 2 == 0:
                allen("[response]")
            else:
                clove("[response]")

            messages.append({"role": "user", "content": response})

            if len(messages) > 14:   # Stop conversation after 4 rounds
                break

    clove "Hmm. Fine, let's just go. You said I'm on a secret floor? I don't recall this building having a secret floor."

    allen "You'll see soon enough, young blood. Now follow me!"

    "And that's the end of this demo!"
return
    # This ends the game.