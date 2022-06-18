"""
Dad Joke:  A program that fetches (called requests in python) a JSON data.  In this case, we are puling dad jokes.  
Obtain user input on a topic and the program filters the joke based on the topic.
"""

from random import randint
import requests

url = "https://icanhazdadjoke.com/search"

logo = """
 ____              _       _         _            _____   ___    ___    ___  
|  _ \   __ _   __| |     | |  ___  | | __  ___  |___ /  / _ \  / _ \  / _ \ 
| | | | / _` | / _` |  _  | | / _ \ | |/ / / _ \   |_ \ | | | || | | || | | |
| |_| || (_| || (_| | | |_| || (_) ||   < |  __/  ___) || |_| || |_| || |_| |
|____/  \__,_| \__,_|  \___/  \___/ |_|\_\ \___| |____/  \___/  \___/  \___/ 
   
"""

print(logo)

input_topic = input("Let me tell you a joke!  Give me a topic: ")

if input_topic:
    # the params below makes it equivalent to typing in address bar the following:
    # "https://icanhazdadjoke.com/search?term=input_topic"
    res = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": input_topic}
    )

    data = res.json()
    #print(data)

    total_jokes = data["total_jokes"]
    search_term = data["search_term"]

    if total_jokes == 1:
        print(f"I've got one joke about {search_term}.  Here it is:")
        print(data["results"][0]["joke"])
    elif total_jokes > 1:
        indx = randint(1, total_jokes)
        #print(indx)
        print(f"I've got {total_jokes} jokes about {search_term}.  Here is one:")
        print(data["results"][indx-1]["joke"])
    else:
        print(f"Sorry, I don't have any jokes about about {search_term}!  Please try again.")


    ##Debug data
    #print(data["results"])
    #print(data["joke"])
    #print(f"status: {data['status']}")
else:
    print("You must give me a topic.  Try again.")

"""
Typical Result ... example for search term = "snow"
{
'results': [
    {'id': '9xPCt411ojb', 'joke': 'What did one snowman say to the other snow man? Do you smell carrot?'},
    {'id': 'M7ElyAQCAd', 'joke': 'How was the snow globe feeling after the storm? A little shaken.'},
    {'id': '6EdFBAsrcpb', 'joke': 'How do you find Will Smith in the snow?  Look for fresh prints.'},
    {'id': 'W8MClVvXSf', 'joke': 'I needed a password eight characters long so I picked Snow White and the Seven Dwarfs.'},
    {'id': 'PZgyPmjb2ob', 'joke': 'What do you get when you cross a snowman with a vampire? Frostbite.'},
    {'id': 'C59hNRCdUnb', 'joke': 'What do you call an old snowman? Water.'}
]
    
'search_term': 'snow',
'status': 200,
'total_jokes': 6,
'total_pages': 1,
}

"""
