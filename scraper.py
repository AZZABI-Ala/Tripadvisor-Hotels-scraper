                               ########### Tripadvisor-Hotels-scraper #############
                    ######### Scraping script for TripAdvisor using BeautifulSoup ##########
                             ####################################################


# import libraries
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
f = csv.writer(open("Tripadvisor_hotels.csv", "w"))
f.writerow(["Comment", "Author","Date"])

# for loop
data = []
for offset in range(0, 80, 5):
    url = 'https://www.tripadvisor.fr/Hotel_Review-g187147-d197528-Reviews-or' + str(offset) + '-Le_Royal_Monceau_Raffles_Paris-Paris_Ile_de_France.html'
    # query the website and return the html to the variable 'page'
    r = requests.get(url)
    
    # parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Take the comment and get its value
    comment = soup.find('p', attrs={'class': 'partial_entry'})
    comment_value = comment.text # strip() is used to remove starting and trailing

    # Take out the <div> of author and get its value
    author = soup.find('div', attrs={'class':'username mo'})
    author_name = author.text.strip()
    
    # Take the date of comment
    date = soup.find('span', attrs={'class': 'ratingDate relativeDate'})
    comment_date = date.text.strip() # strip() is used to remove starting and trailing
    
    # save the data in tuple
    data.append((comment_value, author_name, comment_date))
    
# open a csv file with append, so old data will not be erased
with open('Tripadvisor_hotels.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)

    # The for loop
    for comment_value, author_name, comment_date in data:
        writer.writerow([comment_value, author_name, comment_date])