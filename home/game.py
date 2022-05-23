class Game():
    gameid = 0
    title = ""
    rel_date = ""
    english = ""
    dev = ""
    publisher = ""
    platform = ""
    rec_age = ""
    categories = ""
    genre = ""
    steamspy_tags = ""
    achievements = 0
    pos_rate = 0
    neg_rate = 0
    avg_playtime = 0
    median_playtime = 0
    owners = ""
    price = 0
    deleted = 0
    wishlisted = 0

    def __init__(self, gameid, title, rel_date, english, dev, publisher, platform, rec_age, categories, genre, steamspy_tags, achievements, pos_rate, neg_rate, 
    avg_playtime, median_playtime, owners, price):
        self.gameid = gameid
        self.title = title
        self.rel_date = rel_date
        self.english = english
        self.dev = dev
        self.publisher = publisher
        self.platform = platform
        self.rec_age = rec_age
        self.categories = categories
        self.genre = genre
        self.steamspy_tags = steamspy_tags
        self.achievements = achievements
        self.pos_rate = pos_rate
        self.neg_rate = neg_rate
        self.avg_playtime = avg_playtime
        self.median_playtime = median_playtime
        self.owners = owners
        self.price = price
        self.deleted = 0
        self.wishlisted = 0

    def set_gameid(self, id):
        self.gameid = id

    def get_title(self):
        return self.title

    def get_dev(self):
        return self.dev

    def get_genre(self):
        return self.genre

    def get_pub(self):
        return self.publisher

    def get_price(self):
        return self.price