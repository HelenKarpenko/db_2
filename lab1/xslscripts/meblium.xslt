<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="xml" doctype-system="http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"
                doctype-public="-//W3C//DTD XHTML 1.1//EN" indent="yes"/>
    <xsl:template match="/">
        <html>
            <head>
                <meta charset="utf-8"/>
                <title>The Sofas Table</title>
            </head>
            <body>
                <h1>The Sofas Table</h1>
                <table>
                    <tr>
                        <td>Title</td>
                        <td>Image</td>
                        <td>Price</td>
                    </tr>
                    <xsl:apply-templates/>
                </table>
            </body>
        </html>
    </xsl:template>
    <xsl:template match="item">
        <tr>
            <td>
                <xsl:value-of select="title"/>
            </td>
            <td>
                <xsl:element name="img">
                    <xsl:attribute name="src">
                        <xsl:value-of select="img"/>
                    </xsl:attribute>
                </xsl:element>
            </td>
            <td>
                <xsl:value-of select="price"/>
            </td>
        </tr>
    </xsl:template>
</xsl:stylesheet>