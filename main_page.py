# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import streamlit.components.v1 as components


def main_page():

    st.sidebar.markdown("# Main page 🎈")
    st.image("image/DS4A.svg",width=200 )
    components.html("""
    <center> <h1>Team 48</h1> </center>
        <p> This application was made by Team 48 of Correlation One Colombia, using the data provided by the University of Cauca Popayan. </p>


    """)

    components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Data Analysis
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Through a dashboard you can view the historical data
            of the Confacauca University since 2010, finding information of interest such as the number of students per year, period and view them by career.
            <a href="https://app.powerbi.com/view?r=eyJrIjoiMWI2YTE3ODQtNzM4YS00YzZhLWFmYTEtZGY3YWQ4YmQxYTZlIiwidCI6IjU3N2ZjMWQ4LTA5MjItNDU4ZS04N2JmLWVjNGY0NTVlYjYwMCIsImMiOjR9&pageName=ReportSection">Go to the Dashboard</a>
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Predictions
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            <p>Using regressions, the application deals with two questions that concern the University
            How many students can there be in a given semester?
            How to know before the end of a semester if a student is going to pass a subject or not?</p>

            <p>For this we have two tools:</p>
            <ol>
            <li>Approval predictive model</li>
            <li>Number of student enrolled model</li>
            </ol>
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)

def page2():
    st.markdown("# Approval predictive model")
    st.sidebar.markdown("# Approval predictive model")

def page3():
    st.markdown("# Number of student enrolled model")
    st.sidebar.markdown("# Number of student enrolled model")

page_names_to_funcs = {
    "Main Page": main_page,
    #"page_2": page2,
    #"Number of student enrolled model": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
