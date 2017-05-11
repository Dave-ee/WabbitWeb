# WabbitWeb
#### Payload-handling and SMB service managed by a Python webserver!

Link to WabbitWeb forum post is [here](https://forums.hak5.org/index.php?/topic/40941-payload-wabbitweb/), with information about usage and features.

### [1.0.6] Minor update
- Redone the HTML/CSS web layout
- SMB server no longer instantly starts up when going to the SMB Launcher page
- Payload Editor is now much easier/nicer to use

### [1.0.5] Minor update
- More FCS: 'COMMAND.sh' no longer gets deleted once sourced, it gets saved to 'ww/cmds' directory (if one already exists, it gives it a number on the end of the filename)

### [1.0.4] Minor update
- Cleaned webserver (routing, POST handling etc.)
- More FCS: If there is a file called 'COMMAND.sh' in the 'ww' directory it will be sourced instantly and then deleted
- Reduced the overall size to less than a third of its original

### [1.0.3] Minor update
- Changed webserver port from **8080** to **80**
- Changed mount directory path from **udisk** to **/** (root)
