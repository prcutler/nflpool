import sqlalchemy
import sqlalchemy.orm
from nflpool.data.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences
import nflpool.data.account
# noinspection PyUnresolvedReferences
import nflpool.data.activeplayers
# noinspection PyUnresolvedReferences
import nflpool.data.seasoninfo
# noinspection PyUnresolvedReferences
import nflpool.data.picks
# noinspection PyUnresolvedReferences
import nflpool.data.points
# noinspection PyUnresolvedReferences
import nflpool.data.teaminfo
# noinspection PyUnresolvedReferences
import nflpool.data.weekly_stats
# noinspection PyUnresolvedReferences
import nflpool.data.passwordreset



class DbSessionFactory:
    factory = None

    # Start a database session at app startup
    @staticmethod
    def global_init(db_file):
        if DbSessionFactory.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return DbSessionFactory.factory()
