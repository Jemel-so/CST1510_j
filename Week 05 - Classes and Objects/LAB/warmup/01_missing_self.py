# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

class Record:

    def __init__(self):
        self.value = 0
        self.limit = 10

    
    def status(percent):    # this parameter should be self
        return percent

r = Record()
print(r.status(95))
