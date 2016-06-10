import urllib2
import copy
import json
from twilio.rest import TwilioRestClient 



locu_api='api token'
account_sid_twilio="{{sid}}"
auth_token_twilio="[token]"

def locusearch(city, region, zipp, category):
	api_key=locu_api
	url='https://api.locu.com/v1_0/venue/search/?'
	locality=city.replace(' ','%20')
	final_url=url+ "locality=" + locality + "&region"+region+ "&postal_code="+ zipp + "&category=" +category+ "&api_key=" + api_key
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj) 
	s=""
	client = TwilioRestClient(account='sid',token='token')
	for item in data['objects']:
		s+=item['name']+ " " +item['phone'] + "\n"
	client.messages.create(
		from_="twilio number",
		to="your number", 
		body=s
	)