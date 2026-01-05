from app import get_response


def test_response():
    result = get_response("Mangesh")
    assert "Mangesh" in result
