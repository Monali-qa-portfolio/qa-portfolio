## Day 3 — REST API Testing with Python

**Topic:** HTTP methods, status codes, JSON responses  
**Tools:** Python 3, requests library  
**API Used:** jsonplaceholder.typicode.com (free fake REST API)  

Install: `pip3 install requests`  
Run: `python3 api_test.py`

## Tests covered
- GET single resource
- GET all resources
- POST — create new resource
- PUT — update existing resource
- DELETE — remove resource
- GET non-existent resource (404 test)

## What I learned
- HTTP methods: GET, POST, PUT, DELETE
- Status codes: 200, 201, 404
- Parsing JSON responses with .json()
- Building a reusable check_status() function
- Asserting expected vs actual status codes