from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
import logging

##################################
########## ENGINE SETUP ##########
##################################

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

engine_config = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

engine = create_engine(engine_config, echo = True)

###################################
########## SESSION SETUP ##########
###################################

Session = sessionmaker(bind = engine)
session = Session()

############################################
########## DEFINE DATABASE MODELS ##########
############################################

Base = declarative_base()

class RealityShow(Base):
    __tablename__ = 'reality_shows'
    show = Column(String(250), index = True, primary_key = True)
    contestant = Column(String(250), index = True, primary_key = True)
    tweets = relationship('Tweets', backref = 'reality_shows')
    num_pos_tweets = Column(Integer)
    num_neg_tweets = Column(Integer)
    
class Contestant(Base):
    full_name = Column(String(250))
    alternative_names = Column(String(250), index = True, primary_key = True)
    
class Tweet(Base):
    __tablename__ = 'tweets'
    tweet_id = Column(Integer, index = True, primary_key = True)
    tweet = Column(String(250))
    sentiment = Column(String(250))
    date_time = Column(String(250))

###############################################
########## CREATE TABLES IN DATABASE ##########
###############################################

#def addAwardShowData():
#    golden_globes_award_1 = Awards(
#        award_type = "Best Motion Picture - Drama",
#        nominees = ["Call Me By Your Name", "Dunkirk", "The Post", "The Shape of Water", "Three Billboards Outside Ebbing, Missouri"]
#    )

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    
    reality_show = RealityShow()