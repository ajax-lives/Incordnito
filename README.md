# Incordnito
A discord bot and webhooker written in Python converted to a Windows .EXE that allows to send and read end to end encrypted messages allowing for privacy inside Discord servers with the ability to generate and share keys to communicate with true privacy!

Notice:  If anyone would like to try their hand at making a proper and well made tutorial on YouTube, I will credit them here and inside Incordnito, leave an issue letting me know if you would like to/already did.

Thank you for trying Incordnito, if you discover any errors of relevance, please report them on the github in an issue!
--------------------------------------------

Instructions:
----------------
Add this bot to your server:

https://discord.com/api/oauth2/authorize?client_id=704770027387093024&permissions=8&scope=bot

If you delete a single file (other than this file, "instructions.txt"),
the program will error on launch.  Do not delete a single one.

How to use:
----------------------------------------------------------------
You need to have proper permissions to create a channel webhook.  If you
can, make a webhook for the channel of your choosing, and copy the link
and paste it in "link.txt" and save it.

Choose a name for yourself and put it in "nickname.txt" and save it.

To communicate with others using this tool, send them (over Discord, to be
safe, there is no reason to accept it from elsewhere, it will work
perfectly over Discord) your "key.txt" and have them replace it inside
their Incordnito directory.

When you launch "Incordnito.exe", you are able to click the settings cog (the gear icon), this is at the bottom of 
the main program UI that opens when you launch Incordnito.  

When you click that, you will get a pop up window with a read only text box containing your key (future update will let you copy and paste keys into here, NO CUSTOM KEYS THOUGH >:C), then you can see the "Generate Key" button, this regenerates the key that your encrypted messages are encrypted with when you click it.  

The most efficient way to share keys is to send your "key.txt" file to whomever you would like to communicate with, DO NOT SHARE THIS INSIDE A SERVER WHERE OTHERS CAN SEE IT (if unintended).

Meaning, without this key, no one can access or see what was said
in your messages.  

DO NOT share this key with anyone that you do not trust
or want to see your messages.

When you click the "Generate Key" button, it will automatically put
your generated key inside "key.txt".

WARNING:
-------------------
If you click the "Generate Key" button, you will have to redo this!

DO NOT MESS WITH THESE BIN FILES:
----------------------------
*runCount.txt
cog.png

runCount.txt if deleted will regenerate reset your key, if its contents are changed in anyway, the program will error (easy fix:  delete it, I will be updating soon to fix this and make it redundant)

cog.png if deleted will require a restart so it can be automatically redownloaded.

Info
----------------------------
The way Incordnito is programmed does not accept custom keys for the
security reason being "key cracking".
This would be a case in which a person of interest would
be able to run a program that would constantly test tons of keys until
they find the one that works.



Enjoy!
--------------------
