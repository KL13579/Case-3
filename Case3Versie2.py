#!/usr/bin/env python
# coding: utf-8

# Groep 18: Irina van Dam, Pien van Dongen, Kevin Linders & Floor Wesselink

# In[125]:


import requests
import json
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from shapely.geometry import Point, Polygon
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster
import branca
import streamlit_folium as st_folium
from streamlit_folium import folium_static


# In[2]:


st.header('Toename van elektrisch vervoer')


# De code hieronder hebben wij tot commands gemaakt omdat streamlit de data anders niet in kan laden. Dat is vanwege het feit dat de hoeveelheid data uit de response teveel is om in te laden voor streamlit. 
# Hieronder is te zien hoe wij de data hebben ingeladen met de API's van het RDW en hoe wij deze data hebben geanalyseerd.

# In[3]:


#Inladen van alle auto's vanaf het jaar 2015, met de variabelen kenteken en datum_eerste_tenaamstelling_in_nederland
#response1 = requests.get('https://opendata.rdw.nl/resource/m9d7-ebf2.json?$$app_token=qXFPxMddONVr63MCrFtrxLUrN&$where=datum_eerste_tenaamstelling_in_nederland>20141231&$select=kenteken, datum_eerste_tenaamstelling_in_nederland&$limit=7000000')        
#data1 = response1.json()
#df1 = pd.DataFrame.from_dict(data1)     


# In[4]:


#Inladen van kenteken, brandstof omschrijving en klasse hybride elektrisch voertuig
#response2 = requests.get('https://opendata.rdw.nl/resource/8ys7-d773.json?$$app_token=qXFPxMddONVr63MCrFtrxLUrN&$select=kenteken, brandstof_omschrijving, klasse_hybride_elektrisch_voertuig&$limit=15000000')
#data2 = response2.json()
#df2 = pd.DataFrame.from_dict(data2)


# In[5]:


#Brandstof koppelen aan de juiste auto's
#auto_brandstof = df1.merge(df2, on = 'kenteken', how = 'left')


# In[6]:


#Data bekijken
#auto_brandstof.head()


# In[7]:


#Data verder inspecteren
#auto_brandstof.info()


# In[8]:


#Datum naar datetime omzetten
#auto_brandstof['datum'] = pd.to_datetime(auto_brandstof['datum_eerste_tenaamstelling_in_nederland'], format = '%Y%m%d')
#auto_brandstof['jaar'] = auto_brandstof['datum'].dt.year
#auto_brandstof['maand'] = auto_brandstof['datum'].dt.month
#auto_brandstof['dag'] = 1
#auto_brandstof['datum'] = pd.to_datetime(dict(year = auto_brandstof.jaar, month = auto_brandstof.maand, day = auto_brandstof.dag))
#auto_brandstof.head()


# In[9]:


#df = auto_brandstof[['brandstof_omschrijving', 'datum']]


# In[10]:


#Per brandstofsoort een dataframe aanmaken.
#benzine = df[df['brandstof_omschrijving'] == 'Benzine']
#diesel = df[df['brandstof_omschrijving'] == 'Diesel']
#elektriciteit = df[df['brandstof_omschrijving'] == 'Elektriciteit']
#lpg = df[df['brandstof_omschrijving'] == 'LPG']
#cng = df[df['brandstof_omschrijving'] == 'CNG']
#alcohol = df[df['brandstof_omschrijving'] == 'Alcohol']
#lng = df[df['brandstof_omschrijving'] == 'LNG']
#waterstof = df[df['brandstof_omschrijving'] == 'Waterstof']


# In[11]:


#Deze functie telt het aantal auto's dat binnen een maand aangeschaft wordt.
#def counting(colom, list_name):
    #list_name = {}
    #for entry in colom:
        #if entry in list_name.keys():
            #list_name[entry] = list_name[entry] + 1
        #else:
            #list_name[entry] = 1
    #return list_name


# In[12]:


#Een lege lijst per brandstofsoort aanmaken voor het tellen
#counts1 = {}
#counts2 = {}
#counts3 = {}
#counts4 = {}
#counts5 = {}
#counts6 = {}
#counts7 = {}
#counts8 = {}


# In[13]:


#Hier wordt per brandstofsoort het aantal auto's per maand geteld en opgeslagen.
#counts1 = counting(benzine['datum'], counts1)
#counts2 = counting(diesel['datum'], counts2)
#counts3 = counting(elektriciteit['datum'], counts3)
#counts4 = counting(lpg['datum'], counts4)
#counts5 = counting(cng['datum'], counts5)
#counts6 = counting(alcohol['datum'], counts6)
#counts7 = counting(lng['datum'], counts7)
#counts8 = counting(waterstof['datum'], counts8)


# In[14]:


#Hier worden de dictionarys naar dataframes omgezet
#benzine1 = pd.DataFrame(counts1.items(), columns = ['Datum', 'Aantal'])
#diesel1 = pd.DataFrame(counts2.items(), columns = ['Datum', 'Aantal'])
#elektriciteit1 = pd.DataFrame(counts3.items(), columns = ['Datum', 'Aantal'])
#lpg1 = pd.DataFrame(counts4.items(), columns = ['Datum', 'Aantal'])
#cng1 = pd.DataFrame(counts5.items(), columns = ['Datum', 'Aantal'])
#alcohol1 = pd.DataFrame(counts6.items(), columns = ['Datum', 'Aantal'])
#lng1 = pd.DataFrame(counts7.items(), columns = ['Datum', 'Aantal'])
#waterstof1 = pd.DataFrame(counts8.items(), columns = ['Datum', 'Aantal'])


# In[15]:


#Hier wordt per dataframe een kolom toegevoegd met de cummulatieve som toegevoegd
#benzine1['Cumsum'] = benzine1['Aantal'].cumsum()
#diesel1['Cumsum'] = diesel1['Aantal'].cumsum()
#elektriciteit1['Cumsum'] = elektriciteit1['Aantal'].cumsum()
#lpg1['Cumsum'] = lpg1['Aantal'].cumsum()
#cng1['Cumsum'] = cng1['Aantal'].cumsum()
#alcohol1['Cumsum'] = alcohol1['Aantal'].cumsum()
#lng1['Cumsum'] = lng1['Aantal'].cumsum()
#waterstof1['Cumsum'] = waterstof1['Aantal'].cumsum()


# In[16]:


#De brandstofsoort wordt per dataframe toegevoegd.
#benzine1['Brandstoftype'] = 'Benzine'
#diesel1['Brandstoftype'] = 'Diesel'
#elektriciteit1['Brandstoftype'] = 'Elektriciteit'
#lpg1['Brandstoftype'] = 'LPG'
#cng1['Brandstoftype'] = 'CNG'
#alcohol1['Brandstoftype'] = 'Alcohol'
#lng1['Brandstoftype'] = 'LNG'
#waterstof1['Brandstoftype'] = 'Waterstof'


# In[120]:


#benzine1.to_csv('benzine2.csv')
#diesel1.to_csv('diesel2.csv')
#elektriciteit1.to_csv('elektriciteit2.csv')
#lpg1.to_csv('lpg2.csv')
#cng1.to_csv('cng2.csv')
#alcohol1.to_csv('alcohol2.csv')
#lng1.to_csv('lng2.csv')
#waterstof1.to_csv('waterstof2.csv')


# In[121]:


benzine2 = pd.read_csv('benzine2.csv')
diesel2 = pd.read_csv('diesel2.csv')
elektriciteit2 = pd.read_csv('elektriciteit2.csv')
lpg2 = pd.read_csv('lpg2.csv')
cng2 = pd.read_csv('cng2.csv')
alcohol2 = pd.read_csv('alcohol2.csv')
lng2 = pd.read_csv('lng2.csv')
waterstof2 = pd.read_csv('waterstof2.csv')


# In[122]:


#Alle dataframes in een lijst.
dataframes = [benzine2, diesel2, elektriciteit2, lpg2, cng2, alcohol2, lng2, waterstof2]

#Alle dataframes weer aan elkaar toevoegen en brandstoftype omzetten naar een string.
df2 = pd.concat(dataframes)
df2['Brandstoftype'] = df2['Brandstoftype'].astype('string')


# In[131]:


#Een checkbox om de schaal in de lijnplot aan te passen
checkbox = st.checkbox(label = 'Logaritmische schaal')

#Code voor de lijnplot
if checkbox:
    px.line(x = df2['Datum'], y = df2['Cumsum'], color = df2['Brandstoftype'], log_y = True)
else:
    px.line(x = df2['Datum'], y = df2['Cumsum'], color = df2['Brandstoftype'])


#  
#  

# Hieronder worden de stappen ondernomen voor het maken van een histogram over de laadpaal data.

# In[19]:


#Inladen van de data
df3 = pd.read_csv('laadpaaldata.csv')

#Bekijken van de data
#df3.info()


# In[20]:


#De onderstaande code geeft een error omdat er verschillende rijen die aangeven op 29 februari 2018 te laden, 
#echter bestaat die datum niet.

#df3['Started'] = pd.to_datetime(df3['Started'])
#df3['Ended'] = pd.to_datetime(df3['Ended'])

#Zoeken naar verschillende rijen die aangeven op 29 februari 2018 te laden, echter bestaat die datum niet.
#De onderstaande regels zijn de regels met 29 februari 2018
#df3.loc[1731]
#df3.loc[1732]


# In[21]:


#Droppen van rijen met ongeldige waarden.
df3 = df3.drop([1731,1732])


# In[22]:


#Omzetten naar datetime.
df3['Started'] = pd.to_datetime(df3['Started'])
df3['Ended'] = pd.to_datetime(df3['Ended'])


# In[23]:


#Filteren zodat de eindtijd na de starttijd ligt.
df3 = df3[df3['Started'] < df3['Ended']]
#df3


# In[24]:


#De Charge time moet altijd kleiner of gelijk zijn aan de Connected time
#Hier worden de rijen gedropt waarbij dit niet het geval is
df3 = df3[df3['ChargeTime'] <= df3['ConnectedTime']]
#df3


# In[25]:


#Onderzoeken van de kolom Charge Time.
#df3['ChargeTime'].describe()


# In[26]:


#Negatieve Charge Time droppen.
df3 = df3[df3['ChargeTime'] > 0]

#Waarde boven 20 droppen
df3 = df3[df3['ChargeTime'] <= 15]


# In[27]:


#Kolom Connected Time inspecteren
#df3['ConnectedTime'].describe()


# In[28]:


#Hier wordt er gefilterd zodat de connected time onder de 30 uur zit.
df3 = df3[df3['ConnectedTime'] <= 30]


# In[29]:


#Hier worden strings aangemaakt voor de histogram
string1 = 'Mean: ' + str(round(df3['ConnectedTime'].mean(), 4))
string2 = 'Median: ' + str(round(df3['ConnectedTime'].median(), 4))
string3 = 'Mean: ' + str(round(df3['ChargeTime'].mean(), 4))
string4 = 'Median: ' + str(round(df3['ChargeTime'].median(), 4))


# In[133]:


#Hier wordt een histogram gemaakt voor zowel de Charge time en Connected time. 
fig, ax = plt.subplots()

sns.histplot(data = df3, x = 'ConnectedTime', bins = 39, label = 'Connected time', color = 'Blue')
sns.histplot(data = df3, x = 'ChargeTime', bins = 20, label = 'Charge time', color = 'Red')

ax.set_title('Histogram met de verdeling van tijd voor opladen van voertuigen')
ax.set_xlabel('Laadtijd in uren')
ax.set_ylabel('Aantal voertuigen')

plt.annotate(string1, xy = (10, 2000), color = 'Blue')
plt.annotate(string2, xy = (10, 1850), color = 'Blue')
plt.annotate(string3, xy = (10, 1600), color = 'Red')
plt.annotate(string4, xy = (10, 1450), color = 'Red')

plt.legend()

st.pyplot(fig)


# Uit de plot valt te halen, dat veel auto's langer connected zijn dan dat er daadwerkelijk geladen wordt.

# In[ ]:





# In[31]:


#Alles moet worden ingeladen
url = "https://api.openchargemap.io/v3/poi"

querystring = {"countrycode":"NL","latitude":"52.848781","longitude":"5.838421","distanceunit":"km","key":"444", "maxresults": 10000}

headers = {"Content-Type": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

df = pd.DataFrame.from_dict(data)


# In[57]:


#Informatie uit de ingeladen data die we nodig hebben voor de markers.
df_map = df[['AddressInfo', 'StatusType', 'Connections', 'NumberOfPoints']]


# In[58]:


df_map.info()


# In[59]:


#Welke waarde missen we bij Number of points.
#df_map[df_map['NumberOfPoints'].isna()]


# In[68]:


#Nagaan welke rijen alleen een lege lijst hebben bij de variabele connections.
connections_lengte = []

for i in list(df_map.index):
    connections_lengte.append(len(df_map["Connections"][i]))

lengte = pd.DataFrame(connections_lengte, columns = ['lengte'])

drop_list = list(lengte[lengte['lengte']==0].index)


# Rij met index 5561 zit beide, dus we droppen alle bovenstaande rijen.

# In[72]:


#De rijen droppen waarvoor er geen connection data beschikbaar is en waar geen numberofpoints data beschikbaar voor is.
df_map = df_map.drop(drop_list)


# In[73]:


#StatusType 
title_status = []

for i in df_map['StatusType']:
    title_status.append(i['Title'])
    
len(title_status)


# In[74]:


#ID
ID = []

for i in df_map["AddressInfo"]:
    ID.append(i['ID'])


# In[75]:


#Adres info
adres_info = []

for i in df_map["AddressInfo"]:
    adres_info.append(i['Title'])
    
#len(adres_info)


# In[76]:


#ConnectionType
connectiontype_title = []

for i in df_map['Connections']:
    connectiontype_title.append(i[0]["ConnectionType"]["Title"])
#len(connectiontype_title)


# In[77]:


#Power KW
power_kw = []

for i in df_map['Connections']:
    power_kw.append(i[0]["PowerKW"])
#len(power_kw)


# In[78]:


#Current type
current_type = []

for i in df_map['Connections']:
    if i[0]["CurrentType"] == None:
        current_type.append('Unknown')
    else:
        current_type.append(i[0]["CurrentType"]["Title"])

#len(current_type)


# In[79]:


#De hierboven gegenereerde lijsten samenvoegen tot een dataframe. 
marker_info = {'ID': ID, 'SatusType': title_status, "AdresInfo": adres_info, "ConnectionType": connectiontype_title, "Power_kw": power_kw, "Current_type": current_type}
df_marker_info = pd.DataFrame(data = marker_info, index = list(df_map.index))


# In[80]:


#df_marker_info


# In[81]:


#Provincie grenzen inladen
provincies = gpd.read_file('provincies4.geojson')


# In[82]:


#Adres info inladen om de markers te plotten op de juiste plek.
addressinfo = df['AddressInfo']


# In[83]:


#Lijst maken van de info die we nodig hebben om te plotten.
lijst = []
for adres in addressinfo:
    info = [adres["ID"], adres["Longitude"], adres['Latitude']]
    lijst.append(info)


# In[84]:


#Omzetten naar dataframe
lat_long = pd.DataFrame(lijst, columns = ['ID', 'Lng', 'Lat'] )


# In[85]:


#Mergen van data, zodat er 1 dataframe is met alle benodige info
lat_long2 = lat_long.merge(df_marker_info, on = 'ID')


# In[86]:


#Bepalen in welke provincie een laadpunt zit.
provincie = []
for index, row in lat_long2.iterrows():
    plaats = Point(row['Lng'], row['Lat'])
    if plaats.within(provincies['geometry'][0]) == True:
                     provincie.append("Drenthe")
    elif plaats.within(provincies['geometry'][1]) == True:
                     provincie.append("Flevoland")  
    elif plaats.within(provincies['geometry'][2]) == True:
                     provincie.append("Friesland (Fryslân)") 
    elif plaats.within(provincies['geometry'][3]) == True:
                     provincie.append("Gelderland") 
    elif plaats.within(provincies['geometry'][4]) == True:
                     provincie.append("Groningen") 
    elif plaats.within(provincies['geometry'][5]) == True:
                     provincie.append("Limburg") 
    elif plaats.within(provincies['geometry'][6]) == True:
                     provincie.append("Noord-Brabant")
    elif plaats.within(provincies['geometry'][7]) == True:
                     provincie.append("Noord-Holland") 
    elif plaats.within(provincies['geometry'][8]) == True:
                     provincie.append("Overijssel") 
    elif plaats.within(provincies['geometry'][9]) == True:
                     provincie.append("Utrecht") 
    elif plaats.within(provincies['geometry'][10]) == True:
                     provincie.append("Zeeland") 
    elif plaats.within(provincies['geometry'][11]) == True:
                     provincie.append("Zuid-Holland") 


# In[87]:


#Provincies toevoegen aan het dataframe
lat_long2["Provincie"] = provincie


# In[88]:


#De totale dataframe groeperen per provincie

Friesland = lat_long2[lat_long2["Provincie"]=='Friesland (Fryslân)']
Groningen = lat_long2[lat_long2["Provincie"]=='Groningen']
Drenthe = lat_long2[lat_long2["Provincie"]=='Drenthe']
Gelderland = lat_long2[lat_long2["Provincie"]=='Gelderland']
Flevoland = lat_long2[lat_long2["Provincie"]=='Flevoland']
Noord_Holland = lat_long2[lat_long2["Provincie"]=='Noord-Holland']
Zuid_Holland = lat_long2[lat_long2["Provincie"]=='Zuid-Holland']
Utrecht = lat_long2[lat_long2["Provincie"]=='Utrecht']
Zeeland = lat_long2[lat_long2["Provincie"]=='Zeeland']
Limburg = lat_long2[lat_long2["Provincie"]=='Limburg']
Noord_Brabant = lat_long2[lat_long2["Provincie"]=='Noord-Brabant']
Overijssel = lat_long2[lat_long2["Provincie"]=='Overijssel']


# In[89]:


#Het aantal laadpunten per provincie bepalen
per_provincie = lat_long2.groupby(by = 'Provincie' ).count()[['ID']]
per_provincie["Aantal laadpunten"] = per_provincie['ID']
per_provincie = per_provincie[["Aantal laadpunten"]].reset_index()


# In[90]:


#Geojson file inladen met informatie over de provincies.
geo = r'provincies4.geojson'
with open(geo) as geo_file:
    geo_json = json.load(geo_file)


# In[91]:


#Het middelstepunt van de provincies bepalen. Vervolgens een dataframe creeren met de provincie, het middelstepunt en het aantal laadpunten.
provincies['midden'] = provincies['geometry'].centroid
marker_midden = provincies[['name', 'midden']]
marker_midden["Aantal laadpunten"] = per_provincie['Aantal laadpunten']


# In[92]:


#Dit is de code die gebruikt is om de legenda aan te maken
html = """<!DOCTYPE html>
<html>
<head>
<style type='text/css'>
  .my-legend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .my-legend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .my-legend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .my-legend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .my-legend .legend-source {
    font-size: 70%;
    color: #999;
    clear: both;
    }
  .my-legend a {
    color: #777;
    }
</style>

</head>
<body>

<div class='my-legend'>
<div class='legend-title'>Provincies</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:green;'></span>Groningen</li>
    <li><span style='background:pink;'></span>Drenthe </li>
    <li><span style='background:blue;'></span>Friesland </li>
    <li><span style='background:lightblue;'></span>Overijssel </li>
    <li><span style='background:darkred;'></span>Flevoland </li>
    <li><span style='background:red;'></span>Noord-Holland </li>
    <li><span style='background:orange;'></span>Zuid-Holland </li>
    <li><span style='background:cadetblue;'></span>Zeeland </li>
    <li><span style='background:darkblue;'></span>Noord-Brabant </li>
    <li><span style='background:#FF7F7F;'></span>Limburg </li>
    <li><span style='background:gray;'></span>Utrecht </li>
    <li><span style='background:purple;'></span>Gelderland </li>
  </ul>
</div>
<div class='legend-source'>Source: <a href="#link to source">Name of source</a></div>
</div>

</body>
</html>"""


# In[93]:


#Deze code is gebruikt om marker info in popup 'mooi' te displayen
def popup_html(index):
    
    adres_info = lat_long2.loc[index]['AdresInfo']
    status = lat_long2.loc[index]['SatusType']
    connection = lat_long2.loc[index]['ConnectionType']
    power = lat_long2.loc[index]['Power_kw']
    html2 = """<!DOCTYPE html>

<html>

<body>

<h4>Laadpunt: {}</h4>""".format(adres_info) + """

<table style="width:100%">
  <tr>
    <th>Status</th>
    <th>Connection type</th>
    <th>Power</th>
  </tr>
  <tr>
    <td>{}</td>""".format(status) + """
    <td>{}</td>""".format(connection) + """
    <td>{} Kw</td>""".format(power) + """
  </tr>
</table>



</body>
</html>"""
    return html2


# In[94]:


#Het maken van een map
m = folium.Map(location=[52.090736, 5.121420], zoom_start=7, min_zoom = 7, tiles = 'CartoDB Positron', width = 500, height = 700)

#Eerste map: Verdeling Nederland 
folium.Choropleth(
    geo_data=geo_json,
    name="choropleth",
    data=per_provincie,
    columns=["Provincie", "Aantal laadpunten"],
    key_on="feature.properties.name",
    fill_color="Greens",
    fill_opacity=0.8,
    line_opacity=0.5,
    legend_name="Aantal laadpunten"
).add_to(m)

##Markers maken voor elke provincie!

#Markers Friesland


marker_cluster_friesland = MarkerCluster(name = "Friesland", show = False).add_to(m)
for index, row in Friesland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="blue", icon='flash')).add_to(marker_cluster_friesland)

punt_friesland = marker_midden[marker_midden['name']=='Friesland (Fryslân)']['midden']
laadpunten_friesland = int(marker_midden[marker_midden['name']=='Friesland (Fryslân)']['Aantal laadpunten'])

folium.Marker(location=[punt_friesland.y, punt_friesland.x],
                    popup=f"In Friesland zijn er {laadpunten_friesland} laadpunten",
                    icon=folium.Icon(color="blue", icon='flash')).add_to(m)

#Markers Groningen
marker_cluster_groningen = MarkerCluster(name = "Groningen", show = False).add_to(m)
for index, row in Groningen.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="green", icon='flash')).add_to(marker_cluster_groningen)

punt_groningen = marker_midden[marker_midden['name']=='Groningen']['midden']
laadpunten_groningen = int(marker_midden[marker_midden['name']=='Groningen']['Aantal laadpunten'])

folium.Marker(location=[punt_groningen.y, punt_groningen.x],
                    popup=f"In Groningen zijn er {laadpunten_groningen} laadpunten",
                    icon=folium.Icon(color="green", icon='flash')).add_to(m)


#Markers Drenthe
marker_cluster_drenthe = MarkerCluster(name = "Drenthe", show = False).add_to(m)
for index, row in Drenthe.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="pink", icon='flash')).add_to(marker_cluster_drenthe)

punt_drenthe = marker_midden[marker_midden['name']=='Drenthe']['midden']
laadpunten_drenthe = int(marker_midden[marker_midden['name']=='Drenthe']['Aantal laadpunten'])

folium.Marker(location=[punt_drenthe.y, punt_drenthe.x],
                    popup=f"In Drenthe zijn er {laadpunten_drenthe} laadpunten",
                    icon=folium.Icon(color="pink", icon='flash')).add_to(m)

#Markers Overijssel
marker_cluster_overijssel = MarkerCluster(name = "Overijssel", show = False).add_to(m)
for index, row in Overijssel.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="lightblue", icon='flash')).add_to(marker_cluster_overijssel)

punt_overijssel = marker_midden[marker_midden['name']=='Overijssel']['midden']
laadpunten_overijssel = int(marker_midden[marker_midden['name']=='Overijssel']['Aantal laadpunten'])

folium.Marker(location=[punt_overijssel.y, punt_overijssel.x],
                    popup=f"In Overijssel zijn er {laadpunten_overijssel} laadpunten",
                    icon=folium.Icon(color="lightblue", icon='flash')).add_to(m)

#Markers Gelderland
marker_cluster_gelderland = MarkerCluster(name = "Gelderland", show = False).add_to(m)
for index, row in Gelderland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="purple", icon='flash')).add_to(marker_cluster_gelderland)

punt_gelderland = marker_midden[marker_midden['name']=='Gelderland']['midden']
laadpunten_gelderland = int(marker_midden[marker_midden['name']=='Gelderland']['Aantal laadpunten'])

folium.Marker(location=[punt_gelderland.y, punt_gelderland.x],
                    popup=f"In Gelderland zijn er {laadpunten_gelderland} laadpunten",
                    icon=folium.Icon(color="purple", icon='flash')).add_to(m)


#Markers Utrecht
marker_cluster_utrecht = MarkerCluster(name = "Utrecht", show = False).add_to(m)
for index, row in Utrecht.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="gray", icon='flash')).add_to(marker_cluster_utrecht)

punt_utrecht = marker_midden[marker_midden['name']=='Utrecht']['midden']
laadpunten_utrecht = int(marker_midden[marker_midden['name']=='Utrecht']['Aantal laadpunten'])

folium.Marker(location=[punt_utrecht.y, punt_utrecht.x],
                    popup=f"In Utrecht zijn er {laadpunten_utrecht} laadpunten",
                    icon=folium.Icon(color="gray", icon='flash')).add_to(m)

#Markers Noord-Holland
marker_cluster_noord_holland = MarkerCluster(name = "Noord-Holland", show = False).add_to(m)
for index, row in Noord_Holland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="red", icon='flash')).add_to(marker_cluster_noord_holland)

punt_noord_holland = marker_midden[marker_midden['name']=='Noord-Holland']['midden']
laadpunten_noord_holland = int(marker_midden[marker_midden['name']=='Noord-Holland']['Aantal laadpunten'])

folium.Marker(location=[punt_noord_holland.y, punt_noord_holland.x],
                    popup=f"In Noord-Holland zijn er {laadpunten_noord_holland} laadpunten",
                    icon=folium.Icon(color="red", icon='flash')).add_to(m)

#Markers Zuid-holland
marker_cluster_zuid_holland = MarkerCluster(name = "Zuid-Holland", show = False).add_to(m)
for index, row in Zuid_Holland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="orange", icon='flash')).add_to(marker_cluster_zuid_holland)

punt_zuid_holland = marker_midden[marker_midden['name']=='Zuid-Holland']['midden']
laadpunten_zuid_holland = int(marker_midden[marker_midden['name']=='Zuid-Holland']['Aantal laadpunten'])

folium.Marker(location=[punt_zuid_holland.y, punt_zuid_holland.x],
                    popup=f"In Zuid-Holland zijn er {laadpunten_zuid_holland} laadpunten",
                    icon=folium.Icon(color="orange", icon='flash')).add_to(m)


#Markers Limburg
marker_cluster_limburg = MarkerCluster(name = "Limburg", show = False).add_to(m)
for index, row in Limburg.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="lightred", icon='flash')).add_to(marker_cluster_limburg)

punt_limburg = marker_midden[marker_midden['name']=='Limburg']['midden']
laadpunten_limburg = int(marker_midden[marker_midden['name']=='Limburg']['Aantal laadpunten'])

folium.Marker(location=[punt_limburg.y, punt_limburg.x],
                    popup=f"In Limburg zijn er {laadpunten_limburg} laadpunten",
                    icon=folium.Icon(color="lightred", icon='flash')).add_to(m)

#Markers Noord-Brabant
marker_cluster_noord_brabant = MarkerCluster(name = "Noord-Brabant", show = False).add_to(m)
for index, row in Noord_Brabant.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="darkblue", icon='flash')).add_to(marker_cluster_noord_brabant)

punt_noord_brabant = marker_midden[marker_midden['name']=='Noord-Brabant']['midden']
laadpunten_noord_brabant = int(marker_midden[marker_midden['name']=='Noord-Brabant']['Aantal laadpunten'])

folium.Marker(location=[punt_noord_brabant.y, punt_noord_brabant.x],
                    popup=f"In Noord-Brabant zijn er {laadpunten_noord_brabant} laadpunten",
                    icon=folium.Icon(color="darkblue", icon='flash')).add_to(m)

#Markers Zeeland
marker_cluster_zeeland = MarkerCluster(name = "Zeeland", show = False).add_to(m)
for index, row in Zeeland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="cadetblue", icon='flash')).add_to(marker_cluster_zeeland)

punt_zeeland = marker_midden[marker_midden['name']=='Zeeland']['midden']
laadpunten_zeeland = int(marker_midden[marker_midden['name']=='Zeeland']['Aantal laadpunten'])

folium.Marker(location=[punt_zeeland.y, punt_zeeland.x],
                    popup=f"In Zeeland zijn er {laadpunten_zeeland} laadpunten",
                    icon=folium.Icon(color="cadetblue", icon='flash')).add_to(m)

#Markers Flevoland
marker_cluster_flevoland = MarkerCluster(name = "Flevoland", show = False).add_to(m)
for index, row in Flevoland.iterrows():
    html2 = popup_html(index)
    iframe = branca.element.IFrame(html=html2,width=510,height=280)
    popup = folium.Popup(folium.Html(html2, script=True), max_width=500)
    folium.Marker(location=[row['Lat'], row['Lng']],
                    popup=popup,
                    icon=folium.Icon(color="darkred", icon='flash')).add_to(marker_cluster_flevoland)

punt_flevoland = marker_midden[marker_midden['name']=='Flevoland']['midden']
laadpunten_flevoland = int(marker_midden[marker_midden['name']=='Flevoland']['Aantal laadpunten'])

folium.Marker(location=[punt_flevoland.y, punt_flevoland.x],
                    popup=f"In Flevoland zijn er {laadpunten_flevoland} laadpunten",
                    icon=folium.Icon(color="darkred", icon='flash'), tooltip = "Click here for legend").add_to(m)



#Legenda de markers per provincie
iframe = branca.element.IFrame(html=html,width=510,height=280)
popup = folium.Popup(folium.Html(html, script=True), max_width=500)
folium.Marker(location = [52.244261833472144, 3.2201231832041888], popup = popup, icon = folium.Icon(icon = 'info-sign'), draggable = True).add_to(m)

folium.LayerControl().add_to(m)

folium_static(m)


# In[ ]:




