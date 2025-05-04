from settings import Settings


def test_settings_load_from_test_env():
    """
    Test if settings are loaded correctly from the .env.test file via pytest-dotenv.
    """
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyApp_Test"
    assert settings.API_KEY == "dummy_key"
