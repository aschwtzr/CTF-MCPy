# CTF-MCPy
A program to create geofenced traps in Minecraft using the RaspberryJuice API and Python.

Install the RaspberryJuice server and API from https://www.nostarch.com/programwithminecraft.

Make sure you're using the latest version of the RaspberryJuice API! Find it here: https://github.com/shawill/py3minepi

Place the Capture The Flag directory in the root server folder.
Start the server and in a separate process run tracker.py with python3.
Use settings.py to set up the game, including the player names and traps.
Update trapManager to match the settings file. Once you're ready,

The while True loop updates the location of each player, then checks each player against the opposing team's traps. Some traps from the Game Bahrain program are included! 
