#import functions
from Sentiment_Analysis import*
import sys

#asks user for name of the files
fileName = input("Enter file name")
fileName2 = input("Enter File name")

#call function to get regions sentiment and prints them
sentiments_Final = sent_Anal(fileName, fileName2)
print("The Eastern reagion totaled", sentiments_Final[0][1], "tweets and had a sentiment value of", sentiments_Final[0][0])
print("The Central reagion totaled", sentiments_Final[1][1], "tweets and had a sentiment value of", sentiments_Final[1][0])
print("The Mountain reagion totaled", sentiments_Final[2][1], "tweets and had a sentiment value of", sentiments_Final[2][0])
print("The Pacific reagion totaled", sentiments_Final[3][1], "tweets and had a sentiment value of", sentiments_Final[3][0])
