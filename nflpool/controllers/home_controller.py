import pyramid_handlers
import nflpool.static_cache

class ControllerBase:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = nflpool.static_cache.build_cache_id

class HomeController(ControllerBase):
    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {
            'value': 'HOME',
        }

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {
            'value': 'ABOUt',

        }

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {
            'value': 'CONTACT',

        }