class Playtime:
    title = ""
    avg_playtime = 0

    def __init__(self, title, avg_playtime):
        self.title = title
        self.avg_playtime = avg_playtime

class GoodRatings:
    title = ""
    pos_rate = 0

    def __init__(self, title, pos_rate):
        self.title = title
        self.pos_rate = pos_rate

class BadRatings:
    title = ""
    neg_rate = 0

    def __init__(self, title, neg_rate):
        self.title = title
        self.neg_rate = neg_rate
        
class Genre:
    name=""
    count=0

    def __init__(self, name, count):
        self.name = name
        self.count = count

class Developer:
    name = ""
    total_games = 0
    percentage = 0

    def __init__(self, name, total_games):
        self.name = name
        self.total_games = total_games