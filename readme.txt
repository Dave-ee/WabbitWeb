WabbitWeb

Author: 		Dave-ee Jones
Version: 		1.1.0
Category: 		Tool/General
Target: 		Windows 7, 8, 8.1, 10
Attack: 		RNDIS, HID
Requires:		Impacket

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