# This note book is plotting India's Covid 19 data state wise manner
# Its taking help from plotly and matplotlib package
import pandas as pd  # deals with data inputs
import numpy as np  # deals with numerical data
import plotly.express as px  # calling plotly package
import plotly.graph_objs as go  # calling plotly graphs
import seaborn as sns  # support package for matplotlib
import warnings  # pkg to remove unwanted warnings from jupyter notebook

warnings.filterwarnings("ignore")

sns.set(context="notebook", palette="Spectral", style='darkgrid', font_scale=1.5,
        color_codes=True)  # setting colours and orientation of your notebook

# Deriving a equation for data plotting & Data preprocessing
india_dataset = pd.read_csv("data/covid_19_india.csv")  # Input your data over here
india_dataset['State/UnionTerritory'].unique()
india_dataset = india_dataset[~india_dataset['State/UnionTerritory'].isin(
    ['Unassigned', 'Nagaland#', 'Jharkhand#', 'Cases being reassigned to states'])]
india_dataset['Date'] = pd.to_datetime(india_dataset['Date'], format="%d/%m/%y")
india_dataset = india_dataset.replace(np.nan, 0)
# Loading the dataset
india_date_state_wise_cases = india_dataset.groupby(['Date', 'State/UnionTerritory'])[
    'Cured', 'Deaths', 'Confirmed'].sum().reset_index()  # Reading the change by sum()
india_date_state_wise_cases['Active_Cases'] = india_date_state_wise_cases['Confirmed'] - (
        india_date_state_wise_cases['Cured'] + india_date_state_wise_cases['Deaths'])
india_date_state_wise_cases['Mortality Rate(per 100)'] = (india_date_state_wise_cases['Deaths'] /
                                                          india_date_state_wise_cases[
                                                              'Confirmed']) * 100  # Extracting the equation

# Total Cases - Plotting the curve
total_confirmed_cases = india_date_state_wise_cases.groupby(['Date'])['Confirmed'].sum().reset_index()
fig = px.line(total_confirmed_cases, x="Date", y="Confirmed")

fig.update_layout(title='Positive cases of COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Positive of COVID-19 Cases'
                  )
fig.layout.template = 'plotly_dark'
fig.show()
# Plotting Before and After Active Corona Cases In India
total_active_cases = india_date_state_wise_cases.groupby(['Date'])['Active_Cases'].sum().reset_index()
fig = px.line(total_active_cases, x="Date", y="Active_Cases")
fig.add_annotation(
    x="2020-03-22",
    y=total_active_cases['Active_Cases'].max(),
    text="Lockdown starts",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="red"
    ),
)

fig.add_shape(
    # Line Vertical
    dict(
        type="line",
        x0="2020-03-22",
        y0=total_active_cases['Active_Cases'].max(),
        x1="2020-03-22",

        line=dict(
            color="red",
            width=3
        )
    ))
fig.add_annotation(
    x="2020-06-08",
    y=total_active_cases['Active_Cases'].max(),
    text="Lockdown ends",
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="red"
    ),
)

fig.add_shape(
    # Line Vertical
    dict(
        type="line",
        x0="2020-06-08",
        y0=total_active_cases['Active_Cases'].max(),
        x1="2020-06-08",

        line=dict(
            color="red",
            width=3
        )
    ))
fig.update_layout(title='Positive cases of COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Positive of COVID-19 Cases'
                  )
fig.layout.template = 'plotly_dark'
fig.show()

# Plotting a Log Curve of Active Covid-19 Cases over the time
total_active_cases['log_Active_Cases'] = np.log(total_active_cases['Active_Cases'])
fig = px.line(total_active_cases, x="Date", y="log_Active_Cases")
fig.update_layout(title='Logarithm of Active cases of COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Active Cases of COVID-19')
fig.layout.template = 'plotly_dark'
fig.show()

total_death_cases = india_date_state_wise_cases.groupby(['Date'])['Deaths'].sum().reset_index()
fig = px.line(total_death_cases, x="Date", y="Deaths")
fig.update_layout(title='Deaths COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Deaths from COVID-19')
fig.layout.template = 'plotly_dark'
fig.show()

total_death_cases['log_Deaths'] = np.log(total_death_cases['Deaths'])
fig = px.line(total_death_cases, x="Date", y="log_Deaths")
fig.update_layout(title='Logarithm of Deaths from COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Deaths of COVID-19')
fig.layout.template = 'plotly_dark'
fig.show()

most_effected_covid_states = india_date_state_wise_cases.groupby('State/UnionTerritory').sum().sort_values('Confirmed',
                                                                                                           ascending=False)
top10_most_effected_states = most_effected_covid_states.head(10)
top10_most_effected_states['State/UnionTerritory'] = top10_most_effected_states.index
top_states = top10_most_effected_states['State/UnionTerritory'].tolist()
# Check if the states name is present in "top 10 effected states" then include in the dataset
india_date_state_wise_cases_filtered = india_date_state_wise_cases[
    india_date_state_wise_cases['State/UnionTerritory'].isin(top_states)]

fig = px.line(india_date_state_wise_cases_filtered, x="Date", y="Confirmed", color='State/UnionTerritory',
              color_discrete_sequence=px.colors.qualitative.Dark24)
fig.update_layout(title='State wise cases of COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Confirmed Corona Cases over time State wise')
fig.layout.template = 'plotly_dark'
fig.show()

fig = px.line(india_date_state_wise_cases_filtered, x="Date", y="Active_Cases", color='State/UnionTerritory')
fig.update_layout(title='State wise cases of COVID-19',
                  xaxis_title='Date',
                  yaxis_title='Active Corona Cases over time State wise')
fig.layout.template = 'plotly_dark'
fig.show()

# Plotting Death Cases from Corona Virus in India
india_date_wise_cases = india_dataset.groupby(['Date'])['Cured', 'Deaths', 'Confirmed'].sum().reset_index()
india_date_wise_cases['Active_Cases'] = india_date_wise_cases['Confirmed'] - (
        india_date_wise_cases['Cured'] + india_date_wise_cases['Deaths'])
fig = go.Figure()
fig.add_trace(go.Scatter(x=india_date_wise_cases['Date'], y=india_date_wise_cases['Confirmed'],
                         mode='lines + markers',
                         name='Confirmed Cases'))
fig.add_trace(go.Scatter(x=india_date_wise_cases['Date'], y=india_date_wise_cases['Deaths'],
                         mode='lines + markers',
                         name='Deaths'))
fig.add_trace(go.Scatter(x=india_date_wise_cases['Date'], y=india_date_wise_cases['Cured'],
                         mode='lines + markers',
                         name='Cured'))
fig.add_trace(go.Scatter(x=india_date_wise_cases['Date'], y=india_date_wise_cases['Active_Cases'],
                         mode='lines + markers',
                         name='Active Cases'))
fig.update_layout(title='Daily Death,Recovered and New Cases of COVID-19 reported in India',
                  xaxis_title='Date',
                  yaxis_title='Cases')

fig.layout.template = 'plotly_dark'
fig.show()
