from pyramid.config import Configurator
import nflpool.controllers.home_controller as home
import nflpool.controllers.account_controller as account
import nflpool.controllers.admin_controller as admin
import nflpool.controllers.standings_controller as standings
import nflpool.controllers.picks_controller as picks
from nflpool.data.dbsession import DbSessionFactory
import os
import nflpool


def init_db(config):
    top_folder = os.path.dirname(nflpool.__file__)
    rel_folder = os.path.join('db', 'nflpooldb.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    init_includes(config)
    init_routing(config)
    init_db(config)
    return config.make_wsgi_app()


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, account.AccountController, 'account')
    add_controller_routes(config, admin.AdminController, 'admin')
    add_controller_routes(config, standings.StandingsController, 'standings')
    add_controller_routes(config, picks.PicksController, 'picks')

    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{season}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')

