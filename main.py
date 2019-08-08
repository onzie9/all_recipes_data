# Python 2.7.12
# Written by Trevor McGuire
# GitHub: onzie9

from bs4 import BeautifulSoup
import requests
import re
import time
from torrequest import TorRequest
import numpy as np

# These first three lines are just setting up how I want my data to be written.  They are set to amend currently because
# the code scrapes in segments, so the resulting file gets written to multiple times.
ingredients_file = open("ingredients_file.txt", "a+")
no_recipe = open("no_recipes.txt", "a+")
equalsigns = "======================================="

# The first for loop is there so that I can change my IP after 12 visits to the website.  I found before that between 10
#  and 20 rapid visits will get an IP banned.
# The second for loop is the actual scrape for this particular site.  Depending on what you want from what website, this
#  is where things will change.

for j in np.arange(0, 9997, 12):
    for i in range(241927 + j, 241927 + j + 12):  # The 241927 is just the last place I scraped.  The unique recipes
                                                  # were really sparse out this far.
        try:
            r = requests.get("http://allrecipes.com/recipe/" + str(i))
            soup = BeautifulSoup(r.text, "html.parser")  # First download the code for the individual recipe.

            mother = soup.find("ul", {"id": "lst_ingredients_1"}).parent  # This is the part of the code that stores the
                                                                          # recipe ingredients. This is likely to change 
                                                                          # in future versions of the website.
            children = str(mother.findAll("span", {"itemprop": "ingredients"}))
            children = re.sub(r'<.+?>', '', children)
            children = re.sub(", ([0-9])", "\n \\1", children)

            type = str(soup.find("a", {"data-click-id": "recipe breadcrumb 3"}))  # This is the part of the code that
                                                                                  # stores the recipe type. This is likely
                                                                                  # to change in future versions of the website.
            type = re.sub(r'<.+?>', '', type)
            type = type.strip()

            if (type == "Desserts" or type == "Appetizer and Snacks" or type == "Salad" or type == "Breakfast and Brunch" or type == "Side Dish" or type == "Drinks" or type =="Bread"):
                            # This writes the recipe to a specific file.
                ingredients_file.write("\n" + equalsigns + "\n" + r.url.split("/")[-2] + "\n" + str(i) + " " + type +
                                       "\n" + children)
            else:
                ingredients_file.write("\n" + equalsigns + "\n" + r.url.split("/")[-2] + "\n" + str(i) + " main" + "\n"
                                       + children)
        except:
            no_recipe.write(str(i) + ", ")  # There are thousands of recipe numbers that aren't used.
            print("no recipe for some reason")
        print(str(i))
        time.sleep(1.7)  # This is needed to prevent getting banned.
    # This is the only line that is related to Tor.  In order to make Tor work, you need this line of code, and you also
    #  have to modify the torrc.txt file.  In that file, you need to uncomment the "controlport 9051" line, and then
    # uncomment the "hashed control password" line.  You also have to paste in a hash of your own password.  Get the
    # hash with 'tor --hash-password <mypassword>'.
    with TorRequest(proxy_port=9050, ctrl_port=9051, password='mypassword') as tr:
        tr.reset_identity()
