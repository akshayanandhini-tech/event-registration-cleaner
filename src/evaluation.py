from main import clean, check_facts, is_valid


test_cases = [
    {
        "id": 1,
        "entry": "Name: Priya K, Phone: 9840012345, Email: priya@gmail.com, Year: 2, Branch: CSE",
        "data": {
            "name": "Priya K",
            "phone": "9840012345",
            "email": "priya@gmail.com",
            "year": 2,
            "branch": "CSE"
        },
        "expected": "valid",
        "expected_phone": "9840012345"
    },

    {
        "id": 2,
        "entry": "Name: Arun, Phone: 9876543210, Year: 2, Branch: IT",
        "data": {
            "name": "Arun",
            "phone": "9876543210",
            "email": None,
            "year": 2,
            "branch": "IT"
        },
        "expected": "needs_fix",
        "expected_phone": "9876543210"
    },

    {
        "id": 3,
        "entry": "Name: Kavin, Phone: 12345, Email: kavin@gmail.com, Year: 1, Branch: ECE",
        "data": {
            "name": "Kavin",
            "phone": "12345",
            "email": "kavin@gmail.com",
            "year": 1,
            "branch": "ECE"
        },
        "expected": "needs_fix",
        "expected_phone": None
    },

    {
        "id": 4,
        "entry": "Name: Meena, Phone: 9876543211, Email: meena@gmail.com, Year: 3, Branch: ABC",
        "data": {
            "name": "Meena",
            "phone": "9876543211",
            "email": "meena@gmail.com",
            "year": 3,
            "branch": "ABC"
        },
        "expected": "needs_fix",
        "expected_phone": "9876543211"
    },

    {
        "id": 5,
        "entry": "Name: Rahul, Phone: 9876543210, Email: rahul2@gmail.com, Year: 2, Branch: CSE",
        "data": {
            "name": "Rahul",
            "phone": "9876543210",
            "email": "rahul2@gmail.com",
            "year": 2,
            "branch": "CSE"
        },
        "expected": "duplicate",
        "expected_phone": "9876543210"
    }
]


seen_phones = {}
passed = 0


for test in test_cases:

    print("\nTest:", test["id"])

    # Run fact check
    check_facts(test["entry"], test["data"])

    # Clean data
    cleaned = clean(test["data"])

    phone = cleaned.get("phone")

    # Determine status
    if phone and phone in seen_phones:
        actual_status = "duplicate"

    elif is_valid(cleaned):
        actual_status = "valid"

    else:
        actual_status = "needs_fix"

    # Save first occurrence
    if phone and phone not in seen_phones:
        seen_phones[phone] = test["id"]

    actual_phone = phone

    print("Expected status:", test["expected"])
    print("Actual status:", actual_status)
    print("Expected phone:", test["expected_phone"])
    print("Actual phone:", actual_phone)

    if (
        actual_status == test["expected"]
        and actual_phone == test["expected_phone"]
    ):
        print("Result: PASS")
        passed += 1

    else:
        print("Result: FAIL")


print("\nTOTAL TESTS:", len(test_cases))
print("PASSED:", passed)
print("FAILED:", len(test_cases) - passed)