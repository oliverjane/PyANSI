# Copyright (C) 2021 Oliver Jane
# This file is part of PyANSI.
# 
# PyANSI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# PyANSI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with PyANSI.  If not, see <https://www.gnu.org/licenses/>.

#print color from hex RGB value

def printHex(*values, sep=" ", end="\n", foreHex = None, backHex = None):
    """Prints the values to sys.stdout using the given 24-bit hexadecimal values.\n
Optional keyword arguments:\n
sep:     String inserted between values, default is space\n
end:     String appended after the last value, default is newline.\n
backHex: background color hexadecimal value, default is none.\n
foreHex: Foreground color hexadecimal value, default is none."""
    ForeCol = ""
    BackCol = ""
    if foreHex != None:
        foreHex = foreHex.strip("#")
        ForeRed = int(foreHex[:2], 16)
        ForeGreen = int(foreHex[2:4], 16)
        ForeBlue = int(foreHex[4:], 16)
        if 0 <= ForeRed <= 255 and 0 <= ForeGreen <= 255 and 0 <= ForeBlue <= 255:
            ForeCol = "\x1b[38;2;{red};{green};{blue}m".format(red = ForeRed, green = ForeGreen, blue = ForeBlue)
        else:
            raise ValueError("Value out of range")
    if backHex != None:
        backHex = backHex.strip("#")
        BackRed = int(backHex[:2], 16)
        BackGreen = int(backHex[2:4], 16)
        BackBlue = int(backHex[4:], 16)
        if 0 <= BackRed <= 255 and 0 <= BackGreen <= 255 and 0 <= BackBlue <= 255:
            BackCol = "\x1b[48;2;{red};{green};{blue}m".format(red = BackRed, green = BackGreen, blue = BackBlue)
        else:
            raise ValueError("Value out of range")
    Output = ForeCol + BackCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    print(Output, end=end)

#print color from 256 color mode

def print256(*values, sep=" ", end="\n", foreColor = None, backColor = None):
    """Prints the values to sys.stdout using the given 8-bit color codes.\n
Optional keyword arguments:\n
sep:        String inserted between values, default is space\n
end:        String appended after the last value, default is newline.\n
backColor: background color hexadecimal value, default is none.\n
foreColor: Foreground color hexadecimal value, default is none."""

    ForeCol = ""
    BackCol = ""
    if foreColor != None:
        if 0 <= foreColor <= 255:
            ForeCol = "\x1b[38;5;{}m".format(foreColor)
        else:
            raise ValueError("Value out of range")
    
    if backColor != None:
        if 0 <= backColor <= 255:
            BackCol = "\x1b[48;5;{}m".format(backColor)
        else:
            raise ValueError("Value out of range")
    
    Output = ForeCol + BackCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    print(Output, end=end)