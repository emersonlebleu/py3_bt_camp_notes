#optional lesson on http, I think one of the more interesting topics
#we will be using a package that allows us to make requests

#DNS lookup --> computer makes request to server --> server processes the request --> surver issues a response

#----request headers----
#accept: what type of response we will accept back (html, json, xml etc.)
#cache-control: specifies caching behavior
#user-agent: information about the software used to make the request

#----response headers----
#access-control-allow-orgin: specify domains that can make requests
#allowed: HTTP verbs that are allowed in requests

#---Status---
#2 Success
#3 Redirect
#4 client error
#5 Server error

#----HTTP Verbs----
#GET: 
#trying to retrieve data
#no side effects
#can be cached & bookmarked

#Post:
#trying to write data
#can have side effects
#cannot be cached or bookmarked

#----API----
#stands for --> application programming interface
#allow us to get data without needing to understand how it works 
#.json (javascript object notation) seems to pull only the data on the page without the structure
#xml used to be the standard but it really isnt at this point

#----Requests----
from requests import get,post
from random import randint

url = "https://icanhazdadjoke.com/search"

loop_yes = "Yes"

while loop_yes[0] == "Y" or loop_yes[0] == "y":
    category = input("What to search? ")
    
    response = get(
        url,
        headers={"accept":"application/json"},
        params={"term":category})
    
    data = (response.json())
    results = data["results"]

    if len(results) == 0:
        print(f"Sorry no jokes for {category}.")
    elif len(results) > 1:
        num = randint(0,len(results))
        print(results[num]["joke"])
    else:
        print(results[0])
    loop_yes = input("Another? ")
