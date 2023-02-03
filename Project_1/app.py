
"""
Task:
1-Add new mvoies to my collection ( so I can keep track of my movies)
List all the movies in my collection ( so I can see what movies I already have)
Find a mvoie by using the movie tittle ( so I can locate a specific movie)

2-show the user a menu and let them pick an option
3-implement each requirement in turn, each as a separate function

4-stop running the program when they type 'q' in the menu

Hints:
where to store movies?
1- Store the movies into a list movies=[]
2- what we store for each movie , dict = {title, director, release year} ex:

movies=[]
title=input("Enter the movie title: ")
director= input("Enter the movie director: ")
year=input("Enter the movie release year:  )

movies.append({
    'title':title,
    'director':director,
    'year':year
})

3- MENU_PROMPT: "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a mvoie by tittle, or 'q' to quit:
selection=input(MENU_PROMPT)

while selection !='q':
    if selection=='a':
        pass
    elif selection =='l'
        pass
    elif selection =='f':
        pass
    else:
        print("Unknown command. Please try again")

    selection=input(MENU_PROMPT)

vault /voult/
"""

# Variables:
selection="" # Holds the option menu given by user
movies=[] # Holds the dictionary movies. Info for each movie

# Functions:
def menu():
    print("""
    Welcome to your vault movies!
    Please select one of the following options:
    a) Add Movies - Press keyword 'a'
    l) See your movies - Press keyword 'l'
    f) Find a movie by tittle - keyword Press 'f'
    q) Quit - Press keyword 'q'

    """)

# Function that stores a new movie
def add_movie():
    title=input("Enter the movie tittle: ")
    director= input("Enter the movie director: ")
    year=input("Enter the movie release year:  ")

    # Adding the previous info into "movies" list

    movies.append({
        'title':title,
        'director':director,
        'year':year
    })

    print("Process added successfully...")

# Function that shows the list of movies already stored 
def see_movies_stored():
    for movie in movies:
        print(f"Title: {movie['title']}")
        print(f"Director: {movie['director']}")
        print(f"Year: {movie['year']}")
        print("...End...\n")


# Function that look for title name provided by user: 
def find_movie():
    print("Search a movie into your Vault:")
    title=input("Provide a title Name: ")

    for movie in movies:
        if movie['title'] == title:
            print(movie)
        else:
            print("There isnot movie with similar title name")


# Task
while selection !='q':
    menu()
    selection = input("What is your choise?: ")

    if selection =='a':
        add_movie()
    
    elif selection =='l':
        see_movies_stored()

    elif selection=='f':
        find_movie()

    elif selection=='q':
        print("Quitting from vault movies")

    else:
        print("Unknown command. Please try again")
