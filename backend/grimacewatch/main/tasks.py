from datetime import datetime
import time

from additional.helpers import PAIR_DATA
from .models import History, Tokens

from huey import crontab
from huey.contrib.djhuey import task, periodic_task, db_task, on_commit_task
from dexscreener import DexscreenerClient

def tprint(s, c=32):
    # Helper to print messages from within tasks using color, to make them
    # stand out in examples.
    print('\x1b[1;%sm%s\x1b[0m' % (c, s))

@periodic_task(crontab(minute='*/1'))
def every_other_minute():
    client = DexscreenerClient()
    pair = client.get_token_pair("dogechain", "0x1aAD352a2190B399Bb3cfD4d5E4B0bf6EFA33C0e")
    Tokens.objects.create(
                name="GRIMACE",
                price=pair.price_usd
            )
    for (name, info) in PAIR_DATA.items():
        pair = client.get_token_pair("arbitrum", info)
        Tokens.objects.create(
                name=name,
                price=pair.price_usd
            )

    
    # tprint('This task runs every 1 minutes.', 35)