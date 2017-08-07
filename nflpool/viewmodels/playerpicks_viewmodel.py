from nflpool.viewmodels.viewmodelbase import ViewModelBase


class PlayerPicksViewModel(ViewModelBase):
    def __init__(self):
        self.afc_east_first = None
        self.afc_east_second = None
        self.afc_east_last = None
        self.user_id = None
        self.date = None


    def from_dict(self, data_dict):
        self.afc_east_first = data_dict.get('afc_east_first')
        self.afc_east_second = data_dict.get('afc_east_second')
        self.afc_east_last = data_dict.get('afc_east_last')
        self.user_id = data_dict.get('id')
        self.date = data_dict.get('date')

