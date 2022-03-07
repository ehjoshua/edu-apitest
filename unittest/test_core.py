
def test_version():
    from edu_apitest import __version__
    assert isinstance(__version__, str)