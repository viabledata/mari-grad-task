
class DevConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///people.db"


class TestingConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///./testdb.sqlite"


config = {
    "testing": TestingConfig,
    "dev": DevConfig
}
