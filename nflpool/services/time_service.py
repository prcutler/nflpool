import pendulum


class TimeService:
    @staticmethod
    def get_time():
        """Create a service to get the time - there were too many instances of getting the current time in
        the codebase making testing difficult."""
        # Change now_time for testing
        # Use this one for production:
        # now_time = pendulum.now(tz=pendulum.timezone('America/New_York')).to_datetime_string()
        now_time = pendulum.now(tz=pendulum.timezone('America/New_York'))
        # Use this one for testing:
        # now_time = pendulum.create(2017, 10, 14, 13, 00, tz='America/New_York')

        return now_time
