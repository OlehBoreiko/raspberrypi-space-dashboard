from script import app

def test_home():
    with app.test_client() as client:
        res = client.get("/")
        assert res.status_code == 200
        assert b"Space API" in res.data

def test_apod():
    with app.test_client() as client:
        res = client.get("/apod")
        assert res.status_code == 200
        assert res.is_json
