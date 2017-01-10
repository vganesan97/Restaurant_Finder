import urllib2
import copyr 
import json
from twilio.rest import TwilioRestClient 



locu_api='30bf9d23736f562297e8c86b2b933214e7d119ea'
account_sid_twilio="{{AC382aa7d2a753e94aea2f916a7746ca2f}}"
auth_token_twilio="[02bb57b080d6b66a99a8033a8b7c10f3]"



def locuserch(query):
	api_key=locu_api
	url='https://api.locu.com/v1_0/venue/search/?'
	locality=query.replace(' ','%20')
	final_url=url+ "locality=" + locality + "&region=CA" + "&postal_code=95135"+ "&category=restaurant" + "&api_key=" + api_key
	json_obj=urllib2.urlopen(final_url)
	data=json.load(json_obj) 
	x=[]
	s=""
	#instantiating client object 
	client = TwilioRestClient(account='AC382aa7d2a753e94aea2f916a7746ca2f',token='02bb57b080d6b66a99a8033a8b7c10f3')
	#iterating through 'objects' dictionary in JSON data
	for item in data['objects']:
		#formatting into a string and adding phone number
		s+=item['name']+ " " +item['phone'] + "\n"
	#using twilio API to send text message 
	client.messages.create(
		from_="+12155844319",
		to="(646) 734-9750", 
		body=s
	)

def search(query):

locuserch('San Jose')
	

	