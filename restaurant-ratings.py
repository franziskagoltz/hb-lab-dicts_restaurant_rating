# your code goes here

import sys 

def restaurant_rater():
    """
    Prints an alphabetized list of restaurants and their ratings using a dictionary.
    """

    restaurant_scores_source = open(sys.argv[1])
    restaurant_ratings = {}

    for line in restaurant_scores_source:
        #Strips and splits each line at : and unpacks list into name and rating
        name, rating = line.rstrip().split(":")

        #Add keys and values to restaurant_ratings based on name and rating
        restaurant_ratings[name] = int(rating)

    for restaurant in sorted(restaurant_ratings):
        print restaurant, "is rated at", restaurant_ratings[restaurant]
    
    restaurant_scores_source.close()

restaurant_rater()
