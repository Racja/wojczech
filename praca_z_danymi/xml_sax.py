import xml.sax


class Carshandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ""
        self.brand = ""
        self.engine = ""
        self.navi = ""

    def startElement(self, tag, attributes):
        self.currentdata = tag

    def characters(self, content):
        if self.currentdata == "name":
            self.brand = content
            print("Marka i model samochodu: ", self.brand)
        elif self.currentdata == "engine":
            self.engine = content
            print("Pojemność silnika: ", self.engine)
        elif self.currentdata == "navi":
            self.navi = content
            print("Czy może mieć nawigację w opcji: ", self.navi, "\n")

    def endElement(self, name):
        self.currentdata = ""


parser = xml.sax.make_parser()
handler = Carshandler()
parser.setContentHandler(handler)
parser.parse("cars_1")
