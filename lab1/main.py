import os
from scrapy import cmdline
from lxml import etree


def xsport_parse():
    try:
        os.remove("results/xsport.xml")
    except OSError:
        print("results/xsport.xml not found")

    cmdline.execute("scrapy crawl xsport_news".split())


def xsport_analysis():
    # root = None
    # with open("results/xsport.xml") as file:
    #     root = etree.parse(file)

    root = etree.parse("results/xsport.xml")

    hyperlinks = root.xpath('//page/@url')
    print("Total hyperlinks: {0}".format(len(hyperlinks)))
    for hyperlink in hyperlinks:
        print(hyperlink)


def do_xsport():
    xsport_parse()
    xsport_analysis()


def meblium_parse():
    try:
        os.remove("results/meblium.xml")
    except OSError:
        print("results/meblium.xml not found")

    cmdline.execute("scrapy crawl meblium -o results/meblium.xml -t xml".split())


def meblium_to_xhtml():
    dom = etree.parse("results/meblium.xml")
    xslt = etree.parse("xslscripts/meblium.xslt")
    transform = etree.XSLT(xslt)
    result = transform(dom)

    with open("results/meblium.html", 'wb') as f:
        f.write(etree.tostring(result, pretty_print=True, encoding='UTF-8'))


def do_meblium():
    # meblium_parse()
    meblium_to_xhtml()


# do_xsport()
# do_meblium()

# xsport_parse()
xsport_analysis()

