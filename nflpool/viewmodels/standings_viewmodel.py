from nflpool.viewmodels.viewmodelbase import ViewModelBase


class StandingsViewModel(ViewModelBase):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.total_points = None
        self.player_id = None
        self.is_get = True

    def from_dict(self, data_dict):
        self.first_name = data_dict.get('first_name')
        self.last_name = data_dict.get('last_name')
        self.total_points = data_dict.get('total_points')
        self.player_id = data_dict.get('id')
