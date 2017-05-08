# CTF-MCPy
A script to create geofenced traps in Minecraft using the RaspberryJuice API and Python.

tracker.py is the main Python script. First it pulls a red and blue dictionary from the whitelist module that contains the players' Minecraft entity ID and Vec3 location (an x,y,z coordinate from the Minecraft Python API.) At the top it creates the trap objects that have x,y,z and trap name variables. 

The while True loop updates the location of each player, then checks each player against the opposing team's traps with the checkGeoFence function. This is the step I'm looking to speed up with either multithreading or multiprocessing. If the player is within the trap's boundaries, then the trap is activated by the trapQueen module. 
