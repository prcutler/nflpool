from nflpool.viewmodels.viewmodelbase import ViewModelBase


class PlayerPicksViewModel(ViewModelBase):
    def __init__(self):
        self.afc_east_winner = None
        self.afc_east_second = None
        self.afc_north_winner = None
        self.afc_north_second = None
#        self.user_id = None

    def from_dict(self, data_dict):
        self.afc_east_winner = data_dict.get('afc_east_winner_pick')
        self.afc_east_second = data_dict.get('afc_east_second')
        self.afc_north_winner = data_dict.get('afc_north_winner_pick')
        self.afc_north_second = data_dict.get('afc_north_second')
#        self.user_id = data_dict.get('id')
