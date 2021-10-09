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

def hide():
    """Hide the cursor"""
    print("\x1b[?25l", end="")

def show():
    """Show the cursor"""
    print("\x1b[?25h", end="")

class move:

    def left(distance: int):
        """Move the cursor left the specified distance."""
        print("\x1b[{}D".format(distance), end="")

    def right(distance: int):
        """Move the cursor right the specified distance."""
        print("\x1b[{}C".format(distance), end="")

    def up(distance: int):
        """Move the cursor up the specified distance."""
        print("\x1b[{}A".format(distance), end="")

    def down(distance: int):
        """Move the cursor down the specified distance."""
        print("\x1b[{}B".format(distance), end="")

def home():
    """Return the cursor to the home location"""
    print("\x1b[H", end="")