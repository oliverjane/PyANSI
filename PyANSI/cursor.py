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