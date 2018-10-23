<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<xsl:template match="/">


    <xsl:variable name="path" select="php:function('scandir','/challenge/web-serveur/ch50/')"/>
<xsl:value-of select="php:function('print_r',$path)" />
    
    </xsl:template>
</xsl:stylesheet>
