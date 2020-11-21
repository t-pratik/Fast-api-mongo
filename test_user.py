from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_user_get():
    # Wrong url
    # params missing
    response = client.get("/db/user_details",
                          params={"email": "string@test.com"})
    assert response.status_code == 200

    # What was this supposed to be?
    # assert response.json() == {"email": "string@test.com"}.json() == {"email": "string@test.com"}
