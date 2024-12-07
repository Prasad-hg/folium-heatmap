
import folium
from folium.plugins import HeatMap

mapObj = folium.Map(location=[23.294059708387206, 78.26660156250001], zoom_start=6)

bordersStyle = {
    'color': 'green',
    'weight': 1, 
    'fillOpacity' : 0.1,
}

folium.GeoJson('states_india.geojson', name='India',style_function=lambda x : bordersStyle).add_to(mapObj)
folium.GeoJson('srilanka.geojson', name='Srilanka',style_function=lambda x : bordersStyle).add_to(mapObj)



shapesLayer = folium.FeatureGroup(name="circles").add_to(mapObj)

circlesData = [
    [28.6100,77.2300, 80000],
    [19.0761,72.8775, 80000],
    [12.9789,77.5917, 80000],
    [17.3617,78.4747, 80000],
    [10.1632, 76.6413, 80000],
  
]
for cData in circlesData:
    folium.Circle(location=[cData[0], cData[1]],
                  radius=cData[2],
                  weight=5,
                  color='green',
                  fill_color='red',
                  tooltip="high risk zone",
                  popup=folium.Popup("""<h2>This city is more prone to <b>vector born diseases</b></h2>
                   
                    <img src="https://www.w3schools.com/html/pic_trulli.jpg" alt="Trulli" style="max-width:100%;max-height:100%">""", max_width=500)
                  ).add_to(shapesLayer)

folium.LayerControl().add_to(mapObj)

mapObj.save('output.html')



