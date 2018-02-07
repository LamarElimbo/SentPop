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


#def addAwardShowData():
#    golden_globes_award_1 = Awards(
#        award_type = "Best Motion Picture - Drama",
#        nominees = ["Call Me By Your Name", "Dunkirk", "The Post", "The Shape of Water", "Three Billboards Outside Ebbing, Missouri"]
#    )

 