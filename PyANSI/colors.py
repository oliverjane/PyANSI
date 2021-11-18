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

# print color from hex RGB value


def printHex(*values, sep=" ", end="\n", foreHex=None, backHex=None):
    """Prints the values to sys.stdout using the given 24-bit hexadecimal values.\n
    Optional keyword arguments:\n
    sep:     String inserted between values, default is space\n
    end:     String appended after the last value, default is newline.\n
    backHex: Background color hexadecimal value, default is none.\n
    foreHex: foreground color hexadecimal value, default is none."""
    foreCol = ""
    backCol = ""

    if foreHex != None:
        foreHex = foreHex.strip("#")
        foreRed = int(foreHex[:2], 16)
        foreGreen = int(foreHex[2:4], 16)
        foreBlue = int(foreHex[4:], 16)

        if 0 <= foreRed <= 255 and 0 <= foreGreen <= 255 and 0 <= foreBlue <= 255:
            foreCol = f"\x1b[38;2;{foreRed};{foreGreen};{foreBlue}m"
        else:
            raise ValueError("Value out of range")
    if backHex != None:
        backHex = backHex.strip("#")
        backRed = int(backHex[:2], 16)
        backGreen = int(backHex[2:4], 16)
        backBlue = int(backHex[4:], 16)

        if 0 <= backRed <= 255 and 0 <= backGreen <= 255 and 0 <= backBlue <= 255:
            backCol = f"\x1b[48;2;{backRed};{backGreen};{backBlue}m"
        else:
            raise ValueError("Value out of range")

    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    print(Output, end=end)


# print color from 256 color mode


def print256(*values, sep=" ", end="\n", foreColor=None, backColor=None):
    """Prints the values to sys.stdout using the given 8-bit color codes.\n
    Optional keyword arguments:\n
    sep:        String inserted between values, default is space\n
    end:        String appended after the last value, default is newline.\n
    backColor: Background color hexadecimal value, default is none.\n
    foreColor: foreground color hexadecimal value, default is none."""

    foreCol = ""
    backCol = ""
    if foreColor != None:
        if 0 <= foreColor <= 255:
            foreCol = f"\x1b[38;5;{foreColor}m"
        else:
            raise ValueError("Value out of range")

    if backColor != None:
        if 0 <= backColor <= 255:
            backCol = f"\x1b[48;5;{backColor}m"
        else:
            raise ValueError("Value out of range")

    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    print(Output, end=end)


def colorHex(*values, sep=" ", foreHex=None, backHex=None):
    """Returns the values using the given 24-bit hexadecimal values.\n
    Optional keyword arguments:\n
    sep:     String inserted between values, default is space\n
    end:     String appended after the last value, default is newline.\n
    backHex: Background color hexadecimal value, default is none.\n
    foreHex: foreground color hexadecimal value, default is none."""
    foreCol = ""
    backCol = ""
    if foreHex != None:
        foreHex = foreHex.strip("#")
        foreRed = int(foreHex[:2], 16)
        foreGreen = int(foreHex[2:4], 16)
        foreBlue = int(foreHex[4:], 16)
        if 0 <= foreRed <= 255 and 0 <= foreGreen <= 255 and 0 <= foreBlue <= 255:
            foreCol = f"\x1b[38;2;{foreRed};{foreGreen};{foreBlue}m"
        else:
            raise ValueError("Value out of range")
    if backHex != None:
        backHex = backHex.strip("#")
        backRed = int(backHex[:2], 16)
        backGreen = int(backHex[2:4], 16)
        backBlue = int(backHex[4:], 16)
        if 0 <= backRed <= 255 and 0 <= backGreen <= 255 and 0 <= backBlue <= 255:
            backCol = f"\x1b[48;2;{backRed};{backGreen};{backBlue}m"
        else:
            raise ValueError("Value out of range")
    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    return Output


# print color from 256 color mode
def color256(*values, sep=" ", foreColor=None, backColor=None):
    """Prints the values to sys.stdout using the given 8-bit color codes.\n
    Optional keyword arguments:\n
    sep:       String inserted between values, default is space\n
    end:       String appended after the last value, default is newline.\n
    backColor: Background color hexadecimal value, default is none.\n
    foreColor: Foreground color hexadecimal value, default is none."""

    foreCol = ""
    backCol = ""
    if foreColor != None:
        if 0 <= foreColor <= 255:
            foreCol = f"\x1b[38;5;{foreColor}m"
        else:
            raise ValueError("Value out of range")

    if backColor != None:
        if 0 <= backColor <= 255:
            backCol = f"\x1b[48;5;{backColor}m"
        else:
            raise ValueError("Value out of range")

    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    return Output
