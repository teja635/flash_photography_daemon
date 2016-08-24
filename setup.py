import os

os.system("curl http://mozilla.mirrors.tds.net/pub/mozilla.org/firefox/releases/latest/mac/en-US/Firefox%2025.0.1.dmg -o firefox25.dmg
")
os.system("hdiutil attach firefox25.dmg")
os.system("cd /Volumes/Firefox")
os.system("cp Firefox.app /Applications/Firefox.app")
os.system("hdiutil detach /Volumes/Firefox")

os.system("pip install selenium")
os.system("pip install pillow")