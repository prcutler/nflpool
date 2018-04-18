import requests
import json
import nflpool.data.secret as secret


class SlackService:
    @staticmethod
    def send_message(message_string):
        """
        Set the webhook_url to the one provided by Slack when you create the webhook
        at https://my.slack.com/services/new/incoming-webhook/
        """

        slack_webhook_url = secret.slack_webhook_url
        slack_data = {'text': message_string}

        response = requests.post(slack_webhook_url, data=json.dumps(slack_data),
                                 headers={'Content-Type': 'application/json'})
        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text))
