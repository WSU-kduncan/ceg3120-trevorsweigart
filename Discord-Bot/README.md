# Setup

- Dependencies:
  - python3
  - pip3
  - discord.py

# API Token:
- In the bot page in the Discord Developer Portal:
  - Enable "Message Content Intent"
  - Press "Reset Token" at the top of the page
  - Copy the given Token
  - Paste the token in the `.env` file where the bot will be running

# Usage:

- Users are able to type `!spongequote` in Discord
  - This will make the bot respond with a quote from Spongebob

# Research:
- The bot will only stay running while the code is running
  - This means there has to be a computer running at all times to use the Discord Bot
- A solution is to host the bot on a server that runs 24/7
  - This means there won't be many ways people can accidently mess with it 
  - If the server is a cloud server (such as AWS), this means that you just have to start a cloud process and you can manage everything online
  - Using AWS' autoscaling will also allow the bot to just use the resources it needs and scale to have more resources if there are lots of people using it

