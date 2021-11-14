# PyANSI
PyANSI provides an easy way to use ANSI escape codes to control the colour and cursor of a terminal.
## System Requirements
PyANSI is primarily intended for Unix-like operating systems but will run on any operating system which supports ANSI escape codes.

Note: Windows users may need to initialise the console using `PyANSI.windows.init()`
## Install
Install using pip:
```
pip instally PyANSI
```
## Examples
### Colour
Note: The `colours` and `colors` submodules are functionally identical but the `colors` submodule uses the American spelling of color instead of colour.
#### True Colour
```python
from PyANSI import colours
colours.printHex("Hello, World!", foreHex="#00AEFF", backHex="#FF5500")
```
#### ANSI 256 Colour Mode
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