import numpy as np
import time
import MediaKeys
import requests
import json


API_GET_ADDRESS = "http://localhost:8180/crest2/v1/api?gameStates=true"
target_game_state = 2
target_race_state = 2


previously_racing = False

while True:
    
    response = requests.get(API_GET_ADDRESS)

    if not response:
        #raise Exception(f"Non-success status code: {response.status_code}")
        print("could not get AMS2 information")
        print("retrying in 5 seconds...")
        time.sleep(5)
        continue

    resp_dict = json.loads(response.text)
    game_state = resp_dict['gameStates']['mGameState']
    race_state = resp_dict['gameStates']['mRaceState']

    if game_state == target_game_state and race_state == target_race_state:
        
        if not previously_racing:
            # toggle media
            print("NOW RACING")
            print("toggling media")
            MediaKeys.PressKey(MediaKeys.VK_MEDIA_NEXT_TRACK)
            MediaKeys.PressKey(MediaKeys.VK_MEDIA_PLAY_PAUSE)

        previously_racing = True

    else:
        
        print("not racing")

        if previously_racing:
            # toogle media
            print("toggling media")
            MediaKeys.PressKey(MediaKeys.VK_MEDIA_PLAY_PAUSE)
        
        
        previously_racing = False
        
    print("-----")

    time.sleep(5)
