from pyramid.view import view_config
import nflpool.infrastructure.static_cache


@view_config(route_name='index', renderer='templates/index.pt')
def index(_):
    return extend_model({'project': 'nflpool'})

def extend_model(model_dict):
    model_dict['build_cache_id'] = nflpool.static_cache.build_cache_id
    return model_dict