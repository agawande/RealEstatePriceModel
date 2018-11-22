# Testing with zillow
# Plan is to get "Zestimate" for the property and match against our prediction

import zillow
import pprint

with open("../zillow/zillow-id", 'r') as f:
    key = f.readline().replace("\n", "")

api = zillow.ValuationApi()

address = "3400 Pacific Ave., Marina Del Rey, CA"
postal_code = "90292"
#address = "Crittenden County, AR"
#postal_code = "72364"

data = api.GetSearchResults(key, address, postal_code)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(data.get_dict())

#data = api.GetDeepSearchResults(key, address, postal_code)
#pp.pprint(data.get_dict())
