import urllib.request
import json

def ManipulaJSON():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson")
    if (webURL.getcode() == 200):
        dados = webURL.read()
        oJSON = json.loads(dados)

        contagem = oJSON["metadata"]["count"]
        print ("contagem: " + str(contagem))

        for local in oJSON["features"]:
            if (local["properties"]["place"]) == "180 km WSW of Adak, Alaska":
             print("***************************Encontrado registro especial********************************")
            else:
                print(local["properties"]["place"])

ManipulaJSON()