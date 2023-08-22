import streamlit as st
import pandas as pd 
from streamlit_option_menu import option_menu
import json
import boto3
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
from PIL import Image
from st_aggrid import AgGrid
import time
from streamlit_autorefresh import st_autorefresh
import os
import random

st.set_page_config(page_title="111 Birthday", 
                   page_icon="logo.jpg",
                   layout= "wide")

aws_access_key_id = st.secrets["aws_key"]
aws_secret_access_key = st.secrets["aws_secret_key"]

def GetJSON(key_ , aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key):
    client = boto3.client('s3',aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key)
    f = client.get_object(Bucket = 'summer-song', Key= key_)
    text = f["Body"].read().decode()
    return json.loads(text)


def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)
def color_func(list_colors):
    return rgb_to_hex(list_colors[0], list_colors[1], list_colors[2])

def GetAllPoints(dict_test):
    all_points = []
    all_races = []
    for key_ in dict_test.keys():
        points = 0
        for key_game in dict_test[key_].keys():
            points = points + dict_test[key_][key_game]
        
        all_points.append(points)
        all_races.append(key_)
    return {"race": all_races, "points": all_points}





puntos_juegos = GetJSON("dict_points_part1.json")
with open("colores_lotr.json") as file:
    colors_lotr = json.load(file)

selected3 = option_menu("",["Tabla", "Hazañas"], 
        icons=['file-bar-graph-fill', 'lightning-fill'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": color_func(colors_lotr["marron"])},
            "icon": {"color": "#ffffff", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": color_func(colors_lotr["oro"])},
            "nav-link-selected": {"background-color":color_func(colors_lotr["marron_oscuro"])}
        }
    )

if selected3 == "Tabla":
    all_points = GetAllPoints(puntos_juegos)
    data_points = pd.DataFrame(all_points).sort_values("points", ascending= False).reset_index()
    fig = go.Figure()
    i = 0
    for index, row in data_points.iterrows():
        if i == 0:
            fig.add_shape(
                type='rect', line=dict(dash='dash', color = "white"),
                fillcolor = "#FFD700",
                layer = "below",
                x0=1, x1=2, y0=0, y1=row["points"]
            )

            if (row["points"] < 12) and (row["points"] > 0):
                y_max = row["points"] + 4

                fig.add_annotation(x= 1.5, y=y_max,
                    text="1." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
                
                fig.add_annotation(x=1.5 , y=y_max - 2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
            elif row["points"] >= 12:
                max_points = row["points"]
                y_max = row["points"]*2/3
                fig.add_annotation(x= 1.5, y=y_max,
                    text="1." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))
            
                fig.add_annotation(x=1.5 , y= y_max/2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))

            

        elif i == 1:
            fig.add_shape(
                type='rect', line=dict(dash='dash', color = "white"),
                fillcolor = "#c0c0c0",
                layer = "below",
                x0=0, x1=1, y0=0, y1=row["points"]
            )

            if (row["points"] < 12) and (row["points"] > 0):
                y_max = row["points"] + 4

                fig.add_annotation(x= 0.5, y=y_max,
                    text="2." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
                
                fig.add_annotation(x=0.5 , y=y_max - 2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
            elif row["points"] >= 12:
                max_points = row["points"]
                y_max = row["points"]*2/3
                fig.add_annotation(x= 0.5, y=y_max,
                    text="2." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))
            
                fig.add_annotation(x=0.5 , y= y_max/2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))

        elif i == 2:
            fig.add_shape(
                type='rect', line=dict(dash='dash', color = "white"),
                fillcolor = "#cd7f32",
                layer = "below",
                x0=2, x1=3, y0=0, y1=row["points"]
            )

            if (row["points"] < 12) and (row["points"] > 0):
                y_max = row["points"] + 4

                fig.add_annotation(x= 2.5, y=y_max,
                    text="3." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
                
                fig.add_annotation(x=2.5 , y=y_max - 2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
            elif row["points"] >= 12:
                max_points = row["points"]
                y_max = row["points"]*2/3
                fig.add_annotation(x= 2.5, y=y_max,
                    text="3." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))
            
                fig.add_annotation(x=2.5 , y= y_max/2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))

        elif i == 3:
            fig.add_shape(
                type='rect', line=dict(dash='dash', color = "white"),
                fillcolor = "white",
                layer = "below",
                x0=3, x1=4, y0=0, y1=row["points"]
            )

            if (row["points"] < 12) and (row["points"] > 0):
                y_max = row["points"] + 4

                fig.add_annotation(x= 3.5, y=y_max,
                    text="4." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
                
                fig.add_annotation(x=3.5 , y=y_max - 2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#ffffff"
                        ))
            elif row["points"] >= 12:
                max_points = row["points"]
                y_max = row["points"]*2/3
                fig.add_annotation(x= 3.5, y=y_max,
                    text="4." + row["race"], showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))
                fig.add_annotation(x=3.5 , y= y_max/2,
                        text="{points} pto(s)".format(points = row["points"]), showarrow=False,
                    font=dict(
                        family="Times New Roman, monospace",
                        size = 22,
                        color="#000000"
                        ))
        

        i = i +1

    fig.update_layout(
                    xaxis=dict(
                        showline=True,
                        showgrid=False,
                        showticklabels=False,
                        linecolor='#f04641',
                        linewidth=2,
                        ticks='outside',
                        tickfont=dict(
                            family='Poppins',
                            size=12,
                            color='#f04641'
                        )
                    ),
                    yaxis = dict(
                        showgrid = False,
                        linewidth = 2,
                        linecolor='#00aa9b',
                        ticks = "outside",
                        tickfont = dict(
                            family = "Poppins",
                            size = 14,
                            color = '#00aa9b'
                        ),
                        showticklabels = True
                    ),
                    showlegend=False,
                    title = "Clasificación",
                    plot_bgcolor='rgb(15,18,22)',
                    xaxis_title='',
                    yaxis_title='Puntos',
                )
    fig = fig.update_xaxes(range = [0,4])
    fig = fig.update_yaxes(range = [0,max(data_points.points)+5])

    dict_points = {}
    for race_ in puntos_juegos.keys():
        points_list = []
        for game_ in puntos_juegos[race_].keys():
            points_list.append(puntos_juegos[race_][game_])
        
        dict_points[race_] = points_list
    
    data_points = pd.DataFrame(dict_points)
    data_points = data_points.transpose()
    data_points.columns = list(puntos_juegos[race_].keys())
    with st.expander("Tablas"):
        st.dataframe(data_points, use_container_width= True)

    st.plotly_chart(fig, use_container_width=True)

else:
    list_characters = ["Merryna Hornblower", "Glinaer"]

    dict_pics = {
        "Merryna Hornblower": "maria_test.jpeg",
        "Glinaer": "jay_test.jpeg"
    }

    option = st.selectbox("Elige", options = list_characters)

    st.image(os.path.join("pics_hazañas", dict_pics[option]))

