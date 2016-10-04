# your code goes here

import sys 
ratings_filename = sys.argv[1]

def restaurant_rater(input_filename):
    """
    Prints an alphabetized list of restaurants and their ratings using a dictionary.

    Asks user to contribute to the dictonary and give a restaurant name and rating
    """

    #Open input file
    restaurant_scores_source = open(input_filename)

    #Initialize restaurant_ratings dictionary
    restaurant_ratings = {}

    #Ask user for a restaurant name and rating and store resulting strings
    user_add_restaurant = raw_input("Please add the name of a restaurant you would like to rate: ")
    user_add_score = int(raw_input("Please enter the rating: "))

    #Add user input to dictionary
    restaurant_ratings.update({user_add_restaurant: user_add_score})

    #Loop through each line in input file
    for line in restaurant_scores_source:
        #Strips and splits each line at : and unpacks list into name and rating
        name, rating = line.rstrip().split(":")

        #Add keys and values to restaurant_ratings based on name and rating
        restaurant_ratings[name] = int(rating)

    for restaurant in sorted(restaurant_ratings):
        print restaurant, "is rated at", restaurant_ratings[restaurant]
    
    restaurant_scores_source.close()

#Call restaurant_rater with user inputted filename from sys
restaurant_rater(ratings_filename)
