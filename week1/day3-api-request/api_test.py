import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def check_status(status_code, expected_code):
    if status_code == expected_code:
        return f"[PASS] Status: {status_code}"
    else:
        return f"[FAIL] Expected {expected_code} but got {status_code}"

print("=" * 50)
print("  REST API TEST SUITE — Day 3")
print("  Using: jsonplaceholder.typicode.com")
print("=" * 50)

# ── TEST 1: GET a single post ──────────────────────
print("\nTEST 1: GET /posts/1")
response = requests.get(f"{BASE_URL}/posts/1")
print(check_status(response.status_code, 200))
data = response.json()
print(f"  Title: {data['title']}")
print(f"  User ID: {data['userId']}")

# ── TEST 2: GET all posts ──────────────────────────
print("\nTEST 2: GET /posts")
response = requests.get(f"{BASE_URL}/posts")
print(check_status(response.status_code, 200))
posts = response.json()
print(f"  Total posts returned: {len(posts)}")

# ── TEST 3: POST — create a new post ──────────────
print("\nTEST 3: POST /posts")
new_post = {
    "title": "QA Automation Test Post",
    "body": "This post was created by Monali's API test script",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(check_status(response.status_code, 201))
created = response.json()
print(f"  New post ID: {created['id']}")
print(f"  Title confirmed: {created['title']}")

# ── TEST 4: PUT — update a post ────────────────────
print("\nTEST 4: PUT /posts/1")
updated_post = {
    "id": 1,
    "title": "Updated Title by QA Script",
    "body": "Updated body content",
    "userId": 1
}
response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print(check_status(response.status_code, 200))
print(f"  Updated title: {response.json()['title']}")

# ── TEST 5: DELETE a post ──────────────────────────
print("\nTEST 5: DELETE /posts/1")
response = requests.delete(f"{BASE_URL}/posts/1")
print(check_status(response.status_code, 200))
print(f"  Response body: {response.json()}")

# ── TEST 6: GET non-existent post (404 test) ───────
print("\nTEST 6: GET /posts/99999 (expect 404)")
response = requests.get(f"{BASE_URL}/posts/99999")
print(check_status(response.status_code, 404))

# ── SUMMARY ────────────────────────────────────────
print("\n" + "=" * 50)
print("  All 6 tests completed")
print("=" * 50)