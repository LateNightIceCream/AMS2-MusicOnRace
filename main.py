import time
import requests
import json

import asyncio

from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_session():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if not current_session:
        return None
    return current_session


API_GET_ADDRESS = "http://localhost:8180/crest2/v1/api?gameStates=true"
TARGET_GAME_STATE = 2
TARGET_RACE_STATE = 2
POLL_INTERVAL_SECS = 5

previously_racing = False

while True:
    
    response = requests.get(API_GET_ADDRESS)

    if not response:
        print("could not get AMS2 information")
        print("retrying in 5 seconds...")
        time.sleep(5)
        continue

    resp_dict = json.loads(response.text)
    game_state = resp_dict['gameStates']['mGameState']
    race_state = resp_dict['gameStates']['mRaceState']


    if game_state == TARGET_GAME_STATE and race_state == TARGET_RACE_STATE:
        
        if not previously_racing:
            print("NOW RACING")
            print("starting media")
            session = asyncio.run(get_media_session())
            if session:
                # session.try_skip_next_async()
                session.try_play_async()

        previously_racing = True

    else:

        print("not racing")

        if previously_racing:
            print("pausing media")
            session = asyncio.run(get_media_session())
            if session:
                session.try_pause_async()
        
        previously_racing = False
        
    print("-----")

    time.sleep(POLL_INTERVAL_SECS)
