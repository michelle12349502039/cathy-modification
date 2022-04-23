import os
from os import environ
from cathy import Cathy

def main(): 
  bot = Cathy(os.getenv("CHANNEL"), os.getenv("TOKEN"), os.getenv("DATABASE"))
  bot.run()

main()
