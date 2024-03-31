@ECHO OFF

ECHO Starting ASM2...
"C:\Program Files (x86)\Steam\steamapps\common\Automobilista 2\AMS2.exe"

ECHO Starting Automobilista CREST2 API server...
start .\CREST2-AMS2\CREST2.exe -multiwindow

ECHO Starting media key activator...
start python .\main.py -multiwindow



PAUSE