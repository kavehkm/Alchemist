# alchemy
from sqlalchemy import create_engine

# internal
from src import settings
from src.models import Base


__engine = None


def get():
    # access to outer __engine
    global __engine
    # check for __engine:
    # if __engine did not initialize
    # 1) create engine and initialize __engine
    # 2) emit DDL into database
    if __engine is None:
        # extract required values from settings
        dsn = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(
            settings.USER,
            settings.PASSWORD,
            settings.IP,
            settings.PORT,
            settings.DATABASE,
            settings.CHARSET,
        )
        # create engine
        __engine = create_engine(dsn, echo=settings.ECHO)
        # emit DDL into database
        Base.metadata.create_all(__engine)

    return __engine
