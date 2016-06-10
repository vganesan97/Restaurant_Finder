import urllib2
import copy
import json
from twilio.rest import TwilioRestClient 



locu_api='30bf9d23736f562297e8c86b2b933214e7d119ea'
account_sid_twilio="{{AC382aa7d2a753e94aea2f916a7746ca2f}}"
auth_token_twilio="[02bb57b080d6b66a99a8033a8b7c10f3]"

client = TwilioRestClient(account='AC382aa7d2a753e94aea2f916a7746ca2f',
                              token='02bb57b080d6b66a99a8033a8b7c10f3')

def locusearch(city, region, zipp, category):
	api_key=locu_api
	url='https://api.locu.com/v1_0/venue/search/?'
	locality=city.replace(' ','%20')
	final_url=url+ "locality=" + locality + "&region"+region+ "&postal_code="+ zipp + "&category=" +category+ "&api_key=" + api_key
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj) 
	x=[]
	s=""
	client = TwilioRestClient(account='AC382aa7d2a753e94aea2f916a7746ca2f',token='02bb57b080d6b66a99a8033a8b7c10f3')
	for item in data['objects']:
		s+=item['name']+ " "+item['phone'] + "\n"
	client.messages.create(
		from_="+12155844319",
		to="(609) 462-4702", 
		body=s
	)
locusearch('San Jose', 'CA', '95135', 'restaurant')