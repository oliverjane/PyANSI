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

# print colour from hex RGB value


def printHex(*values, sep=" ", end="\n", foreHex=None, backHex=None):
    """Prints the values to sys.stdout using the given 24-bit hexadecimal values.\n
    Optional keyword arguments:\n
    sep:     String inserted between values, default is space\n
    end:     String appended after the last value, default is newline.\n
    backHex: Background colour hexadecimal value, default is none.\n
    foreHex: foreground colour hexadecimal value, default is none."""
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


# print colour from 256 colour mode


def print256(*values, sep=" ", end="\n", foreColour=None, backColour=None):
    """Prints the values to sys.stdout using the given 8-bit colour codes.\n
    Optional keyword arguments:\n
    sep:        String inserted between values, default is space\n
    end:        String appended after the last value, default is newline.\n
    backColour: Background colour hexadecimal value, default is none.\n
    foreColour: foreground colour hexadecimal value, default is none."""

    foreCol = ""
    backCol = ""
    if foreColour != None:
        if 0 <= foreColour <= 255:
            foreCol = f"\x1b[38;5;{foreColour}m"
        else:
            raise ValueError("Value out of range")

    if backColour != None:
        if 0 <= backColour <= 255:
            backCol = f"\x1b[48;5;{backColour}m"
        else:
            raise ValueError("Value out of range")

    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    print(Output, end=end)


def colourHex(*values, sep=" ", foreHex=None, backHex=None):
    """Returns the values using the given 24-bit hexadecimal values.\n
    Optional keyword arguments:\n
    sep:     String inserted between values, default is space\n
    end:     String appended after the last value, default is newline.\n
    backHex: Background colour hexadecimal value, default is none.\n
    foreHex: foreground colour hexadecimal value, default is none."""
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


# print colour from 256 colour mode
def colour256(*values, sep=" ", foreColour=None, backColour=None):
    """Prints the values to sys.stdout using the given 8-bit colour codes.\n
    Optional keyword arguments:\n
    sep:       String inserted between values, default is space\n
    end:       String appended after the last value, default is newline.\n
    backColour: Background colour hexadecimal value, default is none.\n
    foreColour: Foreground colour hexadecimal value, default is none."""

    foreCol = ""
    backCol = ""
    if foreColour != None:
        if 0 <= foreColour <= 255:
            foreCol = f"\x1b[38;5;{foreColour}m"
        else:
            raise ValueError("Value out of range")

    if backColour != None:
        if 0 <= backColour <= 255:
            backCol = f"\x1b[48;5;{backColour}m"
        else:
            raise ValueError("Value out of range")

    Output = foreCol + backCol + sep.join([str(elem) for elem in values]) + "\x1b[0m"
    return Output
