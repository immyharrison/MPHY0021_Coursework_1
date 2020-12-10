from process_covid import match_age_bins ,check_json_strucutre, hospital_vs_confirmed ,covid_data, generate_data_plot_confirmed, load_covid_data, compute_running_average, simple_derivative, cases_per_population_by_age
import pytest 
def test_simple_derivative():
    input_data = [None, 1, 2, None, 4]
    actual = simple_derivative(input_data)
    expected = [None, None, 1, None, None]
    assert actual == expected
    
def test_match_age_bins_not_possible ():
    A = ['0-14', '15-29','30-']
    B = ['0-19','20-39','40-']
    actual = match_age_bins(A,B)
    expected = ('error: age bins cannot be resported')
    assert actual == expected

def test_match_age_bins ():
    A = ['0-9','10-19','20-29','30-39','40-49','50-']
    B = ['0-19', '20-39', '40-']
    actual = match_age_bins(A,B)
    expected = ({'0-9': 0, '10-19': 0, '20-29': 1, '30-39': 1, '40-49': 2, '50-': 2}, {'0-19': 0, '20-39': 1, '40-': 2}, ['0-19', '0-19', '20-39', '20-39', '40-', '40-'])
    assert actual == expected 

def test_compute_running_average_window_even():
    data = [1,2,3,4,5,6,7,8,9,10]
    window = 5
    actual = compute_running_average(data, window)
    expected = [None, None, 3, 4, 5, 6, 7, 8, None,None]
    assert actual == expected

def test_compute_running_average_window_odd():
    data = [1,2,3 ,4]
    window = 2
    actual = compute_running_average(data, window)
    expected = [None, 2.0, 3.0, None]
    assert actual == expected 

def test_compute_running_average_2():
    data = [2, None, 4]
    window = 3
    actual = compute_running_average(data, window)
    expected = [None, 3.0, None]
    assert actual == expected 

def test_compute_running_average():
    data = [0, 1, 5, 2, 2, 5]
    window = 3 
    actual = compute_running_average(data, window)
    expected = [None, 2.0, 8/3, 3.0, 3.0, None]
    assert actual == expected

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