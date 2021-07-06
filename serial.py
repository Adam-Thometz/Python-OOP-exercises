"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__ (self, start=100):
        """Initializes new serial generator"""
        self.start = start
        self.next = start
    
    def __repr__(self):
        return f'SerialGenerator start={self.start} next={self.next}'

    def generate(self):
        """Generates new serial number"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets serial generator"""
        self.next = self.start