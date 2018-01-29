#! python3
import webbrowser, sys, pyperclip


sys.argv #['mapit.py', '870', 'Valencia', 'St.']
#Check if command line arguments were passed
if len (sys.argv) > 1:
    #['mapit.py', '870', 'Valencia', 'St.']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# http://www.google.com/maps/place
webbrowser.open('http://1337x.to/sort-search/'+address+' 1080p/time/desc/1/')
