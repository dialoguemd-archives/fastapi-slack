def test_importing_version():
    from fastapi_slack import __version__

    assert isinstance(__version__, str)
