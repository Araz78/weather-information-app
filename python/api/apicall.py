import urllib.request
import json

def getWeatherDetails(country, region, city):
    country_res = ""
    region_res = ""
    city_res = ""

    # remove whitespace
    if(country != "null"):
        country_res = country.replace(" ", "%20") + ",%20"

    else: 
        country_res = ""

    if(region != "null"):
        region_res = region.replace(" ", "%20") + ",%20"

    else:
        region_res = ""

    if(city != "null"):
        city_res = city.replace(" ", "%20") + ",%20"

    else:
        city_res = ""

    location = country_res + region_res + city_res

    url = "http://api.weatherapi.com/v1/current.json?key=ccaffbcfbe954f1881b101943201611&q=" + location
    request  = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    result   = json.loads(response.read())
    return result
