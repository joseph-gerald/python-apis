from dotenv import load_dotenv

import blocksmc
import os

load_dotenv()

USERNAME = os.getenv('MCUSERNAME')
HASH = os.getenv('HASH')

blocksmc = blocksmc.BlocksMC(USERNAME, HASH)

player = blocksmc.getPlayer("BusinessManBob")

print(player.display_data())