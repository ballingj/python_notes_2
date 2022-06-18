import requests

url = "https://icanhazdadjoke.com/search"

# the params below makes it equivalent to typing in address bar the following:
# "https://icanhazdadjoke.com/search?term=cat&limit=1"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)

data = res.json()

# print(data)
print(data["results"])

# print(data["joke"])
# print(f"status: {data['status']}")


"""
{'current_page': 1, 'limit': 20, 'next_page': 1, 'previous_page': 1, 'results': [{'id': '8UnrHe2T0g', 'joke': '‘Put the cat out’ … ‘I didn’t realize it was on fire'}, {'id': 'iGJeVKmWDlb', 'joke': 'My cat was just sick on the carpet, I don’t think it’s feline well.'}, {'id': 'daaUfibh', 'joke': 'Why was the big cat disqualified from the race? Because it was a cheetah.'}, {'id': 'AQn3wPKeqrc', 'joke': 'It was raining cats and dogs the other day. I almost stepped in a poodle.'}, {'id': 'O7haxA5Tfxc', 'joke': 'Where do cats write notes?\r\nScratch Paper!'}, {
    'id': '1wkqrcNCljb', 'joke': "Did you know that protons have mass? I didn't even know they were catholic."}, {'id': 'BQfaxsHBsrc', 'joke': 'What do you call a pile of cats?  A Meowtain.'}, {'id': 'TS0gFlqr4ob', 'joke': 'What do you call a group of disorganized cats? A cat-tastrophe.'}, {'id': '39Etc2orc', 'joke': 'Why did the man run around his bed? Because he was trying to catch up on his sleep!'}, {'id': '0wcFBQfiGBd', 'joke': 'Did you hear the joke about the wandering nun? She was a roman catholic.'}], 'search_term': 'cat', 'status': 200, 'total_jokes': 10, 'total_pages': 1}
"""
