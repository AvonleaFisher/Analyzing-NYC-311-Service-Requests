import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_gif_component as gif
import plotly.express as px
import plotly.graph_objects as go
import gunicorn

app = dash.Dash(__name__)
server = app.server

ind_with_avg_calls = pd.read_csv('indicators_with_avg.csv')
noncompliance = pd.read_csv('noncompliance.csv')
mgc = pd.read_csv('mgc.csv')
noise_r = pd.read_csv('noiser.csv')
noise_v = pd.read_csv('noisev.csv')
noise_c = pd.read_csv('noisec.csv')
noise_s = pd.read_csv('noises.csv')
street = pd.read_csv('street.csv')
sidewalk = pd.read_csv('sidewalk.csv')
dt = pd.read_csv('dt.csv')
ot = pd.read_csv('ot.csv')
nt = pd.read_csv('nt.csv')
dd = pd.read_csv('dd.csv')
complaint_type_count_df = pd.read_csv('complaint_type_count.csv')
agency_count_df = pd.read_csv('agency_count.csv')


complaint_type_fig = px.bar(complaint_type_count_df, x="Total Calls", y="Complaint Type",
                            orientation='h',
                            height=700, color="Total Calls",
                            color_discrete_sequence=px.colors.sequential.thermal)

complaint_type_fig.update_layout(hovermode='x',
                                 title="Top 30 Most Frequent 311 Complaint Types",
                                 font=dict(family="silom",
                                           size=14, color="#58508d"))

agency_fig = px.bar(agency_count_df, x="Total Calls", y="Agency",
                    orientation='h',
                    height=700, color="Total Calls",
                    color_discrete_sequence=px.colors.sequential.thermal)

agency_fig.update_layout(hovermode='x',
                         title="311 Call Counts by Agency",
                         font=dict(family="silom",
                                   size=14, color="#58508d"))


fig2 = px.scatter(ind_with_avg_calls, x="community_board",
                  y="Avg daily calls per sqmi", color="Borough", height=700,
                  size='crime_per_1000', size_max=90, color_discrete_sequence=[
                                         "lightsalmon", "lightseagreen",
                                         "lightskyblue", "lightpink",
                                        "lightslategray"])

fig2.update_layout(hovermode='x',
                   title="Average Daily 311 Calls/Sq Mile",
                   xaxis_title="Community Board",
                   font=dict(family="silom",
                             size=14, color="#58508d",
                             ))

fig2.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=noise_r.Date, y=noise_r['Noise - Residential'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#003f5c'), name="Noise - Residential",
    stackgroup='one'
))

fig3.add_trace(go.Scatter(
    x=noise_s.Date, y=noise_s['Noise - Street/Sidewalk'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#58508d'), name='Noise - Street/Sidewalk',
    stackgroup='two'
))

fig3.add_trace(go.Scatter(
    x=noise_v.Date, y=noise_v['Noise - Vehicle'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#bc5090'), name='Noise - Vehicle',
    stackgroup='three'
))

fig3.add_trace(go.Scatter(
    x=noise_c.Date, y=noise_c['Noise - Commercial'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#ffa600'), name='Noise - Commercial',
    stackgroup='four'
))

fig3.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))

fig3.update_layout(title="Noise",
                   xaxis_title="Date",
                   yaxis_title="Total Calls",
                   height=700,
                   font=dict(family="silom",
                             size=14, color="#58508d"))

fig4 = go.Figure()

fig4.add_trace(go.Scatter(
    x=noncompliance.Date, y=noncompliance['Noncompliance With Phased Reopening'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#FF0000'), name="Noncompliance W/ Phased Reopening",
    stackgroup='one'
))

fig4.add_trace(go.Scatter(
    x=mgc.Date, y=mgc['Mass Gathering Complaint'],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#000000'), name="Mass Gathering Complaint",
    stackgroup='two'
))

fig4.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))

fig4.update_layout(title="COVID-19",
                   xaxis_title="Date",
                   yaxis_title="Total Calls",
                   height=700,
                   font=dict(family="silom",
                             size=14, color="#58508d"))

condition_fig = go.Figure()
condition_fig.add_trace(go.Scatter(
    x=street.Date, y=street["Street Condition"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#22DDD3'), name="Street Condition",
    stackgroup='one'
))

condition_fig.add_trace(go.Scatter(
    x=sidewalk.Date, y=sidewalk["Sidewalk Condition"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#6722DD'), name="Sidewalk Condition",
    stackgroup='one'

))

condition_fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01
))

condition_fig.update_layout(title="Sidewalk and Street Condition", height=700,
                            xaxis_title="Date",
                            yaxis_title="Total Calls",

                            font=dict(family="silom",
                                      size=14, color="#58508d"))

damaged_tree_fig = go.Figure()
damaged_tree_fig.add_trace(go.Scatter(
    x=dt.Date, y=dt["Damaged Tree"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#228B22'), name="Damaged Trees",
    stackgroup='one'
    ))

damaged_tree_fig.update_layout(title="Damaged Trees", height=700,
                               xaxis_title="Date",
                               yaxis_title="Total Calls",

                               font=dict(family="silom",
                                         size=14, color="#58508d"))

tree_fig = go.Figure()

tree_fig.add_trace(go.Scatter(
    x=ot.Date, y=ot["Overgrown Tree/Branches"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#8B4513'), name="Overgrown Tree/Branches",
    stackgroup='two'
    ))

tree_fig.add_trace(go.Scatter(
    x=dd.Date, y=dd["Dead/Dying Tree"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#C4285F'), name="Dead/Dying Tree",
    stackgroup='three'
    ))

tree_fig.add_trace(go.Scatter(
    x=nt.Date, y=nt["New Tree Request"],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='#491BE5'), name="New Tree Request",
    stackgroup='four'
    ))

tree_fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="right",
    x=0.99
))


tree_fig.update_layout(title="Other Tree-Related Requests", height=700,
                       xaxis_title="Date",
                       yaxis_title="Total Calls",

                       font=dict(family="silom",
                                 size=14, color="#58508d"))

app.layout = html.Div(className='row', children=[
    html.H1('NYC 311 Data Explorer (June-November 2020)',
            style={'color': '#6b508f', 'fontSize': 50, 'text-align': 'center', 'font-family':'silom'}),

    html.H1('About this Dashboard',
            style={'color': '#113c3c', 'fontSize': 30, 'text-align': 'left', 'margin-left': 100}),

    dcc.Markdown('''
    This dashboard hosts interactive plots of recent data obtained from two public sources:
    * [NYC OpenData 311 Service Requests from 2010 to Present](https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9)
    * [NYC Department of City Planning’s Community District Profiles](https://communityprofiles.planning.nyc.gov/)
    
    The 311 data displayed here is limited to calls that were made between June and November 2020. 
    The community district data consists of information from various sources and collectiod periods. 
    The code for this dashboard and an analysis of the data can be found in this [GitHub repo](https://github.com/AvonleaFisher/Analyzing-NYC-311-Service-Requests).
    ''', style={'margin-left': 100, 'margin-right': 150, 'fontSize': 27}),

    html.H1('Daily Call Volume by Month',
            style={'color': '#113c3c', 'fontSize': 30, 'text-align': 'left', 'margin-left': 100}),

    html.Div(
        gif.GifPlayer(gif='assets/June.gif', still='assets/June.gif', autoplay=True),
        style={'marginLeft': 130, 'width': '31%', 'display': 'inline-block'}
    ),
    html.Div(
        gif.GifPlayer(gif='assets/July.gif', still='assets/July.gif', autoplay=True),
        style={'width': '31%', 'display': 'inline-block'}
    ),
    html.Div(
        gif.GifPlayer(gif='assets/august.gif', still='assets/august.gif', autoplay=True),
        style={'width': '31%', 'display': 'inline-block'}
    ),
    html.Div(
        gif.GifPlayer(gif='assets/September.gif', still='assets/September.gif', autoplay=True),
        style={'marginLeft': 130, 'width': '31%', 'display': 'inline-block'}
    ),

    html.Div(
        gif.GifPlayer(gif='assets/October.gif', still='assets/October.gif', autoplay=True),
        style={'width': '31%', 'display': 'inline-block'}
    ),

    html.Div(
        gif.GifPlayer(gif='assets/November.gif', still='assets/November.gif', autoplay=True),
        style={'width': '31%', 'display': 'inline-block'}
    ),

    html.H1('Total Call Counts by Agency and Complaint Type',
            style={'color': '#113c3c', 'fontSize': 30, 'text-align': 'left', 'margin-left': 100}),

    html.Div(children=[
        dcc.Graph(id="graph0", figure=agency_fig),
        dcc.Graph(id="graph1", figure=complaint_type_fig),
        ]),

    html.H1('Daily Average Call Counts by Community Board (per sqmi)',
            style={'color': '#113c3c', 'fontSize': 30, 'text-align': 'left', 'margin-left': 100}),

    html.Div(children=[
        dcc.Graph(id="graph2", figure=fig2),

    html.H1('Daily Total Calls by Complaint Type',
            style={'color': '#113c3c', 'fontSize': 30, 'text-align': 'left', 'margin-left': 100}),
    ]),

    html.Div(children=[
    dcc.Graph(id="graph3", figure=fig3),
    dcc.Graph(id="graph4", figure=fig4),
    dcc.Graph(id="graph5", figure=condition_fig),
    dcc.Graph(id="graph6", figure=damaged_tree_fig),
    dcc.Graph(id="graph7", figure=tree_fig)

                      ])
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
