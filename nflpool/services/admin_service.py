from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account


def admin_check():
    session = DbSessionFactory.create_session()
    su__query = session.query(Account.id).filter(Account.is_super_user == 1) \
        .filter(Account.id == self.logged_in_user_id).first()
    print(su__query)

    if not su__query[0] == self.logged_in_user_id:
        print("You must be an administrator to view this page")
        self.redirect('/home')