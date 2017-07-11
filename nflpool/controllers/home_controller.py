import pyramid_handlers
import nflpool.infrastructure.static_cache as static_cache


class HomeController:
    def __init__(self, request):
        self.request = request

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