from dash import Dash, dcc, html
import plotly.express as px
import plotly.io as pio
import pandas as pd
import os

# Set the renderer to 'browser'
pio.renderers.default = 'browser'

# Load the state-grouped data
state_grouped = pd.read_csv("cleaned_MSA_patents_data _2015.csv")

# First Plotly Figure (Choropleth Map)
# fig1 = px.choropleth(
#     state_grouped,
#     locations='State',
#     locationmode='USA-states',
#     color='No of Patents in 2015',
#     hover_name='State',
#     scope='usa',
#     color_continuous_scale="Blues",
#     title='Number of Patents by U.S. State (2015)'
# )

fig1 = px.scatter_mapbox(
    state_grouped,
    lat="Latitude",
    lon="Longitude",
    size="No Of Patents",
    color="No Of Patents",
    hover_name="U.S. Regional Title",
    mapbox_style="open-street-map",
    zoom=3,
    title="U.S. Regions with Patents (2015)"
)

# fig1 = px.scatter_mapbox(
#     state_grouped,
#     lat="Latitude",
#     lon="Longitude",
#     color="No Of Patents",
#     size="No Of Patents",
#     hover_name="U.S. Regional Title",
#     mapbox_style="carto-positron",
#     zoom=3,
#     center={"lat": state_grouped["Latitude"].mean(), "lon": state_grouped["Longitude"].mean()},
#     title="Number of Patents by U.S. MSA (2015)"
# )

# fig1.update_layout(
#     coloraxis_colorbar={
#         "title": "No Of Patents",
#         "tickvals": [state_grouped["No Of Patents"].min(), state_grouped["No Of Patents"].max()],
#         "ticktext": ["Low", "High"]
#     },
#     margin={"r": 0, "t": 30, "l": 0, "b": 0}
# )


# Second Plotly Figure (Top 10 States Bar Plot)
state_grouped = state_grouped.sort_values(by='No Of Patents', ascending=False).head(10)
# fig2 = px.bar(
#     state_grouped,
#     x='State',
#     y='2015',
#     title='Top 10 States with Highest Number of Patents in 2015',
#     labels={'No of Patents in 2015': 'Number of Patents'},
#     template='plotly_dark',
#     text='No of Patents in 2015'
# )
fig2 = px.bar(
    state_grouped,
    x='No Of Patents',
    y='U.S. Regional Title',
    title='Top 10 States with Highest Number of Patents in 2015',
    labels={'No of Patents in 2015': 'Number of Patents'},
    template='plotly_dark',
    text='No Of Patents',
    orientation='h'  # Horizontal orientation
)

# Adjust text and labels
fig2.update_traces(textposition='outside')
fig2.update_layout(yaxis=dict(tickangle=0))
# fig2.show()

# Dash App with Plotly for both plots
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Title: Distribution of patents in US - Metropolitan Statistical Areas in 2015", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding': '10px', 'background-color': '#343a40', 'color': '#f8f9fa'}),
        html.H3("IE6600: Computation and Visualization Course", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.H4("Assignment 3", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.P("Instructor: Srinivasan Radhakrishnan", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.P("December 5th, 2024", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
    ], style={'margin-bottom': '20px'}),

    html.Div([
        html.Div([
            # html.H2("U.S. Patents Distribution in 2015", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
            html.P("""
                The map below shows the distribution of patents across various U.S Metropolitan Statistical Areas in 2015. 
            """, style={'text-align': 'center', 'font-size': '16px', 'margin-bottom': '20px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            dcc.Graph(figure=fig1, config={'displayModeBar': False}),
        ], style={'padding': '20px', 'border-radius': '10px', 'background-color': '#3a3b3c', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px'}),

    html.Div([
        html.Div([
            html.H2("Top 10 MSA with Highest Number of Patents in 2015", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
            html.P("""
                The bar chart below highlights the top 10 MSA with the highest number of patents in 2015. 
                The exact count of patents is displayed above each bar for clarity.
            """, style={'text-align': 'center', 'font-size': '16px', 'margin-bottom': '20px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            dcc.Graph(figure=fig2, config={'displayModeBar': False}),
        ], style={'padding': '20px', 'border-radius': '10px', 'background-color': '#3a3b3c', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px'}),

    # Summary Section
    html.Div([
        html.H2("Summary", style={'text-align': 'left', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
        html.P("Data Preparation: The displayed patents data was imported from U.S. PATENT AND TRADEMARK OFFICE into a .csv file.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.P("Data Preprocessing:", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.Ul([
            html.Li("The data types of each column were verified and modified accordingly. The US regional Title column was cleaned using regex.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("The USA map from Plotly was used to get the United States of America map with proper boundaries.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
        ], style={'margin-bottom': '10px', 'padding-left': '20px'}),
        html.P("Setup: Python, Pandas, Plotly, Dash app, Heroku", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.P("Bar Graph:", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.Ul([
            html.Li("San Jose - Sunnyvale- Santa Clara leads significantly with 14618 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("Followed by San Francisco- Oakland- Fremont with9732 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("Apart from that, states like IL, MN, PA, and FL have almost equal numbers of patents in the technology field.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("Los Angeles- Long Beach- Santa Ana and Boston - Cambridge - Quincy  approximately have about 6000 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("In fifth position we have San Diego Carlsbad- SAn Macros with about 5400 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("Detroit- Warren - Livonia, Minneapolis-St. Paul Bloomington,Chicago - Joliet - Naperville have approximately 3000-4000 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
        ], style={'margin-bottom': '10px', 'padding-left': '20px'}),
        html.P("Choropleth Map:", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
        html.Ul([
            html.Li("The lighter the color indicates more patents from that MSA.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("The darker, the color on map, indicates a smaller number of patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Li("From the map, San Jose - Sunnyvale- Santa Clara from CA state has more patents with 14618 hence its color is yellow.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
        ], style={'margin-bottom': '10px', 'padding-left': '20px'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px', 'padding': '20px', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),

    # Footer
    html.Footer([
        html.P("Author: Pillalamarri Venkata Raja Pratyusha", style={'text-align': 'center', 'color': '#f8f9fa', 'font-family': 'Arial, sans-serif', 'padding': '10px'})
    ], style={'background-color': '#343a40', 'position': 'fixed', 'width': '100%', 'bottom': '0'})
], style={'background-color': '#121212', 'color': '#f8f9fa', 'padding-bottom': '40px'})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8027))
    app.run_server(debug=False, host='0.0.0.0', port=port)
