from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyqiwip2p import QiwiP2P
TOKEN = ''# token your bot
PAYMENTS_TOKEN=''
p2p= QiwiP2P(auth_key=PAYMENTS_TOKEN)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot,storage=MemoryStorage())


