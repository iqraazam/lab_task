"""
Test Script for Pakistan House Price Prediction API
"""
import requests
import json

# API endpoint
API_URL = "http://127.0.0.1:5000/api/predict"

# Sample test data
test_cases = [
    {
        "name": "Luxury House in Islamabad",
        "data": {
            "property_type": "House",
            "city": "Islamabad",
            "province_name": "Islamabad Capital",
            "latitude": 33.6844,
            "longitude": 73.0479,
            "baths": 4,
            "bedrooms": 5,
            "Area Type": "Kanal",
            "Area Size": 2.0,
            "Area Category": "1-5 Kanal"
        }
    },
    {
        "name": "Small Flat in Rawalpindi",
        "data": {
            "property_type": "Flat",
            "city": "Rawalpindi",
            "province_name": "Punjab",
            "latitude": 33.5651,
            "longitude": 73.0169,
            "baths": 2,
            "bedrooms": 2,
            "Area Type": "Marla",
            "Area Size": 5.0,
            "Area Category": "5-10 Marla"
        }
    },
    {
        "name": "Medium House in Lahore",
        "data": {
            "property_type": "House",
            "city": "Lahore",
            "province_name": "Punjab",
            "latitude": 31.5204,
            "longitude": 74.3587,
            "baths": 3,
            "bedrooms": 4,
            "Area Type": "Marla",
            "Area Size": 10.0,
            "Area Category": "10-15 Marla"
        }
    }
]

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get("http://127.0.0.1:5000/health")
        print("✓ Health Check:")
        print(json.dumps(response.json(), indent=2))
        print()
        return True
    except Exception as e:
        print(f"✗ Health check failed: {e}")
        return False

def test_prediction(test_case):
    """Test a prediction"""
    try:
        response = requests.post(API_URL, json=test_case["data"])
        if response.status_code == 200:
            result = response.json()
            print(f"✓ {test_case['name']}:")
            print(f"  Predicted Price: {result['formatted']}")
            print(f"  Raw Value: PKR {result['prediction']:,.0f}")
            print()
            return True
        else:
            print(f"✗ {test_case['name']} failed:")
            print(f"  Status Code: {response.status_code}")
            print(f"  Response: {response.text}")
            print()
            return False
    except Exception as e:
        print(f"✗ {test_case['name']} error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 70)
    print("Pakistan House Price Prediction - API Test Suite")
    print("=" * 70)
    print()
    
    # Test health endpoint
    if not test_health():
        print("⚠ Server may not be running. Start with: python housepk_app.py")
        exit(1)
    
    # Test predictions
    print("Testing Predictions:")
    print("-" * 70)
    success_count = 0
    for test_case in test_cases:
        if test_prediction(test_case):
            success_count += 1
    
    print("=" * 70)
    print(f"Results: {success_count}/{len(test_cases)} tests passed")
    print("=" * 70)
