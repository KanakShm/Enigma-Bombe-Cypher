# Enigma-Bombe-Cypher

To encrypt all files in the working directory run python3 main.py. This will encrypt files with the Enigma code.

To run ONLY the Enigma machine enter python3 EnigmaMachine.py

This will generate a new Enigma machine where you are able to enter a string
and it will encrypt it. It will also show the current rotor and plugboard settings. You are then able to send these settings to your friend who can initialise a new Enigma machine (current system design of the project allows multiple types of object instantiation) and will be able to decrypt your message.

To decrypt files using the Bombe machine run python3 BombeMachine.py and give it two arguments, the plain-text and the cypher-text. This process will take roughly 20-30 min and will have threads running in parallel.
