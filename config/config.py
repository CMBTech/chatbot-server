import os


class Base:
    """ base config """


class Development(Base):
    """ development config """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///dev_db"


class Testing(Base):
    """ test environment config """

    TESTING = True
    DEBUG = True
    # use a separate db
    SQLALCHEMY_DATABASE_URI = "postgresql:///my_test_db"


class Production(Base):
    """ production config """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://dfndxkpazglnkcdf:<3TNiC(90|9Pnm!5x9ht|[y?CTNpaQ6z@102.134.147.233:32761/qogjifhbhglibossnqmtuivu'
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")


app_config = {"development": Development, "testing": Testing, "production": Production}
