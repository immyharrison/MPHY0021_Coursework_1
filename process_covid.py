# FIXME add needed imports
# import json file 
import json
# import to get file path 
import os 

current_filepath = os.getcwd()


def load_covid_data(filepath):
      list_files = os.listdir(filepath)
    #check for all files in folder
    check_files_counter = 0
    for fname in list_files: 
        # if file type is json file
        if fname.endswith('.json'):
            # open file
            open_covid_data = open(fname)
            #load file
            covid_data_json = json.load(open_covid_data)
            #load file as string
            covid_data_str = json.dumps(covid_data_json)
            #print(covid_data_str)
            #check title of file fits schema
            # the catagories being checked if present
    

def cases_per_population_by_age(input_data):
    raise NotImplementedError

def hospital_vs_confirmed(input_data):
    raise NotImplementedError

def generate_data_plot_confirmed(input_data, sex, max_age, status):
    """
    At most one of sex or max_age allowed at a time.
    sex: only 'male' or 'female'
    max_age: sums all bins below this value, including the one it is in.
    status: 'new' or 'total' (default: 'total')
    """
    raise NotImplementedError

def create_confirmed_plot(input_data, sex=False, max_ages=[], status=..., save=...):
    # FIXME check that only sex or age is specified.
    fig = plt.figure(figsize=(10, 10))
    # FIXME change logic so this runs only when the sex plot is required
    for sex in ['male', 'female']:
        # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
        plt.plot('date', 'value', changeme)
    # FIXME change logic so this runs only when the age plot is required
    for age in max_ages:
        # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
        plt.plot('date', 'value', changeme)
    fig.autofmt_xdate()  # To show dates nicely
    # TODO add title with "Confirmed cases in ..."
    # TODO Add x label to inform they are dates
    # TODO Add y label to inform they are number of cases
    # TODO Add legend
    # TODO Change logic to show or save it into a '{region_name}_evolution_cases_{type}.png'
    #      where type may be sex or age
    plt.show()

def compute_running_average(data, window):
    raise NotImplementedError

def simple_derivative(data):
    raise NotImplementedError

def count_high_rain_low_tests_days(input_data):
    raise NotImplementedError
