import random  # simulating pass/fail since we have no real server yet

def check_endpoints(filepath):
    print("=" * 45)
    print("  API ENDPOINT STATUS CHECK")
    print("  QA Automation — Day 1 Practice")
    print("=" * 45)

    with open(filepath, "endpoint.txt") as file:
        endpoints = [line.strip() for line in file if line.strip()]

    pass_count = 0
    fail_count = 0

    for endpoint in endpoints:
        # Day 1: simulated result. Day 3 you'll replace this with real requests
        status = random.choice(["PASS", "PASS", "PASS", "FAIL"])  # weighted
        
        if status == "PASS":
            pass_count += 1
            print(f"  [PASS]  {endpoint}")
        else:
            fail_count += 1
            print(f"  [FAIL]  {endpoint}  <-- investigate")

    print("=" * 45)
    print(f"  Total: {len(endpoints)}  |  PASS: {pass_count}  |  FAIL: {fail_count}")
    print("=" * 45)

check_endpoints("endpoints.txt")