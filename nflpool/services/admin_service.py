from nflpool.data.dbsession import DbSessionFactory
from nflpool.data.account import Account


'''Create a check that only the user who is True in the AccountInfo database with is_superuser can access
the admin pages.  Make sure nflpool/data/secret.py has an email assigned that matches the user during registration'''


def admin_check():
    session = DbSessionFactory.create_session()
    su__query = session.query(Account.id).filter(Account.is_super_user == 1) \
        .filter(Account.id == self.logged_in_user_id).first()
    print(su__query)

    if not su__query[0] == self.logged_in_user_id:
        print("You must be an administrator to view this page")
        self.redirect('/home')


class AccountService:
    @staticmethod
    def get_all_accounts():
        session = DbSessionFactory.create_session()
        account_list = session.query(Account).all()

        return account_list
