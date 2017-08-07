import pyramid_handlers
from nflpool.controllers.base_controller import BaseController


class HomeController(BaseController):
    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/credits.pt')
    def credits(self):
        return {}

    @pyramid_handlers.action(renderer='templates/home/rules.pt')
    def rules(self):
        return {}
