'''
DIRECTIONS
==========

1. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    [ "Sally", [ "lollipop", "bubble gum", "laffy taffy" ]],
    [ "Bob", [ "milky way", "licorice", "lollipop" ]],
	[ "Arlene", [ "chocolate bar", "milky way", "laffy taffy" ]],
	[ "Carlie", [ "nerds", "sour patch kids", "laffy taffy" ]]
]

2. In `get_friends_who_like_specific_candy()`, return friends who like lollipops.

3. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

4. Write tests for all of the functions in this exercise.

'''

#  data = friend_favorites
def create_new_candy_data_structure(data):
    
# create function that describes  differnet kinds of candy paired with a LIST of friends that like that candy
    candy_types = []
    


# this makes a list of all the candy types
    for friend in data:
        for candy in friend[1]:
            if candy not in candy_types:
                candy_types.append(candy)

    candy_dict = {}
    friends_list = []
# make each value in candy types a key in candy dict
    for candy in candy_types:
        candy_dict[candy] = []


    for candy in candy_types:
        for friend in data:
            if candy in friend[1]:
                candy_dict[candy].append(friend[0])
    return candy_dict









# def get_friends_who_like_specific_candy(data, candy_name):
#     # return friends who like lollipops


# def create_candy_set(data):
#     # return all candy sets made in the first function
    
