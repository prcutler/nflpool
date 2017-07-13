import nflpool.infrastructure.static_cache as static_cache
from nflpool.infrastructure.supressor import suppress
import pyramid.renderers


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id

        layout_render = pyramid.renderers.get_renderer('nflpool:templates/shared/_layout.pt')
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

    @suppress
    def dont_expose_as_web_action_base(self):
        print("Called dont_expose_as_web_action, what happened?")


