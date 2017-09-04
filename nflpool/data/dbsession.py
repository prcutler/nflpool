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
import nflpool.data.player_picks
# noinspection PyUnresolvedReferences
import nflpool.data.points
# noinspection PyUnresolvedReferences
import nflpool.data.teaminfo
# noinspection PyUnresolvedReferences
import nflpool.data.passwordreset
# noinspection PyUnresolvedReferences
import nflpool.data.picktypes
# noinspection PyUnresolvedReferences
import nflpool.data.conferenceinfo
# noinspection PyUnresolvedReferences
import nflpool.data.divisioninfo
# noinspection PyUnresolvedReferences
import nflpool.data.pick_type_points
# noinspection PyUnresolvedReferences
import nflpool.data.picktypes


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
