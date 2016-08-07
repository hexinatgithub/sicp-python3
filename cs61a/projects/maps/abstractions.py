"""Data Abstractions"""

from utils import mean

# Reviews

def make_review(restaurant_name, rating):
    """Return a review."""
    return [restaurant_name, rating]

def review_restaurant_name(review):
    """Return the reviewed restaurant's name (string)."""
    return review[0]

def review_rating(review):
    """Return the number of stars given (1 to 5)."""
    return review[1]

# Users

def make_user(name, reviews):
    """Return a user."""
    return [name, {review_restaurant_name(r): r for r in reviews}]

def user_name(user):
    """Return the USER's name (string)."""
    return user[0]

def user_reviews(user):
    """Return a dictionary from restaurant names to reviews by the USER."""
    return user[1]

### === +++ USER ABSTRACTION BARRIER +++ === ###

def user_reviewed_restaurants(user, restaurants):
    """Return the subset of restaurants reviewed by USER.

    Arguments:
    user -- a user
    restaurants -- a dictionary from restaurant names to restaurants
    """
    names = user_reviews(user).keys()
    return {name: restaurants[name] for name in names if name in restaurants}

def user_rating(user, restaurant_name):
    """Return the rating given for RESTAURANT_NAME by USER."""
    return review_rating(user_reviews(user)[restaurant_name])

# Restaurants

def make_restaurant(name, location, categories, price, reviews):
    """Return a restaurant, implemented as a dictionary."""
    # You may change this starter implementation however you wish, including
    # adding more items to the dictionary below.
    "*** YOUR CODE HERE ***"
    return {'name': name,
            'location': location,
            'categories': categories,
            'price': price,
            'reviews': reviews
            }

def restaurant_name(restaurant):
    return restaurant['name']

def restaurant_location(restaurant):
    return restaurant['location']

def restaurant_categories(restaurant):
    return restaurant['categories']

def restaurant_price(restaurant):
    return restaurant['price']

def restaurant_ratings(restaurant):
    """Return a list of ratings (numbers from 1 to 5)."""
    return [review_rating(x) for x in restaurant['reviews']]

### === +++ RESTAURANT ABSTRACTION BARRIER +++ === ###

def restaurant_num_ratings(restaurant):
    """Return the number of ratings for RESTAURANT."""
    return len(restaurant_ratings(restaurant))

def restaurant_mean_rating(restaurant):
    """Return the average rating for RESTAURANT."""
    return mean(restaurant_ratings(restaurant))