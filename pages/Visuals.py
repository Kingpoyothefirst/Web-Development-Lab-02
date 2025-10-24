# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.
import matplotlib.pyplot as plt


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

filename = r"C:\Users\Kofia\Downloads\Web Dev Lab02\Lab02\data.csv"
df = pd.read_csv(filename)
print(df.head())


# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Most Active Walking Day of the Week") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
st.bar_chart(df, x = "Category", y = "Value")
st.caption("This bar graph displays a person's most active walking day of the week and how many hours they walked for that day.")
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.



# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Hours of Walking vs Calories Burned Dynamic Graph") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
f_name = r"C:\Users\Kofia\Downloads\Web Dev Lab02\Lab02\data.json"
with open(f_name, "r") as f:
    info = json.load(f)    
params = info



chart_title = params.get("chart_title", "Line Graph")
data_points = params.get("data_points", [])

x_labels = []
y_values = []

for point in data_points:
    for key, value in point.items():
        if "label" in key:
            x_labels.append(value)
        elif "value" in key:
            y_values.append(value)

m_points = st.slider("Scale the # of hours", min_value = 0, max_value = 5, value = 1) # NEW
x_filtered = x_labels[:m_points]
y_filtered = y_values[:m_points]

scale = st.slider("Scale the Calories Burned", min_value = 0.0, max_value = 5.0, value = 1.0, step = 0.1)
y_scaled = [val * scale for val in y_filtered]

st.session_state.graph_data = {
    "x": x_filtered,
    "y": y_scaled,
    "scale": scale,
    "max_points": m_points
} #NEW   



print("x_filtered:", x_filtered)
print("y_scaled:", y_scaled)
print("Lengths:", len(x_filtered), len(y_scaled))
fig, ax = plt.subplots()
ax.plot(x_filtered, y_scaled, marker = "o")
ax.set_title(chart_title)
ax.set_xlabel("Hours")
ax.set_ylabel("Calories Burned")

st.pyplot(fig) # NEW
st.caption("This graph shows the amount of calories burned per hour you walk. There are two sliders. The first slider filters the number of hours on the graph, you can increase or decrease the hours shown on the graph. This works in coordination for the other slider, which scales the amount of calories burned. Not everbody burns the same amount of calories. The standard graph is based off the average person at an average pace. Different body types will burn different amount of calories per hour walked. These filters allow for someone to accurrately see an approximate amount of calories burned per hour for their specific bodytype.")

# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.







# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Amount of Calories Burned vs Pounds Lost Dynamic Graph") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
j_name = r"C:\Users\Kofia\Downloads\Web Dev Lab02\Lab02\data2.json"
with open(j_name, "r") as j:
    data = json.load(j)
lose = data

graph_title = lose.get("graph_title", "Scatterplot")
graph_points = lose.get("graph_points", [])

x_val = []
y_val = []

for point in graph_points:
    for key, value in point.items():
        if "key" in key:
            x_val.append(value)
        elif "point" in key:
            y_val.append(value)


y_scale = [val * scale for val in y_val]

st.session_state.scatter_data = {
    "x": x_val,
    "y": y_scale,
}

fig, ax = plt.subplots()

graph_type = st.selectbox("Choose the preferred graph type", ["Scatter", "Bar"]) # NEW

if graph_type == "Bar":
    ax.bar(x_val, y_scale)
    ax.set_title("Bar Graph")
elif graph_type == "Scatter":
    ax.scatter(x_val, y_scale, color = "red", s = 100)
    ax.set_title(f"{graph_title}")
    

ax.set_xlabel("Pounds Lost")
ax.set_ylabel("Calories Burned")

st.pyplot(fig)
st.caption("This chart shows the amount of calories you would need to burn to lose one pound. You can switch between a bar graph or a scatterplot based on preference.")

    
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.

