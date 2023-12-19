# Thurston Autogen

This python script will create an interactive [Teachable chat Agent](https://microsoft.github.io/autogen/blog/2023/10/26/TeachableAgent) designed to save the user's life lessons, values, memories and other important details.

⚠️ THIS WILL STORE SENSITIVE DATA ABOUT THE USER.  This includes PII, names, dates, places and other information that can be used in identity theft.

This is just a prototype and is intended to be used locally on a secure computer.

## Usage

Once you have completed the Setup steps below, simply start the chat by running `python3 main.py`.

To Exit the Chat type `exit`. This will analyze the conversation and save the relevant parts.


## Setup

*Note to self: Always use `python3` and `pip3` commands.*

#### 1. Set up the venv

`python3 -m venv venv`

#### 2. Activate venv

`source ./venv/bin/activate`

#### 3. Install requirements

`pip3 install -r requirements.txt`

#### 4. Set your OpenAI API Keys
- rename `OAI_CONFIG_LIST.sample` to `OAI_CONFIG_LIST` and fill in your API keys.

#### 5. Deactivate venv when you're done.

`deactivate`

## Resources

- Autogen's [TeachableAgent](https://microsoft.github.io/autogen/blog/2023/10/26/TeachableAgent)
- Teachable Agent Overview Tutorial: [YouTube](https://www.youtube.com/watch?v=KDpGN7QDEVk) -  [github](https://gist.github.com/langecrew/a5620c686790567442b6eb4060f0306d)
- Custom Agents Tutorial: [YouTube](https://www.youtube.com/watch?v=QaJ-mv3LJa4) - [github](https://gist.github.com/langecrew/b9f6a24aba6d47a9888ad7abed8220ee)


## Props

Great tutorials by Andy Smith ([@langecrew](https://gist.github.com/langecrew) on github and [@andymccool](https://www.youtube.com/@andymccool) on YouTube)
