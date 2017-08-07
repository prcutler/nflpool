from nflpool.viewmodels.viewmodelbase import ViewModelBase


class PlayerPicksViewModel(ViewModelBase):
    def __init__(self):
        self.afc_east_winner = None
        self.afc_east_second = None
        self.afc_north_winner = None
        self.afc_north_second = None
        self.user_id = None
        self.date = None
        self.season = None

    def from_dict(self, data_dict):
        self.afc_east_winner = data_dict.get('afc_east_first')
        self.afc_east_second = data_dict.get('afc_east_second')
        self.afc_north_winner = data_dict.get('afc_north_first')
        self.afc_north_second = data_dict.get('afc_north_second')
        self.user_id = data_dict.get('id')
        self.date = data_dict.get('date')
        self.season = data_dict.get('season')

