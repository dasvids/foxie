import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

TOKEN: Final = os.getenv('DISCORD_API_TOKEN')