define config.rollback_enabled = False

init python:
    #import npc
    import chatgpt1
    from apikey import openai_api_key

# The script of the game goes in this file.

# The game starts here.

label act2b:

    nvl clear

    play music "upbeat_corporate.mp3" fadein 1.0

    scene office_lobby with fade
    show enpa happy at right
    with moveinright

    enpa "{i}Allen told me it was in this building on the first floor..."
    extend "{i}I've never been to this building before. I almost forgot it even existed."

    allen "Enpa!"

    show allen at left
    with moveinleft

    allen "Welcome to Building Four. Must be your first time here based on your expression."

    enpa "Yes, I never even knew this place existed until I searched it up."

    "Allen chuckled and crossed his arms."

    allen "Well anyway, we won't keep you here too long for today. Please come over here to this counter."

    "Enpa cautiously followed Allen from behind."

    "Once they arrived at the counter where the wooden front desk sat, Allen pointed to a set of documents." 

    allen "Please read these documents for ten minutes, and sign if everything looks okay."

    enpa "I only get ten minutes to read them?"

    allen "That's all you'll need. I'll be back."

    hide allen with moveoutleft

    enpa "{i}What's stopping me from running away-"

    "Her eyes widened as they darted to the entrance from which she came from. Two tall guards dressed in all black - one male and another female  - stood on both sides of the door."

    enpa "{i}You're kidding me...doesn't this count as holding someone hostage???"

    "She glared down at the papers and began reading."

    scene paper_on_desk with fade

    "{i}Enpa Cantakan will hereby commence her temporary contract-based employment at Hundred Studios Inc. for 30 days upon the date of her signing."
    "{i}She will work on a secret AR-based project for Hundred's next large game and report to supervisor Mr. Allen Walsh."
    "{i}Upon the completion of her contract, if the project deliverable suffices to the supervisor's standards, the conditional compensation will be $1,000,000."
    "{i}This project involves the development of a real-life version of the original 'Snakes and Ladders' board game, with a few modifications."

    "Enpa glimpsed at the remaining papers, but didn't catch anything suspicious. In fact, the other documents were the same as the ones from her original employment."

    enpa "{i}There has to be something weird about this contract...why do they want to build a 'Snakes and Ladders' game? Isn't that a kids board game?"

    "She insepcted the paper one final time. Still nothing disturbing."

    enpa "{i} So if they don't give me my million dollars after my project completion, I'll just sue them."

    scene office_lobby with fade

    "Soon thereafter, Allen returned with a resting smile."

    show allen at left
    with moveinleft

    allen "Alright, I'm back. Any concerns?"

    show enpa happy at right
    with moveinright

    enpa "So can I sue the company if I don't get my million dollars?"

    "{i}AI time. It'll take a few seconds to load responses. Only click once to proceed."

    python:
            import chatgpt1
            from apikey import openai_api_key

            api_key=openai_api_key

            #The "system" message is the initial prompt of your NPC
            #Messages with "assistant" are messages from the NPC, here there's a first message so we add it to the list of messages already said by the NPC
            messages = [
            {"role": "system", "content": "Play the character of Allen, a 60-year-old executive of a billion dollar gaming company in a fictional country called Aequalis. You're pretending to be kindhearted and selfless, but in reality, you're a racist old fart who buys women and holds sex parties for other rich people. You're racist and dislike minorities, but pretend you don't care. You're trying to persuade a woman named Enpa to build a new 'AR tool' that can revolutionize the next video game. You offered her a million dollars if she completes the project in time (1 month). Keep your response to a max of 30 words."},
            {"role": "assistant", "content": "And who might you be?"}
            ]

            while True:

                #Then add it in the "history" of messages
 
                if len(messages) < 7:
                     content = "So can I sue the company if I don't get my million dollars?"
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
                messages.append({"role": "system", "content": "Now play the character of Enpa, a 27-year-old game developer who was recently laid off at his company, Hundred Studios. The reason why you were laid off was because you were being racist toward a colleague. You're quite arrogant and spoilted, and you think you deserve better. You're interested in a project proposal with your former company because they're offering you a million dollars. They want you to build an 'AR tool' that will help enable a real-life version of Snakes and Ladders. Act stoic and guarded. Ask a few questions to Allen, the director at Hundred Studios. Keep your answer to less than 30 words."})
                messages.append({"role": "user", "content": response1})
    
                messages = chatgpt1.completion(
                messages=messages,api_key=openai_api_key
                )

                response2 = messages[-1]["content"]
            
                messages.append({"role": "user", "content": response2})
                
                enpa("[response2]")

                if len(messages) > 10:   # Stop conversation after 4 rounds
                    break

    enpa "Also, about that secret of mine...you don't plan to ever-"

    allen "Of course not. We at Hundred know better than to ever reveal such a thing, so long as you comply with our project needs."

    enpa "Hmm... When does it start?"

    "A beaming smile engulfed Allen's face."

    allen "Now."

    jump act3b
