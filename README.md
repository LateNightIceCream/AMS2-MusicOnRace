# AMS2-MusicOnRace
This is a script for Automobilista 2 based on [CREST2-AMS2](https://github.com/viper4gh/CREST2-AMS2). 
It will play or pause the currently playing media when a race starts or is paused/stopped, respectively. 
The source could be e.g. YouTube, Spotify, or local music.


## Requirements
- python > 3.8
  - `requests`
  - winsdk


## Setup
1. Download this repo's source
2. Download [CREST2-AMS2](https://github.com/viper4gh/CREST2-AMS2) and unzip it inside the root folder
3. Make sure to enable shared memory in the settings (see CREST2-AMS2)

## Usage

You can use it in one of these ways:

### Batch Script / Automatic
Run the batch script `run_ams2.bat` to automatically start the python script along with the CREST2 server
and Automobilista 2.

### Manual Start
Start the CREST2-AMS server and then just run `python .\main.py` from cmd or powershell while inside the
repo directory.


## TODO
- CLI arguments
- Eliminate polling and use shared memory directly (?), maybe this could be event based


## Thanks to
- viper4gh for CREST2-AMS2
- rpetrik for MediaKeys
