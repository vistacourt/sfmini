

import beatbox

service = beatbox.PythonClient()  # instantiate the object
service.login('tkelly@cbank.com', 'Tmus17!!Oeyx9g6Hg8k4I7C5Ho8yEPupw')  # login using your sf credentials



x=0

query_result = service.query("SELECT Name, OwnerID FROM Account")
#query_result = service.query("SELECT Name,Id FROM Account")

records = query_result['records']  # dictionary of results

total_records = query_result['size']  # full size of results
query_locator = query_result['queryLocator']  # get the mystical queryLocator

# loop through, pulling the next 500 and appending it to your records dict
while query_result['done'] is False and len(records) < total_records:
  query_result = service.queryMore(query_locator)
  query_locator = query_result['queryLocator']  # get the updated queryLocator
  records = records + query_result['records']  # append to records dictionary






for i in records:
    x+=1
    print i
print x
