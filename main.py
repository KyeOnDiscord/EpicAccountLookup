import auth
import re
import lookup

bearerToken = auth.GetBearerToken()
input = input("Enter Epic Account ID: ")
if re.search(r'^[0-9a-f]{32}$', input):
     acc = lookup.LookupAccountByID(bearerToken, input)
else:
    print("Invalid Epic Account ID, it should look like this: 0123456789abcdef0123456789abcdef")

# Not yet implemented, requires a bearer token with 'account:public:account READ' permission, https://github.com/LeleDerGrasshalmi/FortniteEndpointsDocumentation/blob/main/EpicGames/AccountService/Account/Lookup/Displayname.md  
# lookup.LookupAccountByName(bearerToken, input)