# FIXME add needed imports
# import json file 
import json
# import to get file path 
import os 

current_filepath = os.getcwd()

# 2.1 load and chek json file 
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
    check_output = check_json_strucutre(covid_data_str)
    if check_output == 'correct structure':
        return(covid_data_json)
    else: 
        return (check_output)

def check_json_strucutre(str_input):
    matches = ["start_data","end_date","region","population","hospitalized", "epidemiology", "weather"]
    catagories_check_counter = 0
    for catagories in matches: 
        if any(catagories in str_input for catagories in matches):
            catagories_check_counter = catagories_check_counter + 1 
                #check if all catagories are present in file - print message is
    if catagories_check_counter == len(matches):
        output = 'correct structure'
    else:
        output = ('Error: ', catagories, ' not found in the loaded data')
    return output
covid_data = load_covid_data(current_filepath

# 2.2 evolution cases by age group and total pop 
def match_age_bins(binning_dic_hosp,binning_dic_pop):
    binning_dic_hosp = ['0-9','10-19','20-29','30-39','40-49','50-']
    binning_dic_pop = ['0-19', '20-39', '40-']
    count_hosp = 0
    count_pop = 0 
    hosp_age_bin_resort  = {}
    pop_age_bin_resort = {}
    new_age_bins_resort = []
    len_binning_dic_pop  = len(binning_dic_pop)
    len_binning_dic_hosp = len(binning_dic_hosp)
    while count_hosp < len_binning_dic_hosp and count_pop < len_binning_dic_pop:
            # upper limit for hospital age bin
            current_hosp_bin = (binning_dic_hosp[count_hosp]) 
            split = current_hosp_bin.split('-')
            limit_upper_hosp = (current_hosp_bin.partition('-')[2])
            limit_lower_hosp = (current_hosp_bin.partition('-')[0])
            # upper limit as number
            if limit_upper_hosp != '':
                limit_upper_hosp = int(limit_upper_hosp)
            #upper limit not defined so define as 100 max age 
            elif limit_upper_hosp == '' or limit_upper_hosp == ' ':
                limit_upper_hosp = int(100)
            if limit_lower_hosp != '':
                limit_lower_hosp = int(limit_lower_hosp)
            # upper value for population age bin
            current_pop_bin = (binning_dic_pop[count_pop]) 
            limit_upper_pop = (current_pop_bin.partition('-')[2])
            limit_lower_pop = (current_pop_bin.partition('-')[0])
            #upper limit defined as number
            if limit_upper_pop != '':
                limit_upper_pop = int(limit_upper_pop)
            # upper limit not defined set as 100
            elif limit_upper_pop == '' or limit_upper_pop == ' ':
                limit_upper_pop = int(100)
            if limit_lower_pop != '':
                limit_lower_pop = int(limit_lower_pop)

           
            if limit_upper_hosp > limit_upper_pop and limit_lower_hosp >= limit_lower_pop:
                position = min(count_hosp, count_pop)
                if current_pop_bin not in pop_age_bin_resort:
                    pop_age_bin_resort.update({current_pop_bin:(position)})
                if current_hosp_bin not in hosp_age_bin_resort:
                    hosp_age_bin_resort.update({current_hosp_bin:(position)})
                if current_pop_bin not in new_age_bins_resort: 
                    new_age_bins_resort.append(current_hosp_bin)
                count_pop += 1
            
            elif limit_upper_hosp > limit_upper_pop and limit_lower_hosp <= limit_lower_pop:
                error_message = ('error: age bins cannot be resported')
                break

            elif limit_upper_pop > limit_upper_hosp and limit_lower_hosp >= limit_lower_pop:
                position = min(count_hosp, count_pop)
                if current_hosp_bin not in hosp_age_bin_resort:
                    hosp_age_bin_resort.update({current_hosp_bin:(position)})
                if current_pop_bin not in pop_age_bin_resort:
                    pop_age_bin_resort.update({current_pop_bin:(position)})
                if (current_hosp_bin or current_pop_bin) not in new_age_bins_resort: 
                    new_age_bins_resort.append(current_pop_bin)
                count_hosp += 1
            
            elif limit_upper_pop > limit_upper_hosp and limit_lower_hosp <= limit_lower_pop:
                error_message = ('error: age bins cannot be resported')
                break
            elif limit_upper_hosp == limit_upper_pop:
                position = min(count_hosp, count_pop)
                if current_hosp_bin not in hosp_age_bin_resort:
                    hosp_age_bin_resort.update({current_hosp_bin:(position)}) 
                if current_pop_bin not in pop_age_bin_resort:
                    pop_age_bin_resort.update({current_pop_bin:(position)})
                if (current_hosp_bin or current_pop_bin) not in new_age_bins_resort: 
                    new_age_bins_resort.append(current_pop_bin)
                count_hosp += 1
                count_pop += 1
    if hosp_age_bin_resort == {} or pop_age_bin_resort == {} or new_age_bins_resort == []:
        return error_message
    else :
        return  hosp_age_bin_resort, pop_age_bin_resort, new_age_bins_resort

def cases_per_population_by_age(input_data):

    results = {}
    binning_dic_hosp = (covid_data['metadata']['age_binning']['hospitalizations'])
    
    len_binning_dic_hosp  = len(binning_dic_hosp)
    binning_dic_pop = (covid_data['metadata']['age_binning']['population'])
    
       
    (hosp_age_bin_resort, pop_age_bin_resort, new_age_bins_resort)=match_age_bins (binning_dic_hosp,binning_dic_pop)
    
    # set all value to zero
    count_pop = 0
    total_pop_0 = 0
    sum_pop_0 = []
    total_pop_1 = 0
    sum_pop_1 = []
    total_pop_2 = 0
    sum_pop_2 = []
    for key in pop_age_bin_resort:
        if(pop_age_bin_resort[key] == 0):
            pop = (covid_data['region']['population']['age'])
            pop = (pop[count_pop])
            total_pop_0 = total_pop_0 + pop
            sum_pop_0.append(total_pop_0)
        elif(pop_age_bin_resort[key] == 1):
            pop = (covid_data['region']['population']['age'])
            pop = (pop[count_pop])
            total_pop_1 = total_pop_1 + pop
            sum_pop_1.append(total_pop_1)
        elif(pop_age_bin_resort[key] == 2):
            pop = (covid_data['region']['population']['age'])
            pop = (pop[count_pop])
            total_pop_2 = total_pop_2 + pop
            sum_pop_2.append(total_pop_2)
        count_pop = count_pop + 1
    sum_pop_0 = str(sum_pop_0)
 
    count = 0
    total_0 = 0
    list_hosp_0 = []
    total_1 = 0
    list_hosp_1 = []
    total_2 = 0 
    list_hosp_2 = []
    for key in hosp_age_bin_resort:
       
        if(hosp_age_bin_resort[key] == 0): 
            for data,data_dic in covid_data.items():
                for date,date_dic in data_dic.items(): 
                    if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                        for group, group_dic in date_dic.items():
                                if group == 'epidemiology':
                                    for status_cases,status_cases_dic in group_dic.items():
                                        if status_cases == 'confirmed': 
                                            for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                                if catgories_cases == 'new':
                                                    for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                        if band_cases == 'age':
                                                            sum_band = (band_cases_dic[count])
                                                            total_0 = (total_0 + sum_band)
                                                            total_0 = (total_0/total_pop_0)*100
                                                            list_hosp_0.append(total_0)
                                                            
            list_1 = (date,list_hosp_0)
            list_1 = (tuple(list_1))
            results[key] = list_1
        elif(hosp_age_bin_resort[key] == 1): 
            for data,data_dic in covid_data.items():
                for date,date_dic in data_dic.items(): 
                    if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                        for group, group_dic in date_dic.items():
                                if group == 'epidemiology':
                                    for status_cases,status_cases_dic in group_dic.items():
                                        if status_cases == 'confirmed': 
                                            for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                                if catgories_cases == 'new':
                                                    for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                        if band_cases == 'age':
                                                            sum_band = (band_cases_dic[count])
                                                            total_1 = total_1 + sum_band
                                                            total_1 = (total_1/total_pop_1)*100
                                                            list_hosp_1.append(total_1)
            list_2 = (date,list_hosp_1)
            list_2 = (tuple(list_2))
            results[key] = list_2
        elif(hosp_age_bin_resort[key] == 2): 
            
            for data,data_dic in covid_data.items():
                for date,date_dic in data_dic.items(): 
                    if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                        for group, group_dic in date_dic.items():
                                if group == 'epidemiology':
                                    for status_cases,status_cases_dic in group_dic.items():
                                        if status_cases == 'confirmed': 
                                            for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                                if catgories_cases == 'new':
                                                    for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                        if band_cases == 'age':
                                                            sum_band = (band_cases_dic[count])
                                                            total_2 = total_2 + sum_band
                                                            total_2 = (total_2/total_pop_2)*100
                                                            list_hosp_2.append(total_2)
            list_3 = (date,list_hosp_2)
            list_3 = (tuple(list_3))
            results[key] = list_3
           
        else: 
            error_message = 'Error: cannot match age bins'
        count = count + 1 

    
    return results

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
