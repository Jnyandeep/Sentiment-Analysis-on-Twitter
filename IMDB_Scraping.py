__author__='jT'

import urllib2
from bs4 import BeautifulSoup as bS
from selenium import webdriver
import codecs
import twitter_Sentiment_Analysis

#All the required modules have been imported to proceed with


def imdbScraping():
    celebrityNameList = []
    celebrityDetails = {}
    counter = 0

    BASE_URL = "http://m.imdb.com/feature/bornondate"

#I'm using Selenium tool to extract the content from the IMDB page as this page is dynamic in nature
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    html = driver.page_source
#Creating soup object to html that I have generated with webdriver.
    soup = bS(html, "html5lib")
    content = soup.find('section', 'posters list')
    bornToday = content.findChild('h1').text

#Looping through all the 'a' tag that contents all the details required about the Celebrities that we looking too
    for a in content.findAll('a', 'poster', limit=10):


        celebrityDetails[counter] = {}

#Creating a dictionary that hilds the details of each celebrities
        '''
        for 0 <= counter < 10, create a celebrity deatils of celebrity that we are interested in
            celebrityDetails{counter: {"celebrityName": "name",
                                       "celebrityImage": "image",
                                       "celebrityProfession": "profession",
                                       "celebrityBestWork": "bestWork"
                                       "celebritySentimentAnalysis": "sentimentAnalysis p/n/nt",
                                       }
                             }
        '''
#Extracting all the required details
        celebrityName = a.find('span', 'title').text
        celebrityNameList.append(celebrityName)

        celebrityDetails[counter]["celebrityName"] = celebrityName
        celebrityDetails[counter]["celebrityImage"] = a.img['src']

        Profession, bestWork = a.find('div', 'detail').text.split(",", 1)

        celebrityDetails[counter]["celebrityProfession"] = Profession
        celebrityDetails[counter]["celebrityBestWork"] = bestWork


        counter += 1
        #print counter
#Returning celebrity name list and the celebrity details.
    return celebrityNameList, celebrityDetails




if __name__ == '__main__':
    count = 0
#Calling imdbScraping function that returns the details that we have asked.
    celebrityNameList, celebrityDetails = imdbScraping()

# Creating instance reference object of Twitter analysis class that we are using to access the class objects
    celebrity = twitter_Sentiment_Analysis.twitterSentimentAnalysis()
#Final output file that contains the actual output
    finalOutFile = codecs.open("Final_Outfile.txt", 'w', "utf-8")

#Iterating through the celebrity details to print the final output
    for i in xrange(10):
        celebrityName = celebrityDetails[i]["celebrityName"]
        celebrity.tweetSearch(celebrityName)
        celebrityDetails[i]["celebritySentimentAnalysis"] = celebrity.sentimentAnalysis()
        count +=1
        #print celebrityNameList[i]["celebrityName"]
        finalOutFile.write("S.No-->" + str(count) + '\n')
        finalOutFile.write("Name of the celebrity: " + celebrityDetails[i]["celebrityName"] + "\n")
        finalOutFile.write("Celebrity Image: " + celebrityDetails[i]["celebrityImage"] + "\n")
        finalOutFile.write("Profession:str " + celebrityDetails[i]["celebrityProfession"] + "\n")
        finalOutFile.write("Best work: " + celebrityDetails[i]["celebrityBestWork"] + "\n")
        finalOutFile.write("Overall sentiment on Twitter: " + celebrityDetails[i]["celebritySentimentAnalysis"] + '\n')
        finalOutFile.write("\n\n")

    finalOutFile.close()





