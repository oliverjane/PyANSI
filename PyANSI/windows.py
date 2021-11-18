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

import ctypes, platform
def init():
    """Initialise the windows console"""
    if platform.system() == "Windows":
        kernel32 = ctypes.windll.kernel32
        console = kernel32.GetStdHandle(-11)
        kernel32.SetConsoleMode(console, 7)
    else:
        return None