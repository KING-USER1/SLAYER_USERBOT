# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import os
import time
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME, CMD_HELP, StartTime, topfunc
from userbot.Config import Var
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, edit_or_reply, sudo_cmd

ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
if ALIVE_PIC is None:
    PM_iMG = "https://telegra.ph/file/8893e4a7a54a4d2c6ba91.jpg"
else:
    PM_iMG = ALIVE_PIC


HELL_PIC = os.environ.get("HELL_PIC", None)
if HELL_PIC is None:
    HELL_IMG = "https://telegra.ph/file/8893e4a7a54a4d2c6ba91.jpg"
else:
    HELL_IMG = HELL_PIC

CAT_IMGE = os.environ.get("CAT_IMGE", None)
if CAT_IMGE is None:
    CAT_IMG = "https://telegra.ph/file/8893e4a7a54a4d2c6ba91.jpg"
else:
    CAT_IMG = CAT_IMGE

version = "4.5"
python_version = "3.8.5"
catversion = "3.0"
ALIVE_MSG = Config.ALIVE_MSG or "ā® MY BOT IS RUNNING SUCCESFULLY ā®"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ā„ "
hellversion = "7.0"
# š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤š¤
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SLAYER āĪ¹gŠ½ŃĪ·Ī¹Ī·g"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)

# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(lightning_cmd(outgoing=True, pattern="alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "š„š„SLAYER šš ššššš„š„\n"
        pm_caption += f"               __ā¼š¼š°ššš“šā__\n**      ć{DEFAULTUSER}ć**\n\n"
        pm_caption += "ššššš             : [ā”COBRAā”](@KING_COBRA_TERABAAP)\n" 
        pm_caption += "šššššššš ššššššš : 1.17.5\n"
        pm_caption += "ššššššš ššššššš  : [į“į“ÉŖÉ“](https://t.me/KING_COBRA_TERABAAP)\n"
        pm_caption += "ššššššš ššššš    : [į“į“ÉŖÉ“](https://t.me/SLAYER_OFFICIAL_CHANELL)\n"
        pm_caption += "šššš ššššš       : [šLAYER](https://t.me/SLAYER_USERBOT_SUPPORT_TEAM)\n\n"
        pm_caption += "[ź·źįźź¦ź© ź©ź¦źźŖ ź¦źź¤ źźź¦źźź](https://github.com/KING-USER1/SLAYER_USERBOT)\n"
        await salive.get_chat()
        await salive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(
            salive.chat_id, ALIVE_PHOTTO, caption=pm_caption, link_preview=False
        )
        
