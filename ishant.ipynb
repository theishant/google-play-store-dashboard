{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "414369a5-b657-4bfb-b9da-0a5cd5179722",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[nltk_data] Downloading package vader_lexicon to\n",
      "[nltk_data]     C:\\Users\\Dell\\AppData\\Roaming\\nltk_data...\n",
      "[nltk_data]   Package vader_lexicon is already up-to-date!\n",
      "C:\\Users\\Dell\\AppData\\Local\\Temp\\ipykernel_6012\\1124471914.py:17: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.\n",
      "The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.\n",
      "\n",
      "For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.\n",
      "\n",
      "\n",
      "  apps_df[column].fillna(apps_df[column].mode()[0],inplace=True)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.express as px\n",
    "import plotly.io as pio\n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer\n",
    "import nltk\n",
    "import webbrowser\n",
    "import os\n",
    "\n",
    "nltk.download('vader_lexicon')\n",
    "\n",
    "apps_df = pd.read_csv(r'C:\\\\Users\\\\Dell\\\\Downloads\\\\Play Store Data.csv')\n",
    "reviews_df = pd.read_csv(r'C:\\\\Users\\\\Dell\\\\Downloads\\\\User Reviews.csv')\n",
    "\n",
    "apps_df = apps_df.dropna(subset=['Rating'])\n",
    "for column in apps_df.columns :\n",
    "    apps_df[column].fillna(apps_df[column].mode()[0],inplace=True)\n",
    "apps_df.drop_duplicates(inplace=True)\n",
    "apps_df=apps_df=apps_df[apps_df['Rating']<=5]\n",
    "reviews_df.dropna(subset=['Translated_Review'],inplace=True)\n",
    "\n",
    "apps_df['Installs']=apps_df['Installs'].str.replace(',','').str.replace('+','').astype(int)\n",
    "apps_df['Price']=apps_df['Price'].str.replace('$','').astype(float)\n",
    "\n",
    "sia = SentimentIntensityAnalyzer()\n",
    "\n",
    "reviews_df['Sentiment_Score']=reviews_df['Translated_Review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])\n",
    "\n",
    "merged_df=pd.merge(apps_df,reviews_df,on='App',how='inner')\n",
    "\n",
    "def convert_size(size):\n",
    "    if 'M' in size:\n",
    "        return float(size.replace('M',''))\n",
    "    elif 'k' in size:\n",
    "        return float(size.replace('k',''))/1024\n",
    "    else:\n",
    "        return np.nan\n",
    "apps_df['Size']=apps_df['Size'].apply(convert_size)\n",
    "\n",
    "apps_df['Log_Installs']=np.log(apps_df['Installs'])\n",
    "\n",
    "apps_df['Reviews']=apps_df['Reviews'].astype(int)\n",
    "\n",
    "apps_df['Log_Reviews']=np.log(apps_df['Reviews'])\n",
    "\n",
    "apps_df['Revenue']=apps_df['Price']*apps_df['Installs']\n",
    "\n",
    "apps_df['Last Updated']=pd.to_datetime(apps_df['Last Updated'],errors='coerce')\n",
    "\n",
    "apps_df['Year']=apps_df['Last Updated'].dt.year\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8cde96b1-9fad-4930-8c35-0ab779eb40be",
   "metadata": {},
   "outputs": [],
   "source": [
    "html_files_path = './plots'\n",
    "os.makedirs(html_files_path, exist_ok=True)\n",
    "plot_containers = ''\n",
    "\n",
    "def save_plot_as_html(fig, filename, insight):\n",
    "    global plot_containers\n",
    "    filepath = os.path.join(html_files_path, filename)\n",
    "    html_content = pio.to_html(fig, full_html=False, include_plotlyjs='inline')\n",
    "    plot_containers += f\"\"\"\n",
    "    <div class=\"plot-container\" id=\"{filename}\" onclick=\"openPlot('{filename}')\">\n",
    "        <div class=\"plot\">{html_content}</div>\n",
    "        <div class=\"insights\">{insight}</div>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    fig.write_html(filepath, full_html=False, include_plotlyjs='inline')\n",
    "\n",
    "plot_width = 900\n",
    "plot_height = 500\n",
    "plot_bg_color = '#ffffff'  \n",
    "text_color = '#333333'     \n",
    "title_font = {'size': 20, 'color': text_color}\n",
    "axis_font = {'size': 14}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "33fedb70-59ea-4b3f-956b-ffb095b5ab6b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Sentiment=Negative<br>Rating_Group=3–4<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Negative",
         "marker": {
          "color": "red",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Negative",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x",
         "y": {
          "bdata": "RE4wIzU=",
          "dtype": "i1"
         },
         "yaxis": "y"
        },
        {
         "hovertemplate": "Sentiment=Negative<br>Rating_Group=4–5<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Negative",
         "marker": {
          "color": "red",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Negative",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x2",
         "y": {
          "bdata": "LQEQA5UPbgFGAQ==",
          "dtype": "i2"
         },
         "yaxis": "y2"
        },
        {
         "hovertemplate": "Sentiment=Neutral<br>Rating_Group=3–4<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Neutral",
         "marker": {
          "color": "grey",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Neutral",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x",
         "y": {
          "bdata": "bikSDR4=",
          "dtype": "i1"
         },
         "yaxis": "y"
        },
        {
         "hovertemplate": "Sentiment=Neutral<br>Rating_Group=4–5<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Neutral",
         "marker": {
          "color": "grey",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Neutral",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x2",
         "y": {
          "bdata": "kQB4AZECAwGCAA==",
          "dtype": "i2"
         },
         "yaxis": "y2"
        },
        {
         "hovertemplate": "Sentiment=Positive<br>Rating_Group=3–4<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Positive",
         "marker": {
          "color": "green",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Positive",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x",
         "y": {
          "bdata": "ZgHGAJYAWgCAAA==",
          "dtype": "i2"
         },
         "yaxis": "y"
        },
        {
         "hovertemplate": "Sentiment=Positive<br>Rating_Group=4–5<br>Category=%{x}<br>Count=%{y}<extra></extra>",
         "legendgroup": "Positive",
         "marker": {
          "color": "green",
          "pattern": {
           "shape": ""
          }
         },
         "name": "Positive",
         "orientation": "v",
         "showlegend": false,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "COMMUNICATION",
          "FAMILY",
          "GAME",
          "PHOTOGRAPHY",
          "SOCIAL"
         ],
         "xaxis": "x2",
         "y": {
          "bdata": "PAMkDyQwIwbUAQ==",
          "dtype": "i2"
         },
         "yaxis": "y2"
        }
       ],
       "layout": {
        "annotations": [
         {
          "font": {},
          "showarrow": false,
          "text": "Rating_Group=3–4",
          "x": 0.245,
          "xanchor": "center",
          "xref": "paper",
          "y": 1,
          "yanchor": "bottom",
          "yref": "paper"
         },
         {
          "font": {},
          "showarrow": false,
          "text": "Rating_Group=4–5",
          "x": 0.755,
          "xanchor": "center",
          "xref": "paper",
          "y": 1,
          "yanchor": "bottom",
          "yref": "paper"
         }
        ],
        "barmode": "stack",
        "font": {
         "color": "#333333",
         "size": 14
        },
        "height": 600,
        "legend": {
         "title": {
          "text": "Sentiment"
         },
         "tracegroupgap": 0
        },
        "paper_bgcolor": "#ffffff",
        "plot_bgcolor": "#ffffff",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#333333",
          "size": 20
         },
         "text": "Figure 1: Sentiment Distribution — Top 5 Categories, Segmented by Rating Group"
        },
        "width": 1200,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          0.49
         ],
         "title": {
          "text": "Category"
         }
        },
        "xaxis2": {
         "anchor": "y2",
         "domain": [
          0.51,
          1
         ],
         "matches": "x",
         "title": {
          "text": "Category"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Review Count"
         }
        },
        "yaxis2": {
         "anchor": "x2",
         "domain": [
          0,
          1
         ],
         "matches": "y",
         "showticklabels": false
        }
       }
      }
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Task 1 \n",
    "\n",
    "import plotly.express as px\n",
    "\n",
    "def rating_group(rating):\n",
    "    if rating <= 2:\n",
    "        return '1–2'\n",
    "    elif rating <= 4:\n",
    "        return '3–4'\n",
    "    else:\n",
    "        return '4–5'\n",
    "\n",
    "merged_df['Rating_Group'] = merged_df['Rating'].apply(rating_group)\n",
    "\n",
    "merged_df['Sentiment'] = merged_df['Sentiment_Score'].apply(\n",
    "    lambda x: 'Positive' if x > 0.05 else ('Negative' if x < -0.05 else 'Neutral')\n",
    ")\n",
    "\n",
    "merged_df['Reviews'] = pd.to_numeric(merged_df['Reviews'], errors='coerce')\n",
    "\n",
    "filtered = merged_df[merged_df['Reviews'] > 1000]\n",
    "\n",
    "\n",
    "top5 = (\n",
    "    filtered.groupby('Category')['Reviews']\n",
    "    .sum()\n",
    "    .sort_values(ascending=False)\n",
    "    .head(5)\n",
    "    .index.tolist()\n",
    ")\n",
    "\n",
    "filtered_top5 = filtered[filtered['Category'].isin(top5)]\n",
    "\n",
    "grouped = (\n",
    "    filtered_top5.groupby(['Category', 'Rating_Group', 'Sentiment'])\n",
    "    .size()\n",
    "    .reset_index(name='Count')\n",
    ")\n",
    "\n",
    "pivot = grouped.pivot_table(\n",
    "    index=['Category', 'Rating_Group'],\n",
    "    columns='Sentiment',\n",
    "    values='Count',\n",
    "    fill_value=0\n",
    ").reset_index()\n",
    "\n",
    "fig1 = px.bar(\n",
    "    grouped,\n",
    "    x='Category',\n",
    "    y='Count',\n",
    "    color='Sentiment',\n",
    "    barmode='stack',\n",
    "    facet_col='Rating_Group',\n",
    "    title=\"Figure 1: Sentiment Distribution — Top 5 Categories, Segmented by Rating Group\",\n",
    "    color_discrete_map={'Negative': 'red', 'Neutral': 'grey', 'Positive': 'green'}\n",
    ")\n",
    "fig1.update_layout(\n",
    "    plot_bgcolor=plot_bg_color,\n",
    "    paper_bgcolor=plot_bg_color,\n",
    "    font=dict(color=text_color, size=axis_font['size']),\n",
    "    title_font=title_font,\n",
    "    width=plot_width + 300,\n",
    "    height=plot_height + 100,\n",
    "    xaxis=dict(title='Category'),\n",
    "    yaxis=dict(title='Review Count')\n",
    ")\n",
    "\n",
    "\n",
    "fig1.show()\n",
    "\n",
    "insight_task1 = \"\"\"\n",
    "This chart shows how user sentiments (positive, neutral, negative) are distributed\n",
    "within different rating groups across the top 5 app categories. \n",
    "It helps understand whether higher-rated apps tend to receive more positive reviews \n",
    "compared to lower-rated ones.\n",
    "\"\"\"\n",
    "\n",
    "save_plot_as_html(fig1, \"fig1_stacked_sentiment.html\", insight_task1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a9fd242f-b3b5-4a5b-bdf6-68c373f1093b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "⏰ Outside 1–2 PM IST — Figure 2 not shown.\n"
     ]
    }
   ],
   "source": [
    "# Task 2 \n",
    "import plotly.graph_objects as go\n",
    "from datetime import datetime\n",
    "import pytz\n",
    "\n",
    "apps_df['Android Ver'] = apps_df['Android Ver'].astype(str).str.extract(r'(\\d+\\.\\d+)')\n",
    "apps_df['Android Ver'] = pd.to_numeric(apps_df['Android Ver'], errors='coerce')\n",
    "\n",
    "filtered = apps_df[\n",
    "    (apps_df['Installs'] >= 10000) &\n",
    "    (apps_df['Revenue'] >= 10000) &\n",
    "    (apps_df['Android Ver'] > 4.0) &\n",
    "    (apps_df['Size'] > 15) &\n",
    "    (apps_df['Content Rating'] == 'Everyone') &\n",
    "    (apps_df['App'].str.len() <= 30)\n",
    "]\n",
    "\n",
    "top3 = (\n",
    "    filtered.groupby('Category')['Installs']\n",
    "    .sum()\n",
    "    .sort_values(ascending=False)\n",
    "    .head(3)\n",
    "    .index.tolist()\n",
    ")\n",
    "\n",
    "filtered_top3 = filtered[filtered['Category'].isin(top3)]\n",
    "\n",
    "grouped2 = (\n",
    "    filtered_top3.groupby('Type').agg({\n",
    "        'Installs': 'mean',\n",
    "        'Revenue': 'mean'\n",
    "    }).reset_index()\n",
    ")\n",
    "\n",
    "now = datetime.now(pytz.timezone('Asia/Kolkata'))\n",
    "\n",
    "if 13 <= now.hour < 14:\n",
    "    fig2 = go.Figure()\n",
    "\n",
    "    fig2.add_trace(\n",
    "        go.Bar(\n",
    "            x=grouped2['Type'],\n",
    "            y=grouped2['Installs'],\n",
    "            name='Average Installs',\n",
    "            yaxis='y1',\n",
    "            marker_color='skyblue'\n",
    "        )\n",
    "    )\n",
    "\n",
    "    fig2.add_trace(\n",
    "        go.Scatter(\n",
    "            x=grouped2['Type'],\n",
    "            y=grouped2['Revenue'],\n",
    "            name='Average Revenue',\n",
    "            mode='lines+markers',\n",
    "            yaxis='y2',\n",
    "            marker=dict(color='orange')\n",
    "        )\n",
    "    )\n",
    "\n",
    "    fig2.update_layout(\n",
    "    plot_bgcolor=plot_bg_color,\n",
    "    paper_bgcolor=plot_bg_color,\n",
    "    font=dict(color=text_color, size=axis_font['size']),\n",
    "    title_font=title_font,\n",
    "    width=plot_width,\n",
    "    height=plot_height,\n",
    "    xaxis=dict(title='App Type (Free vs Paid)'),\n",
    "    yaxis=dict(title='Average Installs'),\n",
    "    yaxis2=dict(\n",
    "        title='Average Revenue',\n",
    "        overlaying='y',\n",
    "        side='right'\n",
    "    )\n",
    ")\n",
    "\n",
    "    fig2.show()\n",
    "\n",
    "    insight_task2 = \"\"\"\n",
    "    This dual-axis chart compares the average installs and revenue between free and paid apps \n",
    "    in the top 3 app categories. It highlights how free apps typically achieve higher installs, \n",
    "    while paid apps generate direct revenue.\n",
    "    \"\"\"\n",
    "\n",
    "    save_plot_as_html(fig2, \"fig2_dual_axis_installs_revenue.html\", insight_task2)\n",
    "else:\n",
    "    print(\"⏰ Outside 1–2 PM IST — Figure 2 not shown.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8e7166a3-dec4-4571-af14-f6c01bb6ca72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Filtered shape: (127, 17)\n",
      "✅ Top 10 Categories: ['FAMILY', 'SPORTS', 'GAME', 'ENTERTAINMENT', 'PERSONALIZATION', 'PHOTOGRAPHY', 'LIFESTYLE', 'EDUCATION', 'TOOLS', 'TRAVEL_AND_LOCAL']\n",
      "✅ Grouped3:\n",
      "            Category    Rating  Reviews\n",
      "0         EDUCATION  4.400000    57645\n",
      "1     ENTERTAINMENT  4.300000   869111\n",
      "2            FAMILY  4.395455  4544623\n",
      "3              GAME  4.313333  2397589\n",
      "4         LIFESTYLE  4.380000    42809\n",
      "5   PERSONALIZATION  4.475000   155996\n",
      "6       PHOTOGRAPHY  4.150000   563720\n",
      "7            SPORTS  4.342857  1982017\n",
      "8             TOOLS  4.200000     8010\n",
      "9  TRAVEL_AND_LOCAL  4.100000      974\n",
      "⏰ Outside 3–5 PM IST or no data left — Task 3 not shown.\n"
     ]
    }
   ],
   "source": [
    "# Task 3\n",
    "from datetime import datetime\n",
    "import pytz\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "filtered3 = apps_df[\n",
    "    (apps_df['Rating'] >= 4.0) &\n",
    "    (apps_df['Size'] >= 10) &\n",
    "    (apps_df['Last Updated'].dt.month == 1)\n",
    "].copy()\n",
    "\n",
    "print(\"✅ Filtered shape:\", filtered3.shape)\n",
    "\n",
    "top10 = (\n",
    "    filtered3.groupby('Category')['Installs']\n",
    "    .sum()\n",
    "    .sort_values(ascending=False)\n",
    "    .head(10)\n",
    "    .index.tolist()\n",
    ")\n",
    "\n",
    "filtered_top10 = filtered3[filtered3['Category'].isin(top10)]\n",
    "\n",
    "print(\"✅ Top 10 Categories:\", top10)\n",
    "\n",
    "grouped3 = (\n",
    "    filtered_top10.groupby('Category')\n",
    "    .agg({'Rating': 'mean', 'Reviews': 'sum'})\n",
    "    .reset_index()\n",
    ")\n",
    "\n",
    "print(\"✅ Grouped3:\\n\", grouped3)\n",
    "\n",
    "\n",
    "now = datetime.now(pytz.timezone('Asia/Kolkata'))\n",
    "\n",
    "if 15 <= now.hour < 17 and not grouped3.empty:\n",
    "\n",
    "    fig3 = go.Figure()\n",
    "\n",
    "    fig3.add_trace(go.Bar(\n",
    "        x=grouped3['Category'],\n",
    "        y=grouped3['Rating'],\n",
    "        name='Average Rating'\n",
    "    ))\n",
    "\n",
    "    fig3.add_trace(go.Bar(\n",
    "        x=grouped3['Category'],\n",
    "        y=grouped3['Reviews'],\n",
    "        name='Total Reviews'\n",
    "    ))\n",
    "\n",
    "    fig3.update_layout(\n",
    "    barmode='group',\n",
    "    plot_bgcolor=plot_bg_color,\n",
    "    paper_bgcolor=plot_bg_color,\n",
    "    font=dict(color=text_color, size=axis_font['size']),\n",
    "    title_font=title_font,\n",
    "    width=plot_width,\n",
    "    height=plot_height,\n",
    "    xaxis=dict(title='Category', tickangle=-30),\n",
    "    yaxis=dict(title='Values')\n",
    ")\n",
    "\n",
    "\n",
    "    fig3.show()\n",
    "\n",
    "    insight_task3 = \"\"\"\n",
    "    This grouped bar chart shows both the average rating and total review count \n",
    "    for the top 10 app categories by installs. It reveals which categories maintain high ratings \n",
    "    while also attracting significant user engagement.\n",
    "    \"\"\"\n",
    "\n",
    "\n",
    "    save_plot_as_html(fig3, \"fig3_grouped_bar_chart.html\", insight_task3)\n",
    "\n",
    "else:\n",
    "    print(\"⏰ Outside 3–5 PM IST or no data left — Task 3 not shown.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "8130f673-b5e8-4e87-a2f6-730d5accd538",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Filtered shape: (6586, 18)\n",
      "✅ Top 5 Categories: ['PRODUCTIVITY', 'TOOLS', 'FAMILY', 'PHOTOGRAPHY', 'TRAVEL_AND_LOCAL']\n",
      "✅ Grouped4 shape: (5, 4)\n",
      "✅ Sample:\n",
      "          Country          Category     Installs  Highlight\n",
      "0  United States            FAMILY  10041130590       True\n",
      "1  United States       PHOTOGRAPHY   9721243130       True\n",
      "2  United States      PRODUCTIVITY  12463070180       True\n",
      "3  United States             TOOLS  11450724500       True\n",
      "4  United States  TRAVEL_AND_LOCAL   6361859300       True\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "coloraxis": "coloraxis",
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Country=%{location}<br>Installs=%{z}<extra></extra>",
         "hovertext": [
          "FAMILY",
          "PHOTOGRAPHY",
          "PRODUCTIVITY",
          "TOOLS",
          "TRAVEL_AND_LOCAL"
         ],
         "locationmode": "country names",
         "locations": [
          "United States",
          "United States",
          "United States",
          "United States",
          "United States"
         ],
         "name": "",
         "type": "choropleth",
         "z": [
          10041130590,
          9721243130,
          12463070180,
          11450724500,
          6361859300
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "Installs"
          }
         },
         "colorscale": [
          [
           0,
           "#440154"
          ],
          [
           0.1111111111111111,
           "#482878"
          ],
          [
           0.2222222222222222,
           "#3e4989"
          ],
          [
           0.3333333333333333,
           "#31688e"
          ],
          [
           0.4444444444444444,
           "#26828e"
          ],
          [
           0.5555555555555556,
           "#1f9e89"
          ],
          [
           0.6666666666666666,
           "#35b779"
          ],
          [
           0.7777777777777778,
           "#6ece58"
          ],
          [
           0.8888888888888888,
           "#b5de2b"
          ],
          [
           1,
           "#fde725"
          ]
         ]
        },
        "font": {
         "color": "#333333",
         "size": 14
        },
        "geo": {
         "center": {},
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "projection": {
          "type": "equirectangular"
         },
         "showcoastlines": true,
         "showframe": false
        },
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "paper_bgcolor": "#ffffff",
        "plot_bgcolor": "#ffffff",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermap": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermap"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#333333",
          "size": 20
         },
         "text": "Figure 4: Global Installs by Category"
        },
        "width": 900
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABEUAAAH0CAYAAADbtZPPAAAAAXNSR0IArs4c6QAAIABJREFUeF7snQd4FVXXhVcCKXRIKKGEFHrvXRBQihWxIXbsvWBBQUQF7CiKFbEXULErqIig9N5LKKEnpNESIBCS/P/acfLdhHRuICHr+Nwnksw9c+adc+fOWbP32h6pqampUBMBERABERABERABERABERABERABERCBEkbAQ6JICTvjOlwREAEREAEREAEREAEREAEREAEREAEjIFFEE0EEREAEREAEREAEREAEREAEREAERKBEEpAoUiJPuw5aBERABERABERABERABERABERABERAoojmgAiIgAiIgAiIgAiIgAiIgAiIgAiIQIkkIFGkRJ52HbQIiIAIiIAIiIAIiIAIiIAIiIAIiIBEEc0BERABERABERABERABERABERABERCBEklAokiJPO06aBEQAREQAREQAREQAREQAREQAREQAYkimgMiIAIiIAIiIAIiIAIiIAIiIAIiIAIlkoBEkRJ52nXQIiACIiACIiACIiACIiACIiACIiACEkU0B0RABERABERABERABERABERABERABEokAYkiJfK066BFQAREQAREQAREQAREQAREQAREQAQkimgOiIAIiIAIiIAIiIAIiIAIiIAIiIAIlEgCEkVK5GnXQYuACIiACIiACIiACIiACIiACIiACEgU0RwQAREQAREQAREQAREQAREQAREQAREokQQkipTI066DFgEREAEREAEREAEREAEREAEREAERkCiiOSACIiACIiACIiACIiACIiACIiACIlAiCUgUKZGnXQctAiIgAiIgAiIgAiIgAiIgAiIgAiIgUURzQAREQAREQAREQAREQAREQAREQAREoEQSkChSIk+7DloEREAEREAEREAEREAEREAEREAERECiiOaACIiACIiACIiACIiACIiACIiACIhAiSQgUaREnnYdtAiIgAiIgAiIgAiIgAiIgAiIgAiIgEQRzQEREAEREAEREAEREAEREAEREAEREIESSUCiSIk87TpoERABERABERABERABERABERABERABiSKaAyIgAiIgAiIgAiIgAiIgAiIgAiIgAiWSgESREnnaddAiIAIiIAIiIAIiIAIiIAIiIAIiIAISRTQHREAEREAEREAEREAEREAEREAEREAESiQBiSIl8rTroEVABERABERABERABERABERABERABCSKaA6IgAiIgAiIgAiIgAiIgAiIgAiIgAiUSAISRUrkaddBi4AIiIAIiIAIiIAIiIAIiIAIiIAISBTRHBABERABERABERABERABERABERABESiRBCSKlMjTroMWAREQAREQAREQAREQAREQAREQARGQKKI5IAIiIAIiIAIiIAIiIAIiIAIiIAIiUCIJSBQpkaddBy0CIiACIiACIiACIiACIiACIiACIiBRRHOgWBB45pln8M8//+Cdd95BkyZNCjTmI0eOYOjQodi7dy8mTZqEqlWrFqifnN7077//2j7uv/9+3HTTTW7vv6h3mNV52rBhA+655x6ce+654N/d2Qqzb3eOU32JgAiIgAiIgAiIgAiIgAgUTQJnvSjiLJri4+OzPQMVKlSwxXa1atVw22234eDBg6e0+C6apzr3Uc2cORNPP/20cSgs0YCjSEhIwI8//ojp06dj+/btOHbsGDw9PVGjRg107doVl1xyiQkfpUqVSh/02SqKOCJK5rNTXEWVkiqKJCYmYvbs2fj666+xadMmm9M+Pj4IDg7GBRdcgIsvvhiVK1fO/UOoLURABERABERABERABERABE4rAYkiACSKAGvXrsXDDz+M/fv3o06dOoUmisybNw+jRo3CgQMHcpzorVu3xquvvpq+kJQoUjjXBXdHtpREUWTjxo146qmnTODLrlEgefLJJ00cyW87HRFO+R2TthcBERABERABERABERCBs4VAiRFFGjVqhNdeew1ly5Y9W86d244jMjISDzzwAFJTUxEXF4dKlSoViijiRKIkJSWhR48euOOOOxAaGorSpUvjxIkT2LFjB3744Qf8/PPP8PPzyzCGs1UUcU7ip59+igkTJtii2d0pJjlNFIkip/Yxcj4727ZtQ4MGDfDggw+iTZs2FiXCaJH169fjww8/xOLFi3HvvfcWKKVKosipnSO9WwREQAREQAREQAREQARyIiBRpITPD6ayDBs2DFzcMXXGWZC7O31m3759tijcunWr+UvccMMNGdJjXE8DPT++/PJL3HzzzfD397c/SRQpnIkqUaTgXCnkvfjii5YK1qlTJ7z00ksoX778SR1SbFy0aBGioqIwYMCAfO9Qoki+kekNIiACIiACIiACIiACIpBnAhJFXFDltPig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4voUOT/Tv7BFEdfFKNNUpk+fblEzfBLOMTNKgV4Kl156qT3xd10QZycMMMKEvi9kzQgGniumJjFihhWDXKMDnPPLCJC+ffvi999/t+on3A9FGCdyxZUZhRemOnARz2gA+j6wjCy9IN577z2LlihqogjPI0sVM3Jo165dFoXDRTkX0Zx7rPDi2nbs2GERAyyrSn6MlqE4xCgQ9sV5yuNMSkoytoMHD852HudVFOFngt4aLIHrzAEKNjQCZVUa7js3QYTH4IginP9Mb5o1a5ZF9vB4Ge3ASB9HWMvqs8BqTRS98lqGN7vPE48n85zm8TCChSkz559/foaKNq7M2SfPCdOXeJ2gIObqKcK/Z56HPD5W02E5W6eiUH6uDRwvzWZ5/eLngsIGP3eMaqPAk3n/HAPTkRgh5MqY0VacU4w6cW15EXmd7XlsPA7Ov4JE6+TnGqdtRUAEREAEREAEREAERCAzgbNeFCnMU+4qouQl1L8wx6K+RUAE8kegIGV487eH4re140/ipPqcjiNQGd7TQVn7EAEREAEREAEREAERyI6ARJECzg0aQdL0kE+6GXXAJ+RZGYcWsHu9TQREoJAJOF4WjrFuIe+uSHfPaA1W/6EPCyNOWCKXFYAKuzEyiWV4eR091Widwh6r+hcBERABERABERABETg7CUgUycN5zc73gW+lBwBD8GlWqCYCIlA8CLhWPXGMdYvHyE99lDl569DP5corr8TQoUNPi8iraJ1TP5/qQQREQAREQAREQARE4NQISBTJAz/6FowdO9bKyXJBwcaqGMy7ZzUJ+oOoiYAIFB8C9DMZOXKkCQAsdZ0X/5Lic3Q5j5QePvQToacPI97oS+T4n9D3qGfPngX2JcovI46DEXeK1skvOW0vAiIgAiIgAiIgAiLgLgISRdxFUv2IgAiIgAiIgAiIgAiIgAiIgAiIgAgUKwISRYrV6dJgRUAEREAEREAEREAEREAEREAEREAE3EVAooi7SKofERABERABERABERABERABERABERCBYkVAokixOl0arAiIgAiIgAiIgAiIgAiIgAiIgAiIgLsISBRxF0n1IwIiIAIiIAIiIAIiIAIiIAIiIAIiUKwISBQpVqdLgxUBERABERABERABERABERABERABEXAXAYki7iKpfkRABERABERABERABERABERABERABIoVAYkixep0abAiIAIiIAIiIAIiIAIiIAIiIAIiIALuIiBRxF0k1Y8IiIAIiIAIiIAIiIAIiIAIiIAIiECxIiBRpFidLg1WBERABERABERABERABERABERABETAXQQkiriLpPoRAREQAREQAREQAREQAREQAREQAREoVgQkihSr06XBioAIiIAIiIAIiIAIiIAIiIAIiIAIuIuARBF3kVQ/IiACIiACIiACIiACIiACIiACIiACxYqARJFidbo0WBEQAREQAREQAREQAREQAREQAREQAXcRkCjiLpLqRwREQAREQAREQAREQAREQAREQAREoFgRkChSrE6XBisCIiACIiACIiACIiACIiACIiACIuAuAhJF3EVS/YiACIiACIiACIiACIiACIiACIiACBQrAhJFitXp0mBFQAREQAREQAREQAREQAREQAREQATcRUCiiLtIqh8REAEREAEREAEREAEREAEREAEREIFiRUCiSLE6XRqsCIiACIiACIiACIiACIiACIiACIiAuwhIFHEXSfUjAiIgAiIgAiIgAiIgAiIgAiIgAiJQrAhIFClWp0uDFQEREAEREAEREAEREAEREAEREAERcBcBiSLuIql+REAEREAEREAEREAEREAEREAEREAEihUBiSLF6nRpsCIgAiIgAiIgAiIgAiIgAiIgAiIgAu4iIFHEXSTVjwiIgAiIgAiIgAiIgAiIgAiIgAiIQLEiIFGkWJ0uDVYEREAEREAEREAEREAEREAEREAERMBdBCSKuIuk+hEBERABERABERABERABERABERABEShWBCSKFKvTpcGKgAiIgAiIgAiIgAiIgAiIgAiIgAi4i4BEEXeRVD8iIAIiIAIiIAIiIAIiIAIiIAIiIALFioBEkWJ1ujRYERABERABERABERABERABERABERABdxGQKOIukupHBERABERABERABERABERABERABESgWBGQKFKsTpcGKwIiIAIiIAIiIAIiIAIiIAIiIAIi4C4CEkXcRVL9iIAIiIAIiIAIiIAIiIAIiIAIiIAIFCsCEkWK1enSYEVABERABERABERABERABERABERABNxFQKKIu0iqHxEQAREQAREQAREQAREQAREQAREQgWJFQKJIsTpdGqwIiIAIiIAIiIAIiIAIiIAIiIAIiIC7CEgUcRdJ9SMCIiACIiACIiACIiACIiACIiACIlCsCEgUKVanS4MVAREQAREQAREQAREQAREQAREQARFwFwGJIu4iqX5EQAREQAREQAREQAREQAREQAREQASKFQGJIsXqdGmwIiACIiACIiACIiACIiACIiACIiAC7iIgUcRdJNWPCIiACIiACIiACIiACIiACIiACIhAsSIgUaRYnS4NVgREQAREQAREQAREQAREQAREQAREwF0EJIq4i6T6EQEREAEREAEREAEREAEREAEREAERKFYEJIoUq9OlwYqACIiACIiACIiACIiACIiACIiACLiLgEQRd5FUPyIgAiIgAiIgAiIgAiIgAiIgAiIgAsWKgESRYnW6NFgREAEREAEREAEREAEREAEREAEREAF3EZAo4i6S6kcEREAEREAEREAEREAEREAEREAERKBYEZAoUqxOlwYrAiIgAiIgAiIgAiIgAiIgAiIgAiLgLgISRdxFUv2IgAiIgAiIgAiIgAiIgAiIgAiIgAgUKwISRYrV6dJgRUAEREAEREAEREAEREAEREAEREAE3EVAooi7SKofERABERABERABERABERABERABERCBYkVAokixOl0arAiIgAiIgAiIgAiIgAiIgAiIgAiIgLsISBRxF0n1IwIiIAIiIAIiIAIiIAIiIAIiIAIiUKwISBQpVqdLgxUBERABERABERABERABERABERABEXAXAYki7iKpfkRABERABERABERABERABERABERABIoVAYkixep0abAiIAIiIAIiIAIiIAIiIAIiIAIiIALuIiBRxF0k1Y8IiIAIiMBZTyA1NRWHDx9GUlJS+uv48eP2//ybp6cnSpcujVKlSqW/svqdsw3/piYCIiACIiACIiACInDmCEgUOXPstWcREAERKBIEYmNjceTIEVvsJyYm4tixY0hOTsaJEyfsZ0pKCqpXrw4vLy/bhts6L/6NAgAX+b6+vvb/3t7etm3ZsmVNJOD/u77KlSuX/rciAQBAREQEwsPDERcXB4ocmUWN8uXL4985cxAevg374mJRurQXvHicpUujtJeX/btCxYqIP3TQmBk3/kxJSfv3fyyTU/77vbNNSgqaNmuO+EOHEBAQgBoBNVAzIMD+3/5dowYqVapUVDBpHCIgAiIgAiIgAiJw1hGQKHLWnVIdkAiIgAj8j8DmzZuxadMmEza4sG/YsCFq166Nr76ajGnTpyE6Kgot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nJ4AAQIECBAgMMMCQpEZBnc6Ag0SEIo0CNZhF5aAUGRh9Vu1BAgQIECAAAGhiPcAgToEhCJ19FEVsywgFJnlBjg9AQIECBAgQGCGBYQiMwzudAQaJCAUaRCswy4sAaHIwuq3agkQIECAAAECQhHvAQJ1CAhF6uijKmZZQCgyyw1wegIECBAgQIDADAsIRWYY3OkINEhAKNIgWIddWAJCkYXVb9USIECAAAECBIQi3gME6hAQitTRR1UQIECAAAECBAgQIECAAAEChQJCkUIwywkQIECAAAECBAgQIECAAIE6BIQidfRRFQQIECBAgAABAgQIECBAgEChgFCkEMxyAgQIECBAgAABAgQIECBAoA4BoUgdfVQFAQIECBAgQIAAAQIECBAgUCggFCkEs5wAAQIECBAgQIAAAQIECBCoQ0AoUkcfVUGAAAECBAgQIECAAAECBAgUCghFCsEsJ0CAAAECBAgQIECAAAECBOoQEIrU0UdVECBAgAABAgQIECBAgAABAoUCQpFCMMsJECBAgAABAgQIECBAgACBOgSEInX0URUECBAgQIAAAQIECBAgQIBAoYBQpBDMcgIECBAgQIAAAQIECBAgQKAOAaFIHX1UBQECBAgQIECAAAECBAgQIFAoIBQpBLOcAAECBAgQIECAAAECBAgQqENAKFJHH1VBgAABAgQIECBAgAABAgQIFAoIRQrBLCdAgAABAgQIECBAgAABAgTqEBCK1NFHVRAgQIAAAQIECBAgQIAAAQKFAkKRQjDLCRAgQIAAAQIECBAgQIAAgToEhCJ19FEVBAgQIECAAAECBAgQIECAQKGAUKQQzHICBAgQIECAAAECBAgQIECgDgGhSB19VAUBAgQIECBAgAABAgQIECBQKCAUKQSznAABAgQIECBAgAABAgQIEKhDQChSRx9VQYAAAQIECBAgQIAAAQIECBQKCEUKwSwnQIAAAQIECBAgQIAAAQIE6hAQitTRR1UQIECAAAECBAgQIECAAAEChQJCkUIwywkQIECAAAECBAgQIECAAIE6BIQidfRRFQQIECBAgAABAgQIECBAgEChgFCkEMxyAgQIECBAgAABAgQIECBAoA4BoUgdfVQFAQIECBAgQIAAAQIECBAgUCggFCkEs5wAAQIECBAgQIAAAQIECBCoQ0AoUkcfVUGAAAECBAgQIECAAAECBAgUCghFCsEsJ0CAAAECBAgQIECAAAECBOoQEIrU0UdVECBAgAABAgQIECBAgAABAoUCQpFCMMsJECBAgAABAgQIECBAgACBOgSEInX0URUECBAgQIAAAQIECBAgQIBAoYBQpBDMcgIECBAgQIAAAQIECBAgQKAOAaFIHX1UBQECBAgQIECAAAECBAgQIFAoIBQpBLOcAAECBAgQIECAAAECBAgQqENAKFJHH1VBgAABAgQIECBAgAABAgQIFAoIRQrBLCdAgAABAgQIECBAgAABAgTqEBCK1NFHVRAgQIAAAQIECBAgQIAAAQKFAkKRQjDLCRAgQIAAAQIECBAgQIAAgToEhCJ19FEVBAgQIECAAAECBAgQIECAQKGAUKsV1wAAAANlSURBVKQQzHICBAgQIECAAAECBAgQIECgDgGhSB19VAUBAgQIECBAgAABAgQIECBQKCAUKQSznAABAgQIECBAgAABAgQIEKhDQChSRx9VQYAAAQIECBAgQIAAAQIECBQKCEUKwSwnQIAAAQIECBAgQIAAAQIE6hAQitTRR1UQIECAAAECBAgQIECAAAEChQJCkUIwywkQIECAAAECBAgQIECAAIE6BIQidfRRFQQIECBAgAABAgQIECBAgEChgFCkEMxyAgQIECBAgAABAgQIECBAoA4BoUgdfVQFAQIECBAgQIAAAQIECBAgUCggFCkEs5wAAQIECBAgQIAAAQIECBCoQ0AoUkcfVUGAAAECBAgQIECAAAECBAgUCghFCsEsJ0CAAAECBAgQIECAAAECBOoQEIrU0UdVECBAgAABAgQIECBAgAABAoUCQpFCMMsJECBAgAABAgQIECBAgACBOgSEInX0URUECBAgQIAAAQIECBAgQIBAoYBQpBDMcgIECBAgQIAAAQIECBAgQKAOAaFIHX1UBQECBAgQIECAAAECBAgQIFAoIBQpBLOcAAECBAgQIECAAAECBAgQqENAKFJHH1VBgAABAgQIECBAgAABAgQIFAoIRQrBLCdAgAABAgQIECBAgAABAgTqEBCK1NFHVRAgQIAAAQIECBAgQIAAAQKFAkKRQjDLCRAgQIAAAQIECBAgQIAAgToEhCJ19FEVBAgQIECAAAECBAgQIECAQKGAUKQQzHICBAgQIECAAAECBAgQIECgDgGhSB19VAUBAgQIECBAgAABAgQIECBQKCAUKQSznAABAgQIECBAgAABAgQIEKhDQChSRx9VQYAAAQIECBAgQIAAAQIECBQKCEUKwSwnQIAAAQIECBAgQIAAAQIE6hAQitTRR1UQIECAAAECBAgQIECAAAEChQJCkUIwywkQIECAAAECBAgQIECAAIE6BIQidfRRFQQIECBAgAABAgQIECBAgEChgFCkEMxyAgQIECBAgAABAgQIECBAoA4BoUgdfVQFAQIECBAgQIAAAQIECBAgUCggFCkEs5wAAQIECBAgQIAAAQIECBCoQ0AoUkcfVUGAAAECBAgQIECAAAECBAgUCghFCsEsJ0CAAAECBAgQIECAAAECBOoQ+C/BxUmU5Qr0ygAAAABJRU5ErkJggg=="
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# ✅ TASK 4 — Choropleth Map for Top 5 Categories (6 PM to 8 PM IST)\n",
    "from datetime import datetime\n",
    "import pytz\n",
    "import plotly.express as px\n",
    "\n",
    "# Set dummy country if not available\n",
    "if 'Country' not in apps_df.columns:\n",
    "    apps_df['Country'] = 'United States'  # fallback/default country\n",
    "\n",
    "# ➤ Filter out categories starting with A, C, G, S\n",
    "filtered4 = apps_df[~apps_df['Category'].str.startswith(('A', 'C', 'G', 'S'))].copy()\n",
    "print(\"✅ Filtered shape:\", filtered4.shape)\n",
    "\n",
    "# ➤ Get top 5 categories by total installs\n",
    "top5 = (\n",
    "    filtered4.groupby('Category')['Installs']\n",
    "    .sum()\n",
    "    .sort_values(ascending=False)\n",
    "    .head(5)\n",
    "    .index.tolist()\n",
    ")\n",
    "print(\"✅ Top 5 Categories:\", top5)\n",
    "\n",
    "# ➤ Keep only top 5 categories\n",
    "filtered_top5 = filtered4[filtered4['Category'].isin(top5)].copy()\n",
    "\n",
    "# ➤ Highlight if installs > 1 million\n",
    "filtered_top5['Highlight'] = filtered_top5['Installs'] > 1_000_000\n",
    "\n",
    "# ➤ Group by Country + Category\n",
    "grouped4 = (\n",
    "    filtered_top5.groupby(['Country', 'Category'])\n",
    "    .agg({'Installs': 'sum', 'Highlight': 'max'})\n",
    "    .reset_index()\n",
    ")\n",
    "print(\"✅ Grouped4 shape:\", grouped4.shape)\n",
    "print(\"✅ Sample:\\n\", grouped4.head())\n",
    "\n",
    "# ➤ Check time window\n",
    "now = datetime.now(pytz.timezone('Asia/Kolkata'))\n",
    "\n",
    "if 11 <= now.hour < 20 and not grouped4.empty:\n",
    "    fig4 = px.choropleth(\n",
    "        grouped4,\n",
    "        locations='Country',\n",
    "        locationmode='country names',\n",
    "        color='Installs',\n",
    "        hover_name='Category',\n",
    "        color_continuous_scale='Viridis',\n",
    "        title=\"Figure 4: Global Installs by Category\"\n",
    "    )\n",
    "\n",
    "    # ➤ Update layout\n",
    "    fig4.update_layout(\n",
    "        geo=dict(\n",
    "            showframe=False,\n",
    "            showcoastlines=True,\n",
    "            projection_type='equirectangular'\n",
    "        ),\n",
    "        plot_bgcolor=plot_bg_color,\n",
    "        paper_bgcolor=plot_bg_color,\n",
    "        font=dict(color=text_color, size=axis_font['size']),\n",
    "        title_font=title_font,\n",
    "        width=plot_width,\n",
    "        height=plot_height\n",
    "    )\n",
    "\n",
    "    fig4.show()\n",
    "\n",
    "    insight_task4 = \"\"\"\n",
    "    This interactive map displays global installs for the top 5 app categories, \n",
    "    highlighting regions and categories with the highest user reach. \n",
    "    Categories with over 1 million installs are emphasized to indicate major markets.\n",
    "    \"\"\"\n",
    "\n",
    "    # ➤ Save as HTML\n",
    "    save_plot_as_html(fig4, \"fig4_choropleth_map.html\", insight_task4)\n",
    "\n",
    "else:\n",
    "    print(\"⏰ Outside 6–8 PM IST or no data available — Task 4 not shown.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5e641c43-a16e-415b-b15f-4f9026290812",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Filtered shape: (3181, 19)\n",
      "⏰ Outside 5–7 PM IST or no data left — Task 5 not shown.\n"
     ]
    }
   ],
   "source": [
    "# Task 5 \n",
    "from textblob import TextBlob\n",
    "from datetime import datetime\n",
    "import pytz\n",
    "import plotly.express as px\n",
    "\n",
    "if 'Subjectivity' not in reviews_df.columns:\n",
    "    reviews_df['Subjectivity'] = reviews_df['Translated_Review'].apply(\n",
    "        lambda x: TextBlob(str(x)).sentiment.subjectivity\n",
    "    )\n",
    "\n",
    "merged5 = pd.merge(apps_df, reviews_df[['App', 'Subjectivity']], on='App', how='left')\n",
    "\n",
    "filtered5 = merged5[\n",
    "    (merged5['Rating'] > 3.5) &\n",
    "    (merged5['Category'].isin(['GAME', 'Beauty', 'Business', 'Comics', 'Communication',\n",
    "                               'Dating', 'Entertainment', 'Social', 'Event'])) &\n",
    "    (merged5['Reviews'] > 500) &\n",
    "    (~merged5['App'].str.contains('S', case=False, na=False)) &\n",
    "    (merged5['Subjectivity'] > 0.5) &\n",
    "    (merged5['Installs'] > 50_000)\n",
    "].copy()\n",
    "\n",
    "print(\"✅ Filtered shape:\", filtered5.shape)\n",
    "\n",
    "def translate_category(cat):\n",
    "    if cat == 'Beauty':\n",
    "        return 'सौंदर्य'  \n",
    "    elif cat == 'Business':\n",
    "        return 'வணிகம்'  \n",
    "    elif cat == 'Dating':\n",
    "        return 'Verabredung' \n",
    "    else:\n",
    "        return cat\n",
    "\n",
    "filtered5['Category_Label'] = filtered5['Category'].apply(translate_category)\n",
    "\n",
    "now = datetime.now(pytz.timezone('Asia/Kolkata'))\n",
    "\n",
    "if 17 <= now.hour < 19 and not filtered5.empty:\n",
    "\n",
    "    fig5 = px.scatter(\n",
    "        filtered5,\n",
    "        x='Size',\n",
    "        y='Rating',\n",
    "        size='Installs',\n",
    "        color='Category_Label',\n",
    "        hover_name='App',\n",
    "        title=\"Figure 5: Bubble Chart - Size vs Rating (Bubble = Installs)\",\n",
    "    )\n",
    "\n",
    "    fig5.for_each_trace(\n",
    "        lambda t: t.update(marker=dict(color='pink'))\n",
    "        if 'GAME' in t.name.upper() or 'Game' in t.name else ()\n",
    "    )\n",
    "\n",
    "    fig5.update_layout(\n",
    "    plot_bgcolor=plot_bg_color,\n",
    "    paper_bgcolor=plot_bg_color,\n",
    "    font=dict(color=text_color, size=axis_font['size']),\n",
    "    title_font=title_font,\n",
    "    width=plot_width,\n",
    "    height=plot_height,\n",
    "    xaxis=dict(title='App Size (MB)'),\n",
    "    yaxis=dict(title='Average Rating')\n",
    ")\n",
    "\n",
    "\n",
    "    fig5.show()\n",
    "\n",
    "    insight_task5 = \"\"\"\n",
    "    This bubble chart visualizes how app size relates to average rating, \n",
    "    with bubble size representing the number of installs. \n",
    "    It highlights whether larger apps tend to achieve better ratings and bigger audiences.\n",
    "    The Game category is emphasized in pink, and select categories are translated \n",
    "    for regional context.\n",
    "    \"\"\"\n",
    "\n",
    "\n",
    "    save_plot_as_html(fig5, \"fig5_bubble_chart.html\", insight_task5)\n",
    "\n",
    "else:\n",
    "    print(\"⏰ Outside 5–7 PM IST or no data left — Task 5 not shown.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "66a24544-abfd-47af-8674-d27b9fd26da3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Filtered shape: (214, 18)\n",
      "✅ Grouped6:\n",
      "    YearMonth       Category_Label  Installs\n",
      "46   2018-03               BEAUTY      5000\n",
      "58   2018-06               BEAUTY   1000000\n",
      "64   2018-07               BEAUTY   1000000\n",
      "72   2018-08               BEAUTY    100000\n",
      "5    2014-10  BOOKS_AND_REFERENCE    500000\n",
      "✅ Grouped6 with % Change:\n",
      "    YearMonth       Category_Label  Installs  Pct_Change\n",
      "46   2018-03               BEAUTY      5000    0.000000\n",
      "58   2018-06               BEAUTY   1000000  199.000000\n",
      "64   2018-07               BEAUTY   1000000    0.000000\n",
      "72   2018-08               BEAUTY    100000   -0.900000\n",
      "5    2014-10  BOOKS_AND_REFERENCE    500000    0.000000\n",
      "6    2014-11  BOOKS_AND_REFERENCE   5000000    9.000000\n",
      "10   2015-07  BOOKS_AND_REFERENCE  10000000    1.000000\n",
      "18   2016-06  BOOKS_AND_REFERENCE     60000   -0.994000\n",
      "21   2016-08  BOOKS_AND_REFERENCE    100000    0.666667\n",
      "27   2017-02  BOOKS_AND_REFERENCE    100000    0.000000\n",
      "⏰ Outside 6–9 PM IST or no data left — Task 6 not shown.\n"
     ]
    }
   ],
   "source": [
    "# Task 6\n",
    "from datetime import datetime\n",
    "import pytz\n",
    "import plotly.graph_objects as go\n",
    "\n",
    "filtered6 = apps_df[\n",
    "    (~apps_df['App'].str.startswith(('X', 'Y', 'Z'), na=False)) &\n",
    "    (apps_df['Category'].str.startswith(('E', 'C', 'B'))) &\n",
    "    (apps_df['Reviews'] > 500) &\n",
    "    (~apps_df['App'].str.contains('S', case=False, na=False))\n",
    "].copy()\n",
    "\n",
    "print(\"✅ Filtered shape:\", filtered6.shape)\n",
    "\n",
    "def translate_category(cat):\n",
    "    if cat == 'Beauty':\n",
    "        return 'सौंदर्य' \n",
    "    elif cat == 'Business':\n",
    "        return 'வணிகம்'   \n",
    "    elif cat == 'Dating':\n",
    "        return 'Verabredung'\n",
    "    else:\n",
    "        return cat\n",
    "\n",
    "filtered6['Category_Label'] = filtered6['Category'].apply(translate_category)\n",
    "\n",
    "filtered6['YearMonth'] = filtered6['Last Updated'].dt.to_period('M')\n",
    "grouped6 = (\n",
    "    filtered6.groupby(['YearMonth', 'Category_Label'])['Installs']\n",
    "    .sum()\n",
    "    .reset_index()\n",
    "    .sort_values(['Category_Label', 'YearMonth'])\n",
    ")\n",
    "\n",
    "print(\"✅ Grouped6:\\n\", grouped6.head())\n",
    "\n",
    "grouped6['Pct_Change'] = (\n",
    "    grouped6.groupby('Category_Label')['Installs']\n",
    "    .pct_change()\n",
    "    .fillna(0)\n",
    ")\n",
    "\n",
    "print(\"✅ Grouped6 with % Change:\\n\", grouped6.head(10))\n",
    "\n",
    "now = datetime.now(pytz.timezone('Asia/Kolkata'))\n",
    "\n",
    "if 18 <= now.hour < 21 and not grouped6.empty:\n",
    "\n",
    "    fig6 = go.Figure()\n",
    "\n",
    "    categories = grouped6['Category_Label'].unique()\n",
    "\n",
    "    for cat in categories:\n",
    "        cat_data = grouped6[grouped6['Category_Label'] == cat]\n",
    "\n",
    "        fig6.add_trace(go.Scatter(\n",
    "            x=cat_data['YearMonth'].astype(str),\n",
    "            y=cat_data['Installs'],\n",
    "            mode='lines',\n",
    "            name=cat\n",
    "        ))\n",
    "\n",
    "        highlight = cat_data[cat_data['Pct_Change'] > 0.2]\n",
    "        fig6.add_trace(go.Scatter(\n",
    "            x=highlight['YearMonth'].astype(str),\n",
    "            y=highlight['Installs'],\n",
    "            mode='lines',\n",
    "            line=dict(width=0),\n",
    "            showlegend=False,\n",
    "            fill='tozeroy',\n",
    "            fillcolor='rgba(255, 0, 0, 0.2)'  \n",
    "        ))\n",
    "\n",
    "    fig6.update_layout(\n",
    "    plot_bgcolor=plot_bg_color,\n",
    "    paper_bgcolor=plot_bg_color,\n",
    "    font=dict(color=text_color, size=axis_font['size']),\n",
    "    title_font=title_font,\n",
    "    width=plot_width,\n",
    "    height=plot_height,\n",
    "    xaxis=dict(title='Date'),\n",
    "    yaxis=dict(title='Total Installs')\n",
    ")\n",
    "\n",
    "\n",
    "    fig6.show()\n",
    "\n",
    "    insight_task6 = \"\"\"\n",
    "    This time series shows how total installs have changed over time for selected app categories. \n",
    "    Periods where installs grew by more than 20% month-over-month are shaded, \n",
    "    indicating spikes in popularity or seasonal trends.\n",
    "    \"\"\"\n",
    "\n",
    "\n",
    "    save_plot_as_html(fig6, \"fig6_time_series.html\", insight_task6)\n",
    "\n",
    "else:\n",
    "    print(\"⏰ Outside 6–9 PM IST or no data left — Task 6 not shown.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22ac2a88-e9da-410b-abcf-2ba7eed4fff2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
