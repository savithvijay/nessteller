import requests
import json
customerId = 'your customerId here'
apiKey = 'your apiKey here'

url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)

# Get the balance for customerID
def getBalance(url) 
    try:  response = requests.get(url)
        
        # Consider any status other than 2xx an error  if not response.status_code // 100 == 2:   return "Error: Unexpected response {}".format(response)  results = response.json()   print(results)  return results   except requests.exception.Requestexception as e: # A serious problem happened, like an SSLError or InvalidURL        return "Error: {}".format(e)
