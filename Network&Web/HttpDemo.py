from urllib import request, parse

# Base URL being accessed
url = 'https://app-portal-pdc1.envisioniot.com/starbucks-check-bff/v1.0/user/loginRequest'

# Dictionary of query parameters (if any)
parms = {
   'code' : 1,
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a GET request and read the response
u = request.urlopen(url+'?' + querystring)
resp = u.read()

# Make a POST request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()

# Extra headers
headers = {
    'User-agent' : 'none/ofyourbusiness',
    'Spam' : 'Eggs'
}
 
req = request.Request(url, querystring.encode('ascii'), headers=headers)

# Make a request and read the response
u = request.urlopen(req)
resp = u.read()