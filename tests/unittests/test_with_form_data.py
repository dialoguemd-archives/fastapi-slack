def test_with_form_data():
    from fastapi_slack import with_form_data

    assert with_form_data(b"param1=1&param2=abc") == {
        "param1": "1",
        "param2": "abc",
    }
