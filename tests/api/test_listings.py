# Tests for the 'Retrieve Latest Listings' API
def test_get_latest_listings_is_successful(api_client):
    """
    Verify the API can retrieve the latest listings.
    Prints the results to the console.
    """
    # Act: Make the API call
    response = api_client.get_latest_listings()

    # Assert: Check the response status
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"

    response_data = response.json()

    # --- Print the results ---
    print(f"\nFound {response_data['TotalCount']} total listings:")
    for listing in response_data['List']:
        print(f"  - ID: {listing['ListingId']}, Title: {listing['Title']}")
    # -------------------------

    # Assert: Check the response data structure
    assert "List" in response_data, "The 'List' key was not found in the response"
    assert isinstance(response_data["List"], list), "The 'List' value should be a list"