from dash import Dash, dcc, html
import plotly.express as px
import plotly.io as pio
import pandas as pd

# Set the renderer to 'browser'
# pio.renderers.default = 'browser'

# Load the state-grouped data
state_grouped = pd.read_csv("state_grouped.csv")

# First Plotly Figure (Choropleth Map)
fig1 = px.choropleth(
    state_grouped,
    locations='State',
    locationmode='USA-states',
    color='No of Patents in 2015',
    hover_name='State',
    scope='usa',
    color_continuous_scale="Blues",
    title='Number of Patents by U.S. State (2015)'
)

# Second Plotly Figure (Top 10 States Bar Plot)
state_grouped = state_grouped.sort_values(by='No of Patents in 2015', ascending=False).head(10)
fig2 = px.bar(
    state_grouped,
    x='State',
    y='No of Patents in 2015',
    title='Top 10 States with Highest Number of Patents in 2015',
    labels={'No of Patents in 2015': 'Number of Patents'},
    template='plotly_dark',
    text='No of Patents in 2015'
)
fig2.update_traces(textposition='outside')

# Dash App with Plotly for both plots
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Patents Visualization", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding': '10px', 'background-color': '#343a40', 'color': '#f8f9fa'}),
    ], style={'margin-bottom': '20px'}),

    html.Div([
        html.Div([
            html.H2("U.S. Patents Distribution in 2015", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
            html.P("""
                The map below shows the distribution of patents across various U.S. States in 2015. 
                Darker regions indicate a higher number of patents.
            """, style={'text-align': 'center', 'font-size': '16px', 'margin-bottom': '20px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            dcc.Graph(figure=fig1, config={'displayModeBar': False}),
        ], style={'padding': '20px', 'border-radius': '10px', 'background-color': '#3a3b3c', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px'}),

    html.Div([
        html.Div([
            html.H2("Top 10 States with Highest Number of Patents in 2015", style={'text-align': 'center', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
            html.P("""
                The bar chart below highlights the top 10 states with the highest number of patents in 2015. 
                The exact count of patents is displayed above each bar for clarity.
            """, style={'text-align': 'center', 'font-size': '16px', 'margin-bottom': '20px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            dcc.Graph(figure=fig2, config={'displayModeBar': False}),
        ], style={'padding': '20px', 'border-radius': '10px', 'background-color': '#3a3b3c', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px'}),

    # Summary Section
    html.Div([
        html.H2("Summary", style={'text-align': 'left', 'font-family': 'Arial, sans-serif', 'padding-top': '20px', 'color': '#f8f9fa'}),
        html.Ul([
            html.Li("The first map provides an overview of patent distribution across U.S. states in 2015:", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Ul([
                html.Li("California leads significantly with over 40,000 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
                html.Li("Most other states have fewer patents, indicated by lighter shades.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
            ], style={'margin-bottom': '10px', 'padding-left': '20px'}),
            html.Li("The bar chart shows the top 10 states with the highest patent counts in 2015:", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
            html.Ul([
                html.Li("California tops the list with 40,106 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
                html.Li("New York follows with 12,244 patents, and Texas with 9,938.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
                html.Li("Massachusetts, Washington, and Michigan have between 6,839 and 5,545 patents.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'}),
                html.Li("Illinois, Minnesota, Pennsylvania, and Florida each have fewer than 5,000 patents, with Florida at 4,024.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
            ], style={'margin-bottom': '10px', 'padding-left': '20px'}),
            html.Li("Using **pandas** for data manipulation and **plotly** for visualization allowed for efficient analysis and presentation of patent distribution, clearly illustrating California's dominance in patent activity in 2015.", style={'font-size': '16px', 'margin-bottom': '10px', 'font-family': 'Arial, sans-serif', 'color': '#f8f9fa'})
        ], style={'margin-bottom': '20px', 'padding-left': '20px'}),
    ], style={'margin': '20px', 'background-color': '#212529', 'border-radius': '10px', 'padding': '20px', 'box-shadow': '0px 0px 10px rgba(0, 0, 0, 0.5)'}),

    # Footer
    html.Footer([
        html.P("Author: Pillalamarri Venkata Raja Pratyusha", style={'text-align': 'center', 'color': '#f8f9fa', 'font-family': 'Arial, sans-serif', 'padding': '10px'}),
    ], style={'background-color': '#343a40', 'position': 'fixed', 'width': '100%', 'bottom': '0'})
], style={'background-color': '#121212', 'color': '#f8f9fa', 'padding-bottom': '40px'})

if __name__ == "__main__":
    app.run_server(debug=False)
