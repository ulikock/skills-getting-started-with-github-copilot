
import pytest

def test_get_activities(client):
    # Arrange: (nenhuma preparação especial necessária)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 6
    for activity, details in data.items():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details


def test_signup_success(client):
    # Arrange
    email = "testuser@example.com"
    activity = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert "message" in response.json()


def test_signup_duplicate(client):
    # Arrange
    email = "duplicate@example.com"
    activity = "Chess Club"

    # Act
    response_first = client.post(f"/activities/{activity}/signup?email={email}")
    response_second = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response_first.status_code == 200
    assert response_second.status_code == 400
    assert "detail" in response_second.json()


def test_signup_activity_not_found(client):
    # Arrange
    email = "notfound@example.com"
    activity = "Nonexistent Activity"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 404
    assert "detail" in response.json()
