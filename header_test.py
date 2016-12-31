from http.client import HTTPSConnection
from base64 import b64encode
# This sets up the https connection
c = HTTPSConnection("www.mysportsfeeds.com/api/feed/pull/nfl/2016-2017-regular/playoff_team_standings.json?teamstats")
# we need to base 64 encode it
# and then decode it to acsii as python 3 stores it as a byte string
userAndPass = b64encode(b"prcutler:r6RWPADULVd3wj").decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }
# then connect
c.request('GET', '/', headers=headers)
# get the response back
res = c.getresponse()
# at this point you could check the status etc
# this gets the page text
# data = res.read()
print(res)
