### Anleitungen ###
# https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
# https://beta.openai.com/docs/guides/fine-tuning
# https://betterprogramming.pub/hello-codex-openai-gpt-3-telegram-bot-362d93ea6959
# https://help.openai.com/en/articles/5955604-how-can-i-solve-429-too-many-requests-errors

### generated models ###
# ada model > ada:ft-benita-2022-12-16-13-49-49
# curie model > curie:ft-benita-2022-12-21-15-41-46
# curie model V2 > curie:ft-benita-2023-01-24-14-33-22

# bot channel chat id @achtungpropaganda

import logging
import os
from dotenv import load_dotenv # if you dont have dotenv yet: pip install python-dotenv

import telegram
import telebot
import openai

import env

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

load_dotenv()
bot = telebot.TeleBot(env.telegram_KEY)
openai.api_key = env.OPENAI_API_KEY
channel_id = '@achtungpropaganda'

@bot.message_handler(func=lambda message: True)
def get_codex(message):
    response = openai.Completion.create(
        engine="curie:ft-benita-2023-01-24-14-33-22",
        prompt='"""\n{}\n"""'.format(message.text),
        temperature=1, # controls randomness, 0 = repetitive
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.5, # decreases model's likelihood to repeat the same line verbatim
        presence_penalty=0.5, # increases model's likelihood to talk about new topics
        stop=['"."'])

    #bot.send_message(message.chat.id,
    bot.send_message(channel_id,
    f'```python\n{response["choices"][0]["text"]}\n```',
    parse_mode="Markdown")


bot.infinity_polling()