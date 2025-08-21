import time

def test_list_item_is_successful(api_client):
    """
    Verify the API can list a new item for sale.
    Checks for a successful response and confirms a ListingId is returned.
    """
    # Arrange: Create a payload for the new item.
    # Use a timestamp to ensure the title is unique for each test run.
    unique_timestamp = int(time.time())
    item_payload = {
        "Category": "3413-",  # A valid sandbox category
        "Title": f"My Test item {unique_timestamp}",
        "Description": ["This is test data."],
        "Duration": 7,
        "StartPrice": 50.00,
        "Pickup": 1, # Buyer must pick up
        "PaymentMethods": [1, 2], # 1 = Bank Deposit, 2 = Cash
        "ShippingOptions": [
            {
                "Type": 1 # Buyer must pick up
            }
        ]
    }

    # Act: Make the API call to list the item
    response = api_client.list_item(item_payload)
    
    # FOR DEBUGGING
    if response.status_code != 200:
        print("\nAPI Error Response:", response.json()) # <-- This line is now correctly indented

    # Assert: Check the response
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    
    response_data = response.json()
    assert response_data.get("Success") is True, "The 'Success' key should be True"
    assert "ListingId" in response_data, "The response should contain a 'ListingId'"
    assert isinstance(response_data["ListingId"], int), "The 'ListingId' should be an integer"