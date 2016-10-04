# your code goes here

import sys 

restaurant_scores_source = open(sys.argv[1])

restaurant_ratings = {}

for line in restaurant_scores_source:
    #Splits each line at : and creates a list containing two strings for each line
    restaurant_details = line.split(":")
    
    #Strips white space from rating
    restaurant_details[1] = restaurant_details[1].rstrip() 

    # we set the key of restaurant_ratings to the 0th index of our list (the restaurant)
    # to the index[1] of our list(the rating of said restaurant)
    restaurant_ratings[restaurant_details[0]] = int(restaurant_details[1])

sorted_keys = sorted(restaurant_ratings.keys())

for restaurant in sorted_keys:
    print restaurant, "is rated at", restaurant_ratings[restaurant]
    

    # sorted_ratings = [key, value]





restaurant_scores_source.close()

