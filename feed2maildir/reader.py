import feedparser

class Reader:
    """Get updates on the supplied feed"""

    def __init__(self, feed, silent=False):
        self.feed   = None
        self.silent = silent

        f = feedparser.parse(feed)
        if f.bozo:
            raise Exception('Could not parse feed')
        else:
            self.feed = f

    def output(self, arg):
        if not self.silent:
            print(arg)
