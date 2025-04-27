import requests

api_key = "28d27ce2b0454fe78a9cbf3d29ae492c"

url = "https://newsapi.org/v2/everything?" \
"q=tesla&from=2025-03-27&sortBy=publishedAt&apiKey=" \
"28d27ce2b0454fe78a9cbf3d29ae492c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
for article in content["articles"]:
    print (article["title"])
    print (article["description"])
    print (article["author"])