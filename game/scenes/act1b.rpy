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

            #The "system" message is the initial prompt of your NPC
            #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
            messages = [
                {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company called 'Hundred Studios' in a fictional country called Aequalis. You're pretending to be kindhearted and selfless, but in reality, you're a racist old fart who buys women and holds sex parties for other rich people. You're racist and dislike minorities, but pretend you don't care. You're trying to persuade a woman named Enpa to build a new 'AR tool' that can revolutionize the next video game. Keep your response to a max of 30 words."},
                {"role": "assistant", "content": "And who might you be?"}
            ]

            while True:

                #Then add it in the "history" of messages
                content = "Hello, Enpa speaking, who is this on the phone? How did you get my number?"
                messages.append(
                    {"role": "user", "content": content}
                    
                )

                if apikey != '':
                    #We ask ChatGPT to "complete" the conversation by adding a response
                    #If you have an API key, let's use that
                    messages = chatgpt1.completion(messages,api_key=apikey)
                else :
                    messages = chatgpt1.completion(messages,openai_api_key)

                #Here we only care about the response from the NPC
                response = messages[-1]["content"]
                #So we display just that
                allen("[response]")
            
                messages = [
                    {"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred Studios. The reason why you were laid off was because you were being racist toward a colleague. You're quite arrogant and spoilted, and you think you deserve better. Someone just called you, asking for you to join their project. Decline and keep your answer to less than 20 words."},
                    {"role": "assistant", "content": "And who might you be?"}
                ]

                #Then add it in the "history" of messages
                messages.append({"role": "user", "content": response})

                if apikey != '':
                    #We ask ChatGPT to "complete" the conversation by adding a response
                    #If you have an API key, let's use that
                    messages = chatgpt1.completion(messages,api_key=apikey)
                else :
                    messages = chatgpt1.completion(messages,openai_api_key)

                #Here we only care about the response from the NPC
                response = messages[-1]["content"]

                enpa("[response]")

                messages = [
                {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're pretending to be kindhearted and selfless, but in reality, you're a racist old fart who buys women and holds sex parties for other rich people. You're racist and dislike minorities, but you act like that's not the case. You're currently trying to persuade a woman named Enpa to build a new 'AR tool' that can revolutionize the next video game. Keep your responses to a max of 35 words every time."},
                {"role": "assistant", "content": "And who might you be?"}
            ]
                #Then add it in the "history" of messages
                content = "Hello, Enpa speaking, who is this on the phone? How did you get my number?"
                messages.append(
                    {"role": "user", "content": response}
                    
                )

                if apikey != '':
                    #We ask ChatGPT to "complete" the conversation by adding a response
                    #If you have an API key, let's use that
                    messages = chatgpt1.completion(messages,api_key=apikey)
                else :
                    messages = chatgpt1.completion(messages,openai_api_key)

                #Here we only care about the response from the NPC
                response = messages[-1]["content"]
                #So we display just that
                allen("[response]")

                messages = [
                    {"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred. You're quite arrogant and spoiled, and you think you deserve better. Someone just called you, asking for you to join their project. You declined, but they're persistent on taking you in. Act annoyed as you decline again. Keep your answer to less than 30 words."},
                    {"role": "assistant", "content": "And who might you be?"}
                ]

                #Then add it in the "history" of messages
                messages.append({"role": "user", "content": response})

                if apikey != '':
                    #We ask ChatGPT to "complete" the conversation by adding a response
                    #If you have an API key, let's use that
                    messages = chatgpt1.completion(messages,api_key=apikey)
                else :
                    messages = chatgpt1.completion(messages,openai_api_key)

                #Here we only care about the response from the NPC
                response = messages[-1]["content"]

                enpa("[response]")

                messages = [
                {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're currently trying to persuade a woman named Enpa to build a new 'AR tool' that can revolutionize the next video game, but she declines. Threaten her by claiming you know her darkest secret which will be exposed if she doesn't join. Keep your response to less than 35 words."},
                {"role": "assistant", "content": "And who might you be?"}
            ]
                #Then add it in the "history" of messages
                content = "Hello, Enpa speaking, who is this on the phone? How did you get my number?"
                messages.append(
                    {"role": "user", "content": response}
                    
                )

                if apikey != '':
                    #We ask ChatGPT to "complete" the conversation by adding a response
                    #If you have an API key, let's use that
                    messages = chatgpt1.completion(messages,api_key=apikey)
                else :
                    messages = chatgpt1.completion(messages,openai_api_key)

                #Here we only care about the response from the NPC
                response = messages[-1]["content"]
                #So we display just that
                allen("[response]")

                break

    enpa "What?! You... How could you know such a-"

    allen "Listen, besides keeping your secret, I'm also willing to award you a million dollars to join my project. It'll be a full-time commitment for about a month. You'll be free and rich after that."

    enpa "..."

    enpa "Okay, fine I'll consider it. Is there a time and date when I should meet you? And where?"

    allen "Twelve O'clock tomorrow at Hundred Studios building four. That work for you?"

    enpa "Yes."

    stop music fadeout 1.0

    "As Enpa wrapped up her bizarre call, she continued home with continued mixed feelings about the arrangement."

    jump act2b
