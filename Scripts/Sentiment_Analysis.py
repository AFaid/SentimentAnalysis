def regionSentiment(regionList, keyList, valueList):
#empty list to store sentiment value of each tweet
    sentimentList = []
#goes through tweet for given region
    for z in range (len(regionList)):
        line = regionList[z].split()
        value = 0
        count = 0
    #goes through every word in tweet and strips ir ad converts to lower case
        for i in range (len(line)):
            line[i] = line[i].strip("[],.'!@$#%?")
            line[i] = line[i].lower()
        #searches for word in keywords
            for x in range (len(keyList)):
            #if word is found in key list add one to counter and adds value to total value of tweet
                if line[i] == keyList[x]:
                    count = count + 1
                    value = value + int(valueList[x])
    #if tweet value is greater than 0 divide value by the counter to get sentiment value of the tweet
    # add to sentiment value list
        if value > 0:
            sentiment = (value/count)
            sentimentList.append(sentiment)
#add all sentiment values to get total sentiment of the region
    totalSent = sum(sentimentList)
#divide total region sentiment by number of tweets in region
    regionSent = round(totalSent/len(sentimentList), 2)
#returns tuple that contains average region sentiment and total number of region's tweets (only those that have keywords)
    regionValues  = (regionSent, len(sentimentList))
    return regionValues


def sent_Anal(fileName, fileName2):
# creates lists to store key words and values
    keyList = []
    valueList = []

#opens file and checks for invalid input
    try:
        keyfile = open(fileName, "r")
    except:
        print ("Invalid input for keywords file")
        sys.exit()

#goes through every line in keyfile and adds the keywords to a list and their corresponding values
#to anohter list
    for line in keyfile:
        key = line.split(",")
        for i in range (len(key)):
            key[i] = key[i].strip()
        keyList.append(key[0])
        valueList.append(key[1])

#creates list to store latitude and longitude and text of the tweets
    latitude = []
    longitude = []
    tweets = []

#validates input for name of the tweets file
    try:
        tweetFile =  open(fileName2, "r")
    except:
        print("Invalid input for tweets file")
        sys.exit()

#Goes through every line in tweets file
    for line in tweetFile:
        line = line.split(" ",5)
#strips unwanted punctiation from words in line
        for i in range (len(line)):
            line[i] = line[i].strip("[],.'!@$#%?")
#adds longitude of each tweet to list of longitude
        longitude.append(float(line[0]))
#adds lattitude of each list to a list of lattitude
        latitude.append(float(line[1]))
#adds text of each tweet to list of tweets
        tweets.append(line[5])

#creates lists to store tweets for each region
    pacificTweets = []
    easternTweets = []
    mountainTweets = []
    centralTweets = []

#checks latitude and longitude of tweets and adds it to its region's tweets
    for i in range (len(tweets)):
        if float(longitude[i]) < 49.189787 and float(longitude[i]) > 24.660845:
            if latitude[i] > -125.242264 and latitude[i] < -115.236428:
                pacificTweets.append(tweets[i])
            elif latitude[i] > -115.236428 and latitude[i] < -101.998892:
                mountainTweets.append(tweets[i])
            elif latitude[i] > -101.998892 and latitude[i] < -87.518395:
                centralTweets.append(tweets[i])
            elif latitude[i] > -87.518395 and latitude[i] < -67.444574:
                easternTweets.append(tweets[i])

#calls on function to calculate the total number of tweets and the average sentiment value for each region and adds it to a list
    finalList = []
    finalList.append(regionSentiment(easternTweets, keyList, valueList))
    finalList.append(regionSentiment(centralTweets, keyList, valueList))
    finalList.append(regionSentiment(mountainTweets, keyList, valueList))
    finalList.append(regionSentiment(pacificTweets, keyList, valueList))

#close files
    keyfile.close()
    tweetFile.close()

#returns a list of region average sentiment and total number of tweets
    return finalList
