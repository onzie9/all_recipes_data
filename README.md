# all_recipes_data
Scraping of 250,000+ recipes from allrecipes.com

I wrote a web scraper in Python that scraped 250,000+ recipes from allrecipes.com. Included in each recipe is the recipe name and the ingredients and measurements. The website bans scrapers after 10-15 rapid downloads, so the code includes an IP updater through Tor.

I have included the raw data in one large text file, and the data roughly parsed by recipe type.  There are 7 types, but the type "sides" only included 62 recipes, so it likely that it is no longer an active section on the website.  Of the scraped recipes, around 130,000 of the recipes were copies of one recipe for a pizza that used some kind of Johnsonville sausage. There were several other recipes that had several hundred or thousand copies of themselves.  Once those are removed, there remains around 80,000 unique recipes.
