import requests

parameters = { "apiKey" : "1170aaed0ee6472096809e429373fdab",
	"version" : "4.01", 
	"streetAddress" : "622 Brister St", 
	"city" : "Memphis", 
	"state" : "TN", 
	"zip" : "38111"}


response = requests.get("https://geoservices.tamu.edu/Services/Geocode/WebService/GeocoderWebServiceHttpNonParsed_V04_01.aspx?", params=parameters)


if response.status_code == 200:
	if 'Success' in response.text:
		lat = response.text.strip().split(',')[3]
		lng = response.text.strip().split(',')[4]
		print('Lattitude: ', lat)
		print('Longitute: ', lng)
	else:
		print('GeoCoding Failed')
		print(response.text)
else:
	print('Invalid Request')
	print(response.text)



