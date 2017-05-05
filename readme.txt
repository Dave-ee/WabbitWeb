WabbitWeb

Author: 		Dave-ee Jones
Version: 		1.
Category: 		Tool/General
Target: 		Anything with a web browser
Attack: 		RNDIS
Requires:		Impacket

Features:
- File Command System (FCS - just to make it fancy and sound like a real method..)
	- Only real way to handle commands Bash-cross-Python-cross-HTML
	
- Payload Editor (more like creator, but that doesn't sound as good)
	- Write a payload in-browser and save it to a 'Letter' (A, B or C)
	
- Payload Launcher (well, just tells the Bunny to run a script really..)
	- Launch a payload 'Letter' (A, B or C)
	
- SMB Launcher (this is pre'ey cool)
	- Launch an SMB server in the root directory of the Bunny itself
	- Automatically takes you to the location of the SMB server via Windows Explorer popup
	- Accessible as: \\172.16.64.1\s

- Shutdown (yes, this is a feature)
	- Shuts down WabbitWeb

LED Configuration:
					
STATE 		COLOUR			ACTION

SETUP		M (SOLID)		Performing checks
FAIL2		R (FAST)		Directory 'ww' not found
FAIL3		R (VFAST)		Failed to mount directory 'mfs'
STAGE1		Y (SINGLE)		Starting webserver/attackmode
NONE		B (SOLID)		Payload started
NONE		B (SLOW)		Webserver started/Payload ended/Waiting for commands
FAIL1		R (SLOW)		Impacket wasn't found
NONE		C (SOLID)		SMB server launching
NONE		C (SLOW)		SMB server running and waiting for commands
NONE		G (SOLID)		Shutdown sequence has started
FINISH		G (SUCCESS)		Shutdown sequence finished
NONE		NO COLOUR		Payload complete