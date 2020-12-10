from process_covid import match_age_bins ,check_json_strucutre, hospital_vs_confirmed ,covid_data, generate_data_plot_confirmed, load_covid_data, compute_running_average, simple_derivative, cases_per_population_by_age
import pytest 

def test_generate_data_plot_confirmed():
    input_data = covid_data
    sex = 4 
    max_age = False
    status = 'total'

    actual = generate_data_plot_confirmed(covid_data, sex, max_age, status)
    expected = ([ ], [ ], '', 'Error in input value for sex')
    assert actual == expected
    
def test_check_json_strucutre():
    input_data = {"metadata":{"age_binning": {"hospitalizations": ["0-24","25-49","50-74","75-"],}},},
    {"evolution":{"2020-03-16": {"hospitalizations": {
        "hospitalized": {
          "new": {
            "all": None,
            "male": 28,
            "female": 44,
            "age": [
              15,
              23,
              21,
              13
            ]
    }}}}}}
    {"epidemiology": {
        "confirmed": {
          "new": {
            "all": None,
            "male": 66,
            "female": 78,
            "age": [
              29,
              49,
              43,
              23
            ]
          },
      }}}
    actual = check_json_strucutre(input_data)
    expected = 'Error: ','weather', ' not found in the loaded data'
    assert actual == expected

def test_hospital_vs_confirmed():
    input_data = {"metadata":{"age_binning": {"hospitalizations": ["0-24","25-49","50-74","75-"],}},},
    {"evolution":{"2020-03-16": {"hospitalizations": {
        "hospitalized": {
          "new": {
            "all": None,
            "male": 28,
            "female": 44,
            "age": [
              15,
              23,
              21,
              13
            ]
    }}}}}}
    {"epidemiology": {
        "confirmed": {
          "new": {
            "all": None,
            "male": 66,
            "female": 78,
            "age": [
              29,
              49,
              43,
              23
            ]
          },
      }}}
    actual = hospital_vs_confirmed(input_data)
    expected = 'error: missing data'
    assert actual == expected