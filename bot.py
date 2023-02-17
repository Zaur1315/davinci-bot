from aiogram import Dispatcher, Bot, executor, types
from config import openAI_key, telegram_key
import openai

bot = Bot(token=telegram_key)
dp = Dispatcher(bot)

openai.api_key = openAI_key


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Добро пожаловать, {message.from_user.first_name}. Я постараюсь быть интересным собеседником.')

# print(response['choices'][0]['text'])


@dp.message_handler()
async def bot_answer(message: types.Message):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    await message.answer(response['choices'][0]['text'])

if __name__ == '__main__':
    executor.start_polling(dp)
