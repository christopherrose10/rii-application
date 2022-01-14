import requests
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

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

yearCurrent = datetime.today()

# list that contains authors and the book they could NOT have written
listOfNotMyBooks = []

# loop through each author 
for i in authors:
    # dict that will hold author
    resultObj = {}

    # stores authors name
    authorName = str(i['name']) + '(could not have written these books)'
    # stores authors age
    age = int(i['age'])
    # calculates and stores authors birth year by subtracting their age from current year
    birthYear = yearCurrent - relativedelta(years=age)
    # calculates and stores when author was 10
    authorTenYrsOld = birthYear + relativedelta(years=10)

    # pushes author's name as key to resultObj dict... empty list as value will be filled with books
    resultObj[authorName] = []

    print(authorTenYrsOld)

    # pushes each dict containing author to 'listOfNotMyBooks' list
    listOfNotMyBooks.append(resultObj)

print(listOfNotMyBooks)

