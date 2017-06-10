# Author: Rohit Gupta
# Date: February 10, 2017
# Version: 1.0

import datetime


def main():
    print_header()
    print_lists()


def print_header():
    print("------------------------------------")
    print("         WELCOME TO THE LISTS")
    print("------------------------------------")
    print("")
    user_name = input("Please input your name :")
    current_time = datetime.datetime.now()
    print("Welcome to the Application {}".format(user_name))
    print("Current system time is: " + (current_time.strftime("%A, %d %B, %Y")))


def print_lists():
    movies = ["The Holy Grail", 1975, "Terry Jones and Terry Gilliam", 91,["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
    #print(movies)
    #print(len(movies))

    #if isinstance(movies, list):
    for each_item in movies:
        if isinstance(each_item, list):
            print("Found a List at level 0")
            print(each_item)
            for list_level in each_item:
                if isinstance(list_level, list):
                    print("Found a list level at 1")
                    print(list_level)
                    for list_level_2 in list_level:
                        if isinstance(list_level_2, list):
                            print("Found a list at level 2")

        else:
         print(each_item)


    #cast = ["Cleese", "Palin", "Jones", "Idle", "Gilliam"]
    #print(cast)

if __name__ == '__main__':
    main()
