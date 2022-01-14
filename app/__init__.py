import requests

# api that displays books
books_api_url = 'https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview/books'

# api that displays authors
authors_api_url = 'https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview/authors'

# requests endpoint with GET call 
booksResponse = requests.get(books_api_url)
# displays as JSON object
books = booksResponse.json()

# requests endpoint with GET call 
authorResponse = requests.get(authors_api_url)
# displays as JSON object
authors = authorResponse.json()

print(books)
print(authors)
