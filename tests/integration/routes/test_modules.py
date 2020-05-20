def test_get_module_failure(client):
    response = client.get("/modules/526ca59c-94da-4e33-96b1-ae6ff2610f0c")
    expected_response = {
        "error": {
            "message": "No such module.",
            "messages": {},
            "status": 404,
            "type": "Not Found",
        }
    }

    assert response.json == expected_response
    assert response.status == "404 NOT FOUND"


def test_post_module_success(client):
    data = {"module": {"code": "cs1010", "size": 1000}}
    response = client.post("/modules/", json=data)

    assert response.json["module"]["code"] == data["module"]["code"]
    assert response.json["module"]["size"] == data["module"]["size"]
    assert response.status == "201 CREATED"


def test_post_module_again_success(client):
    data = {"module": {"code": "cs1010", "size": 1000}}
    response = client.post("/modules/", json=data)

    assert response.json["module"]["code"] == data["module"]["code"]
    assert response.json["module"]["size"] == data["module"]["size"]
    assert response.status == "201 CREATED"
