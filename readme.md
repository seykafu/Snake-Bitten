# Snake Bitten (Visual Novel Game)

Snake Bitten is a visual novel story which I've built using Ren'Py and leverages the OpenAI API (GPT-3.5) to experiment with back-and-forth character dialogue.

The VN features two main characters - Enpa and Clove, who both just got laid off from their respective jobs as game developers. Watch as their stories unfold in parallel and see the magic of GPT3.5 allowing my characters to converse with each other without any hard-coded dialogue!

![Snake Bitten](/game/gui/SB.png)

In this story, Enpa and Clove run into a unique opportunity by a mysterious man named Allen to build a new game - a real life version of "Snakes and Ladders" which features more dangerous implications than they initially expected. Play as either character in this multi-path visual novel demo while watching AI allow characters to talk to each other naturally in the dialogue!

Watch this first demo where you can interact with a character directly:
https://github.com/seykafu/Snake-Bitten/assets/35230390/554d6ccf-9cb4-4a42-980e-6d6752c4c19a

## Installation

There are two ways you can try my game or run my code. 
1) First, you can just visit my itch.io link: [Snake Bitten on Itch.io](https://seykafu.itch.io/snake-bitten)
As you'll see, you'll need to install ChatGPT locally before running my game, and borrow my API key (I have a limit of $5 until no more tokens can be processed - sorry hehe).

2. Just clone my repo and run the game using the Ren'Py engine! 
Make sure to perform the following instructions below before you run the game so you have access to the OpenAI API.

## Instructions to set up
1. Install Python 3.7 or later. You can download Python from the official website (https://www.python.org/) and follow the instructions to install it on your machine.
2. Install the OpenAI API client. You can do this by running the following command:
```bash
pip install openai
```

Set up an API key. To use the OpenAI API, you will need to sign up for an account and obtain an API key. You can sign up for an API key at the OpenAI website (https://beta.openai.com/signup/).

Create a new file titled "apikey.py" within the parent Snake Bitten directory and paste your API key into that file as a string while naming the string "openai_api_key":

```python
openai_api_key = "<insert API key here>"
```

## Contributing

I mean, fork and contribute to my game if you want or just create your own versions.
