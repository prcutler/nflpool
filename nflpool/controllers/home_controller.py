import pyramid_handlers
from nflpool.controllers.base_controller import BaseController


class HomeController(BaseController):
    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'value': 'HOME'}

    @pyramid_handlers.action(renderer='templates/home/about.pt')
    def about(self):
        return {'value': 'ABOUt'}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'value': 'CONTACT'}

    @pyramid_handlers.action(renderer='templates/home/credits.pt')
    def credits(self):
        return {'value': 'IMAGES'}

    @pyramid_handlers.action(renderer='templates/home/rules.pt')
    def rules(self):
        return {'value': 'RULES'}