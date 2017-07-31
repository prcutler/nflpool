import pyramid_handlers
from nflpool.controllers.base_controller import BaseController
from nflpool.viewmodels.newalbumviewmodel import NewAlbumViewModel
from nflpool.services.albums_service import AlbumsService


class AdminController(BaseController):
    # GET /admin/new_album
    @pyramid_handlers.action(renderer='templates/admin/new_install.pt',
                             request_method='GET',
                             name='new_install')
    def new_install_get(self):
        vm = NewAlbumViewModel()
        return vm.to_dict()

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/admin/new_album.pt',
                             request_method='POST',
                             name='new_album')
    def new_album_post(self):
        vm = NewAlbumViewModel()
        vm.from_dict(self.request.POST)

        # might want to add this ;)
        # if not vm.validate():
        #     return vm.to_dict()

        # Insert album
        new_album = AlbumsService.create_album(vm.title, vm.year, vm.album_image,
                                               vm.price, vm.url, vm.track_titles)
        # log new album
        print("Created a new album with id {}".format(new_album.id))

        # redirect
        self.redirect('/albums')
