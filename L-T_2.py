import folium

map=folium.Map(location=[28.3949,84.1240],zoom_start=8)
map.add_child(folium.Marker(location=[27.9881,86.9250],popup="Mount Everest",icon=folium.Icon(color="green")))
map.save("map.html")