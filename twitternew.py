import tweepy
import time
import string
import operator
import sys

ACCESS_TOKEN = '964905320748371969-rO61JjHqKG74yFrwCvE5CmATQWmQ38K'
ACCESS_SECRET = 't6p7FnK4HIeajrY7kHyWdSJMNan2pyN1lUcwk4aUPTcpp'
CONSUMER_KEY = 'iGVd6epC9o0I50Wr8CFo072fB'
CONSUMER_SECRET = 'LJv6nKOkBgsqwnQdb1dg0yGPqLH0d9vFLrvNQ9XHXT5wMWIsGr'
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
    i+=1
    f.write(res.user.screen_name)
    f.write(' ')
    f.write('[')
    f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
    f.write(']')    
    f.write(" ")
    f.write('"')
    f.write(res.text.replace('\n',''))
    f.write('"')
    f.write(" ")
    f.write(str(res.user.followers_count))
    f.write(" ")
    f.write(str(res.retweet_count))
    f.write('\n')
f.close
print("Tweets retrieved ",i)

  # Top n users who are having maximum number of followers.
def maxNumberOfFollowers():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    lastInTopTen = 0
    lastInTopTN = "abc"
    s1 = []
    fp = open (INPUT_FILE_PATH, encoding = "latin-1")
    line= fp.readlines()
    for word in line:
        maxfollow = word.split()
        if not s1:
           s1.append(maxfollow[0]) 
           lastInTopTen = int(maxfollow[-2])
           lastInTopTN = maxfollow[0]   
        elif  len(s1) < 10:
           s1.append(maxfollow[0]) 
           if lastInTopTen > int(maxfollow[-2]):
               lastInTopTen = int(maxfollow[-2])
               lastInTopTN = maxfollow[0] 
        elif lastInTopTen < int(maxfollow[-2]):
             s1.remove(lastInTopTN)    
             lastInTopTen = int(maxfollow[-2])
             lastInTopTN = maxfollow[0] 
             s1.append(maxfollow[0]) 
             
    fp.close()
        
    
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
       
    outputFile.write("The top 10 users who have the maximum followers: " + "\n\n")

    for item in s1:
        outputFile.write("Username: " + item + "\n\n")
    outputFile.close()

# Top n users with most number of tweets.
def mostNumberOfTweets():
    INPUTFILE = input("Input file Location: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Output File Location: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    fp = open (INPUT_FILE_PATH, encoding = "latin-1")
    line=fp.readlines()
    count = {}
    for word in line:
        if "[" in word:
           firstName = word[0: word.index("[")]
           if firstName in count:
              count[firstName] +=1
           else:
              count[firstName] = 1
            
    fp.close()
    
    SortedCount = sorted(count.items(), key = operator.itemgetter(1), reverse = True)
 
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
       
    outputFile.write("The top 10 users with most number of tweets: \n")
    for i in range (0,10):
        outputFile.write("User Name " + SortedCount[i][0] + "\n\n")    
    outputFile.close()
	

# Top n tweets with maximum number of retweet count.
def topTenTweetReCount():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    lastInTopTen = 0
    count = {}
    fp = open (INPUT_FILE_PATH, encoding = "latin-1")
    line= fp.readlines()
    
    for word in line:
        if " \"" in word and "\" " in word:
           tweets = word[word.index(" \""): word.index("\" ")]
           tweeterUser = word.split()
           lastInTopTen = int(tweeterUser[-1])
           count[tweets]= lastInTopTen
           
    fp.close()
    print(len(count))
    SortedCount = sorted(count.items(), key = operator.itemgetter(1), reverse = True)
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
       
    outputFile.write("The top 10 Tweets with most number of tweets: \n")
    for i in range (0,10):
        outputFile.write("Tweets " + SortedCount[i][0] + "\n\n")    
    outputFile.close()
	
# Top n users who have tweeted the most in every hour.
def topTenUsersPerHour():
    INPUTFILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUTFILE+ '.txt'
    OUTFILE = input("Enter the file write path: ")
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    mintime = 24
    maxtime = 0

    fp = open (INPUT_FILE_PATH, encoding = "latin-1")
    line= fp.readlines()
    
    for word in line:
        if ":" in word:
           tweeterline = word.split()
           tweetertime = tweeterline[1].split(":")
           hr = int(tweetertime[1])
        
           if mintime > hr:
              mintime = hr
            
           if maxtime < hr:
               maxtime = hr
             
    fp.close()
    outputFile = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')        
    for hr in range (mintime, maxtime):
        count={}
        fp = open (INPUT_FILE_PATH, encoding = "latin-1")
        line1 = fp.readlines()
        for word1 in line1:
           if ":" in word1:
             tweeterline1 = word1.split()
             tweetertime1 = tweeterline1[1].split(":")
             hr1 = int(tweetertime1[1])
            
             if hr1-hr == 1:
                 
                 if tweeterline1[0] in count:
                    count[tweeterline1[0]] +=1
                 else:
                    count[tweeterline1[0]] = 1
                    
        fp.close()
        
        SortedCount = sorted(count.items(), key = operator.itemgetter(1), reverse = True)
        
        
       
        outputFile.write("The top 10 users with most number of tweets in from "+ str(hr) +":00 To "+ str(hr+1) + ":00 \n")
        
        if len(SortedCount) < 10:
           for i in range (0,len(SortedCount)):
               outputFile.write("User Name " + SortedCount[i][0] + "\n\n")   
        elif len(SortedCount) > 10:
              for i in range (0,10):
               outputFile.write("User Name " + SortedCount[i][0] + "\n\n")   
    outputFile.close()            
        
          
topTenUsersPerHour()
topTenTweetReCount()
mostNumberOfTweets()
maxNumberOfFollowers()
