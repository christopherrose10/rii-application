import requests

books_api_url = 'https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview/books'
authors_api_url = 'https://p8doqtvi9f.execute-api.us-west-2.amazonaws.com/rii-dev-interview/authors'

booksResponse = requests.get(books_api_url)
books = booksResponse.json()

authorResponse = requests.get(authors_api_url)
authors = authorResponse.json()

print(books)
print(authors)
