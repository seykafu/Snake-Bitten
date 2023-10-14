define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act3b:

    nvl clear

    "{i} One week later..."

    scene lab with fade
    show enpa happy at right
    with moveinright

    enpa "Morning."

    others "Morning Ms. Cantakan."

    enpa "{i}It's been a week since I've started... the work in creating this real-life AR game is harder than I imagined."
    enpa "What's our current status on the design of the tile?"

    others "Coming along well. We've implemented the digital software GUI and established the touch screen. Now we have to fix the dice to make it float."

    enpa "Good. As your project lead, I expect any potential issues or blockers to be reported to me immediately. Understood?"

    others "Yes, ma'am."

    enpa "{i}I can't believe that Allen man hired so many people for this project but made me the project lead. It didn't say anywhere on that contract about how many people would work under me."

    show samantha at left
    with moveinleft

    "A feint shadow emerged from the other door across the lab. Enpa, despite her focus, darted her eyes to the door and stood up from her rolling chair."

    enpa "Who are you? What are you doing here?"

    samantha "..."

    enpa "..."

    "The two stared at each other with stoic faces. Enpa, crossing her arms, waited in her spot for the woman to respond. Everyone else in the lab stopped their work to watch."

    samantha "So you're the project lead - Enpa?"

    enpa "Yes, but please answer my questions."

    "{i}AI time. It'll take a few seconds to load responses. Only click once to proceed."

    python:
            import chatgpt1

            #The "system" message is the initial prompt of your NPC
            #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
            messages = [
                {"role": "system", "content": "Play the character of Samantha, a thirty-year-old woman who used to be a chess grandmaster. Because of the current misogynistic society that's developed in the past few years, you were forced to give up your title and become a servant for male millionaires. One day, you overheard the boss of a prestigious gaming company called 'Hundred' talking about a grand project that will turn the old 'Snakes and Ladders' game into a real-life simulation. You snuck into the lab one day (you have access because of your sexual relationship with the superiors) and encountered a woman named Enpa who's working on the project. You know about the secrets of her project even though she doesn't, and you try to indirectly tell her to stop the project, otherwise everyone's lives' are in danger. You also act stubborn and rude. Keep your response to a max of 35 words."},
                {"role": "assistant", "content": "And who might you be?"}
            ]

            while True:

                #Then add it in the "history" of messages
                content = "What's your name and why are you here?"
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
                samantha("[response]")
            
                messages = [
                    {"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred. The reason why you were laid off was because you were being racist toward a colleague. You're quite arrogant and spoilted, and you think you deserve better. You're currently working on a revolutionary AR game that will turn the old 'Snakes and Ladders' board game into a real-life simulation. You're in the lab working with your team to finish the project, as you will earn a million dollars upon completion. You see a woman walk into your lab without permission, so you ask her who she is and why she showed up. Act stoic and guarded. keep your answer to less than 30 words."},
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
                    {"role": "system", "content": "Play the character of Samantha, a thirty-year-old woman who used to be a chess grandmaster. Because of the current misogynistic society that's developed in the past few years, you were forced to give up your title and become a sex worker for male millionaires. One day, you overheard the boss of a prestigious gaming company called 'Hundred' talking about a grand project that will turn the old 'Snakes and Ladders' game into a real-life simulation. You snuck into the lab one day (you have access because of your sexual relationship with the superiors) and encountered a woman named Enpa who's working on the project. You know about the secrets of her project even though she doesn't, and you try to indirectly tell her to stop the project, otherwise everyone's lives' are in danger. You also act stubborn and rude. Keep your response to a max of 35 words."},
                    {"role": "assistant", "content": "And who might you be?"}
                ]

                #Then add it in the "history" of messages"
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
                samantha("[response]")

                messages = [
                    {"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred. The reason why you were laid off was because you were being racist toward a colleague. You're quite arrogant and spoilted, and you think you deserve better. You're currently working on a revolutionary AR game that will turn the old 'Snakes and Ladders' board game into a real-life simulation. You're in the lab working with your team to finish the project, as you will earn a million dollars upon completion. You see a woman walk into your lab without permission, so you ask her who she is and why she showed up. Act stoic and guarded, and don't listen to her. keep your answer to less than 30 words."},
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
                    {"role": "system", "content": "Play the character of Samantha, a thirty-year-old woman who used to be a chess grandmaster. Because of the current misogynistic society that's developed in the past few years, you were forced to give up your title and become a sex worker for male millionaires. One day, you overheard the boss of a prestigious gaming company called 'Hundred' talking about a grand project that will turn the old 'Snakes and Ladders' game into a real-life simulation. You snuck into the lab one day (you have access because of your sexual relationship with the superiors) and encountered a woman named Enpa who's working on the project. You know about the secrets of her project even though she doesn't, and you try to indirectly tell her to stop the project, otherwise everyone's lives' are in danger. You also act stubborn and rude. Keep your response to a max of 35 words."},
                    {"role": "assistant", "content": "And who might you be?"}
                ]

                #Then add it in the "history" of messages"
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
                samantha("[response]")
                break

    enpa "So are you going to leave or what? You clearly don't belong here."

    samantha "Listen. Stop this entire project and run for your life. Please."

    enpa "Again, I haven't a clue what you're talking about. Why do you want us to stop?"

    samantha "Look, I know you're being compensated for all of this and you're under contract. But please hear me out. This game you're building... it's going to be-"

    "{i}SLAM!!!"

    stop music fadeout 0.5

    "The entrance door flung open after a ferocious kick. In stormed two guards dressed in all black and grey."

    "Without even a chance to react, Samantha had her arms constrained behind her and handcuffed within seconds."

    play music "horror.mp3" fadein 1.0

    samantha "H-Hey! Stop it! Let go of me!"
    extend " Look, I promise to leave after, but please just-"

    hide samantha with moveoutleft

    "Samantha's voice froze as one of the guards injected a syrum into her neck using a needle."

    enpa "...!"

    "Without batting an eye or turning heads, the guards hurried away with Samantha through the door where they barged in from. Everyone in the lab, including Enpa, stood there in shock."

    enpa "{i}D-Did the guards need to go that far to stop an intruder like her?!"

    enpa "{i}Why was she trying to tell me to quit the project?"

    "A million questions clouded her mind; even as the time passed, she could barely continue her tasks for the day."

    scene black with dissolve

    stop music fadeout 0.5

    play music "saving.mp3" fadein 1.0

    "{i} Two weeks later"
    
    nvl clear

    scene lab with fade
    show enpa happy at right
    with moveinright

    "With only a week left in her project timeline, things were looking bright. Enpa had since shook away the event with Samantha from a few weeks back."

    "She wandered around the lab during her lunch break, unable to stop thinking about the million dollars she'll earn once the project's completed. It was just her in the lab today as everyone was out eating."

    enpa "{i}I'll use that million dollars to start my own research company, and only hire minorities. That'll show those idiots at Hundred how pathetic their company values are!"

    "{i}Knock knock!"

    "Her own voice almost made her miss the gentle tapping against the door."

    "Enpa blushed and slapped her cheeks, frustrated to have spoken her thoughts out loud."

    enpa "Come in."

    "In came Allen with a smile even larger than hers."
    
    "Enpa frowned immediately."

    show allen at left
    with moveinleft

    allen "Things are coming along perfectly! I have to say, Ms. Enpa. There couldn't have been a better candidate than you for this job."

    enpa "Hmm."

    allen "You seem displeased. Anything the matter?"

    enpa "Say, this may be late to ask, but why are you so interested in a real-life Snakes and Ladders game? Do you really expect anyone to play a luck-based game?"

    allen "..."

    "Allen turned around, facing his back to her. His hands were held tightly behind him; Enpa could only imagine his eyes closed deep in thought."

    allen "Actually, your question has impeccable timing. Do you mind following me to another floor? I'd like to show you something, and it won't take more than a few minutes."

    "Enpa normally would've declined, but with the curiousity that has built up thanks to Allen's mysterious behavior, she folded her arms and nodded."

    enpa "Fine."

    allen "Excellent, please follow me to the elevator, we're headed to the thirteenth floor."

    nvl clear

    jump act4b