# Incordnito
A discord bot and webhooker written in Python converted to a Windows .EXE that allows to send and read end to end encrypted messages allowing for privacy inside Discord servers with the ability to generate and share keys to communicate with true privacy!

Thank you for trying Incordnito, if you discover any errors of
relevance, please report them on the github!
--------------------------------------------
Instructions:

Add this bot to your server:
----------------------------
https://discord.com/api/oauth2/authorize?client_id=704770027387093024&permissions=8&scope=bot

If you delete a single file (other than this file, "instructions.txt"),
the program will error on launch.  Do not delete a single one.

"background.png" is the background image, the program will error and crash
automatically on start if this is deleted.  Custom background images will
be added in V1.1 (next update), so keep your eyes on the github.
----------------------------------------------------------------
How to use:

You need to have proper permissions to create a channel webhook.  If you
can, make a webhook for the channel of your choosing, and copy the link
and paste it in "link.txt" and save it.

Choose a name for yourself and put it in "nickname.txt" and save it.

To communicate with others using this tool, send them (over Discord, to be
safe, there is no reason to accept it from elsewhere, it will work
perfectly over Discord) your "key.txt" and have them replace it inside
their Incordnito directory.

WARNING:

If you click the "Generate Key" button, you will have to redo this!
----------------------------
DO NOT MESS WITH "key.txt"!:
----------------------------

When you launch "Incordnito.exe", you are able to click the "Generate
Key" button, this is the key that your encrypted messages are encrypted
with.  

Meaning, without this key, no one can access or see what was said
in your messages.  

DO NOT share this key with anyone that you do not trust
or want to see your messages.

When you click the "Generate Key" button, it will automatically put
your generated key inside "key.txt".

The way Incordnito is programmed does not accept custom keys for the
security reason being "key cracking".
This would be a case in which a person of interest would
be able to run a program that would constantly test tons of keys until
they find the one that works.
-----------------------------
"runCount.txt" is used to detect if the program has been run, do not delete this, it will regenerate your key.
-------------------------------------------------------------------------------------------------------------
Enjoy!
