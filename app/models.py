from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class RealityShows(Base):
    __tablename__ = 'reality_shows'
    show = Column(String(250), index = True, primary_key = True)
    contestant = Column(String(250), index = True, primary_key = True)
    tweets = relationship('Tweets', backref = 'reality_shows')
    num_pos_tweets = Column(Integer)
    num_neg_tweets = Column(Integer)
    

class Tweets(Base):
    __tablename__ = 'tweets'
    tweet_id = Column(String(250), index = True, primary_key = True)
    tweet = Column(String(250))
    sentiment = Column(String(250))
    date_time = Column(String(250))


def addAwardShowData():
    golden_globes_award_1 = Awards(
        award_type = "Best Motion Picture - Drama",
        nominees = ["Call Me By Your Name", "Dunkirk", "The Post", "The Shape of Water", "Three Billboards Outside Ebbing, Missouri"]
    )

    golden_globes_award_2 = Awards(
        award_type = "Best Motion Picture - Musical or Comedy",
        nominees = ["I, Tonya", "Lady Bird", "The Disaster Artist", "Get Out", "The Greatest Showman"]
    )
    
    golden_globes_award_3 = Awards(
        award_type = "Best Motion Picture - Animated",
        nominees = ["The Boss Baby", "The Breadwinner", "Coco", "Ferdinand", "Loving Vincent"]
    )
    
    golden_globes_award_4 = Awards(
        award_type = "Best Motion Picture - Foreign Language",
        nominees = ["Loveless", "The Square", "A Fantastic Woman", "First They Killed My Father", "In The Fade"]
    )
    
    golden_globes_award_5 = Awards(
        award_type = "Best Television Series - Drama",
        nominees = ["The Crown", "Game of Thrones", "The Handmaid's Tale", "Stranger Things", "This Is Us"]
    )
    
    golden_globes_award_6 = Awards(
        award_type = "Best Television Series - Musical or Comedy",
        nominees = ["Black-ish", "The Marvelous Mrs. Maisel", "Master of None", "SMILF", "Will & Grace"]
    )
    
    golden_globes_award_7 = Awards(
        award_type = "Best Television Limited Series or Motion Picture Made for Television",
        nominees = ["Big Little Lies", "Fargo", "Feud: Bette And Joan", "The Sinner", "Top of The Lake: China Girl"]
    )
    
    golden_globes = AwardShows(
        season = 75,
        name = "Golden Globes",
        air_date = "January 7",
        air_time = "8 p.m.",
        awards = [golden_globes_award_1, golden_globes_award_2, golden_globes_award_3, golden_globes_award_4, golden_globes_award_5, golden_globes_award_6, golden_globes_award_7]
    )
    golden_globes.save()


