<xsl:test select="beers/beer">
    XSLT Version: <xsl:value-of select="system-property('xsl:version')" /><br/>
    XSLT Vendor: <xsl:value-of select="system-property('xsl:vendor')" /><br/>
    XSLT Verdor URL: <xsl:value-of select="system-property('xsl:vendor-url')" /><br/>
</xsl:test>
</body>
</html>
