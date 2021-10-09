# PyANSI
PyANSI provides an easy way to use ANSI escape codes to control the colour and cursor of a terminal.
## System Requirements
PyANSI is primarily intended for Unix-like operating systems but will run on any operating system which supports ANSI escape codes.

Note: Windows users may need to enable support for ANSI escape codes if using Command Prompt or PowerShell. To do this, open registry editor and navigate to `HKEY_CURRENT_USER\Console\` Create a DWORD entry called `VirtualTerminalLevel` with a value of 1. 
Windows users may also need to 'initialise' the terminal for ANSI support using
```python
import subprocess
subprocess.call("", shell=True)
```
## Examples
### Colour
True colour
```python
from PyANSI import colours
colours.printHex("Hello, World!", foreHex="#00AEFF", backHex="#FF5500")
```
ANSI 256 colour mode
```python
from PyANSI import colours
colours.print256("Hello, World!", foreColour=32, backColour=172)
```
### Cursor Control
Show/hide the cursor
```python
from PyANSI import cursor
cursor.hide()
cursor.show()
```
Move the cursor
```python
from PyANSI import cursor
cursor.move.left(10)
cursor.move.right(10)
cursor.move.up(10)
cursor.move.right(10)
```
Jump to home
```python
from PyANSI import cursor
cursor.home()
```