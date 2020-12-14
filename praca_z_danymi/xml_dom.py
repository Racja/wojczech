from xml.dom import minidom

DOMTree = minidom.parse("cars_1")
collection = DOMTree.documentElement

cars = collection.getElementsByTagName("car")

for car in cars:
   brand = car.getElementsByTagName("name")[0]
   print("Marka i model samochodu:  ", brand.childNodes[0].data)
   engine = car.getElementsByTagName("engine")[0]
   print("Silnik: ", engine.childNodes[0].data)
   navi = car.getElementsByTagName("navi")[0]
   print("Czy samochód może mieć nawigację w opcji: ", navi.childNodes[0].data, "\n")