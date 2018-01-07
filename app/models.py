from mongoengine import *

connect('pop_tweets')

class Awards(EmbeddedDocument):
    award_type = StringField()
    nominees = ListField(StringField())


class AwardShows(Document):
    season = IntField()
    name = StringField()
    air_date = StringField()
    air_time = StringField()
    awards = ListField(EmbeddedDocumentField(Awards))


class Tweets(Document):
    award = StringField()
    tweet = StringField()


def addAwardShowData():
    golden_globes_award_1 = Awards(
        award_type = "Best Motion Picture - Drama",
        nominees = ["Call Me By Your Name", "Dunkirk", "The Post", "The Shape of Water", "Three Billboards Outside Ebbing, Missouri"]
    )

    golden_globes_award_2 = Awards(
        award_type = "Best Motion Picture - Musical or Comedy",
        nominees = ["I, Tonya", "Lady Bird", "The Disaster Artist", "Get Out", "The Greatest Showman"]
    )

    golden_globes = AwardShows(
        season = 75,
        name = "Golden Globes",
        air_date = "January 7",
        air_time = "8 p.m.",
        awards = [golden_globes_award_1, golden_globes_award_2]
    )
    golden_globes.save()

