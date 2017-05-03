Problem Statement:

IMDB provides a list of celebrities born on the current date. Below is the link: 
http://m.imdb.com/feature/bornondate 
Get the list of these celebrities from this webpage using web scraping (the ones that are 
displayed i.e top 10). You have to extract the below information: 

1. Name of the celebrity 
2. Celebrity Image 
3. Profession 
4. Best Work 
Once you have this list, run a sentiment analysis on twitter for each celebrity and finally the 
output should be in the below format 

1. Name of the celebrity:
2. Celebrity Image: 
3. Profession:
4. Best Work: 
5. Overall Sentiment on Twitter: Positive, Negative or Neutral

Python used is – Python 2.7.6
Os used is Ubuntu (not vm so finding difficult to prepare document)



Tools and Packages used:

Tweepy: is an open-sourced on Github, and enables python to communicate with the Twitter platform  and use its API.

Codes: is used for storing the data, to stream and file interfaces for transcoding the data. In project I have used it for storing the tweets as Unicode text and for all file handling and operations.

BeautifulSoup: BeautifulSoup is used for webScraping. I have used it to store the contents from IMDB web page using html5lib parser.

Selenium: The webdriver kit emulates the web-browser and executes the JS script to load the dynamic content.

Punctuation: to get rid of all the pumctuations present in the tweet.

Challenges Faced during the project:

The IMDB website has dynamic content:

Reference: http://fruchter.co/post/53164489086/python-headless-web-browser-scraping-on-amazon
Description: Had to use the Selenium’s webdriver to emulate a Chrome browser and execute the JS functions which dynamically fetches the details of celebrities born on the current day.



A
A
A
A
A
A
A

