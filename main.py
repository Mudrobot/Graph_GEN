import os.path
import overpy
import json
from matplotlib import pyplot as plt

def queryGen(info,delta):
    lat,lon = None,None
    if info['lon_delta'] == 0 or info['lat_delta'] == 0:
        lat = [info['lat'] - delta, info['lat'] + delta]
        lon = [info['lon'] - delta, info['lon'] + delta]
    else:
        lat = [info['lat'], info['lat']+info['lat_delta']]
        lon = [info['lon'], info['lon']+info['lon_delta']]
    query_str = "[out:json];way[\"highway\"](%.3f,%.3f,%.3f,%.3f);out body;>;out skel qt;" % (lat[0], lon[0], lat[1], lon[1])
    print(query_str)
    return query_str,lon,lat

def init():
    with open("query.json", encoding="utf-8") as f:
        city = json.load(f)
    api = overpy.Overpass()
    
    return city[0]["delta"],city[1:],api

def savePic(result,lon,lat,path='img/'):
    plt.figure(dpi=256, figsize=(32, 32))
    # plt.rcParams['image.interpolation'] = 'nearest'
    plt.axis('off')
    plt.xlim(lon)
    plt.ylim(lat)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    for way in result.ways:
        nodes = way.get_nodes()
        x = []; y = []
        for node in nodes:
            x.append(node.lon)
            y.append(node.lat)
        plt.plot(x, y, color='black')
    plt.savefig("%s%s.png" % (path,name))   
    # plt.savefig("svgs/%s.svg" % name, format='svg')  
    plt.close()

if __name__ == '__main__':
    delta,city,api = init()
    print(delta)
    
    for info in city:
        name = info['name']
        print(info)
        if os.path.exists("svgs/%s.svg" % name):
            print(name)
            continue
        query_str,lon,lat = queryGen(info,delta)
                    
        try:
            result = api.query(query_str)  # "node(min_lat,min_lon,max_lat,max_lon);out;"
        except:
            print("-------------------------SOMETING WRONG!!!!-------------------------")
            continue
        print(name, len(result.ways), len(result.nodes))
        
        savePic(result,lon,lat)
            