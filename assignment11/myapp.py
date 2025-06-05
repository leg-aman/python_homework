from dash import Dash, dcc, html, Input, Output # Dash components you need
import plotly.express as px # Dash relies on Plotly to actually do the plotting.  Plotly creates an HTML page with lots of JavaScript.
import plotly.data as pldata # This is only needed to give access to the Plotly built in datasets.

df = pldata.gapminder(return_type='pandas',  datetimes=True) # This loads one of the datasets


# Initialize Dash app
app = Dash(__name__) # This creates the app object, to wich various things are added below. 
# __name__ is the name of the running Python module, which is your main module in this case

# Layout: This section creates the HTML components
app.layout = html.Div([ # This div is for the dropdown you see at the top, and also for the graph itself
    dcc.Dropdown( # This creates the dropdown
        id="country-dropdown", # and it needs an id
        options=[{"label": country, "value": country} for country in df['country'].unique()], # This populates the dropdown with the list of stocks
        value="Canada" # This is the initial value
    ),
    dcc.Graph(id="gdp-growth") # And the graph itself has to have an ID
])

# Callback for dynamic updates
@app.callback( # OK, now this is a decorator.  Hmm, we haven't talked about decorators in Python.  This decorator is decorating the update_graph() function.
    # Because of the decorator, the update_graph() will be called when the stock-dropdown changes, passing the value selected in the dropdown.
    Output("gdp-growth", "figure"),  # And ... you get the graph back
    [Input("country-dropdown", "value")] # When you pass in the value of the dropdown.
)

def update_graph(country):
    filtered_df = df[df['country'] == country]  # Filter for the selected country
    fig = px.line(filtered_df, x='year', y='gdpPercap',
                  title=f"{country}'s GDP per Capita vs Year",hover_data=['country','continent'])  # Create a line plot
    return fig

# Run the app
if __name__ == "__main__": # if this is the main module of the program, and not something included by a different module
    app.run(debug=True) # start the Flask web server