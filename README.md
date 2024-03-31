# AMS2-MusicOnRace
This is a script for Automobilista 2 based on [CREST2-AMS2](https://github.com/viper4gh/CREST2-AMS2). 
It will virtually trigger the media keys to play or pause the currently playing media when a race starts or is paused/stopped, respectively. 
The source bould be e.g. YouTube, Spotify, or local music.


## Setup
1. Download this repo's source
2. Download [CREST2-AMS2](https://github.com/viper4gh/CREST2-AMS2) and unzip it inside the root folder


## Usage

Since there is (unfortunately) only one media key for playing and pausing, we can only toggle the media state.
This means that before the start of the race/script the media you want to play (e.g. YouTube) should be PAUSED.
Otherwise it will be paused when the race starts.
(Maybe there is some way in windows to find out if some media is currently playing, this is a TODO)

### Batch Script / Automatic
You can use the batch script `run_ams2.bat` to automatically start the script along with the CREST2 server
and Automobilista 2.

### Manual Start
Start the CREST2-AMS server and then just run `python .\main.py` from cmd or powershell while inside the
repo directory.


## TODO
- CLI arguments
- eliminate toggle by detecting current media state


## Thanks to
- viper4gh for CREST2-AMS2
- rpetrik for MediaKeys
