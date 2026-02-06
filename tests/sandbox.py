import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from core.brain import generate_reply

print(generate_reply("bhai kya kar raha hai"))
