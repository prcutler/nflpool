from nflpool.viewmodels.viewmodelbase import ViewModelBase


class PlayerPicksViewModel(ViewModelBase):
    def __init__(self):
        self.afc_east_winner_pick = None
        self.afc_east_second = None
        self.afc_east_last = None
        self.afc_north_winner_pick = None
        self.afc_north_second = None
        self.afc_north_last = None
        self.afc_south_winner_pick = None
        self.afc_south_second = None
        self.afc_south_last = None
        self.afc_west_winner_pick = None
        self.afc_west_second = None
        self.afc_west_last = None
        self.nfc_east_winner_pick = None
        self.nfc_east_second = None
        self.nfc_east_last = None
        self.nfc_north_winner_pick = None
        self.nfc_north_second = None
        self.nfc_north_last = None
        self.nfc_south_winner_pick = None
        self.nfc_south_second = None
        self.nfc_south_last = None
        self.nfc_west_winner_pick = None
        self.nfc_west_second = None
        self.nfc_west_last = None
        self.afc_qb_pick = None
        self.nfc_qb_pick = None
        self.user_id = None

    def from_dict(self, data_dict):
        self.afc_east_winner_pick = data_dict.get('afc_east_winner_pick')
        self.afc_east_second = data_dict.get('afc_east_second')
        self.afc_east_last = data_dict.get('afc_east_last')
        self.afc_north_winner_pick = data_dict.get('afc_north_winner_pick')
        self.afc_north_second = data_dict.get('afc_north_second')
        self.afc_north_last = data_dict.get('afc_north_last')
        self.afc_south_winner_pick = data_dict.get('afc_south_winner_pick')
        self.afc_south_second = data_dict.get('afc_south_second')
        self.afc_south_last = data_dict.get('afc_south_last')
        self.afc_west_winner_pick = data_dict.get('afc_west_winner_pick')
        self.afc_west_second = data_dict.get('afc_west_second')
        self.afc_west_last = data_dict.get('afc_west_last')
        self.nfc_east_winner_pick = data_dict.get('nfc_east_winner_pick')
        self.nfc_east_second = data_dict.get('nfc_east_second')
        self.nfc_east_last = data_dict.get('nfc_east_last')
        self.nfc_north_winner_pick = data_dict.get('nfc_north_winner_pick')
        self.nfc_north_second = data_dict.get('nfc_north_second')
        self.nfc_north_last = data_dict.get('nfc_north_last')
        self.nfc_south_winner_pick = data_dict.get('nfc_south_winner_pick')
        self.nfc_south_second = data_dict.get('nfc_south_second')
        self.nfc_south_last = data_dict.get('nfc_south_last')
        self.nfc_west_winner_pick = data_dict.get('nfc_west_winner_pick')
        self.nfc_west_second = data_dict.get('nfc_west_second')
        self.nfc_west_last = data_dict.get('nfc_west_last')
        self.afc_qb_pick = data_dict.get('afc_qb_pick')
        self.nfc_qb_pick = data_dict.get('nfc_qb_pick')
        self.user_id = data_dict.get('user_id')
