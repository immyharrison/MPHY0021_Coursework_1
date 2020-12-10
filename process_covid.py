# FIXME add needed imports
# import json file 
import json
# import to get file path 
import os 

current_filepath = os.getcwd()

# load matplotlib to plot graphs 
import matplotlib.pyplot as plt

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
    # categories that need to be check to see if present in loaded data 
    matches = ["start_data","end_date","region","population","hospitalized", "epidemiology", "weather"]
    catagories_check_counter = 0
    for catagories in matches: 
        if any(catagories in str_input for catagories in matches):
            catagories_check_counter = catagories_check_counter + 1 
                #check if all catagories are present in file - print message is
    if catagories_check_counter == len(matches):
        output = 'correct structure'
    # if not all categories are present print enttor message with that catagorie 
    else:
        output = ('Error: ', catagories, ' not found in the loaded data')
    return output

# 2.2 evolution cases by age group and total pop 
def match_age_bins(binning_dic_hosp,binning_dic_pop):
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
    # sum bins that index to the same in ppulation 
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
    # creat/set variables to empty and zero 
    count = 0
    total_0 = 0
    list_hosp_0 = []
    total_1 = 0
    list_hosp_1 = []
    total_2 = 0 
    list_hosp_2 = []
    for key in hosp_age_bin_resort:
       # index hosp sum together
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
        # reutn list of data                                              
            list_1 = (date,list_hosp_0)
            # make list tuple
            list_1 = (tuple(list_1))
            # add age bins 
            results[key] = list_1
         # index hosp sum together
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
            #make list 
            list_2 = (date,list_hosp_1)
            # make tuple 
            list_2 = (tuple(list_2))
            # add age bin
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
            #make list of date and summed data
            list_3 = (date,list_hosp_2)
            # make list tuple
            list_3 = (tuple(list_3))
            # add age bin to list 
            results[key] = list_3
         # error message if not possible  
        else: 
            error_message = 'Error: cannot match age bins'
        count = count + 1 

    
    return results


#2.3 new hosp and new cases 
def hospital_vs_confirmed(input_data):
    # create empty variables 
    list_date = []
    list_ratio = []
    list_results = []
    no_new_cases = [] 
    no_new_hosp = []
    len_age_bin = len(covid_data['metadata']['age_binning']['hospitalizations'])
    # find data about confirded case s
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
                                                if band_cases == 'all':
                                                    print(band_cases_dic)
                                                    if band_cases_dic == None:
                                                        no_new_cases = band_cases_dic
                                                    else: 
                                                        result = ('error: missing data')
                    # find data about hospitalised  
                        elif group == 'hospitalizations':
                            for status_cases_hosp,status_cases_hosp_dic in group_dic.items():
                                if status_cases_hosp == 'hospitalized': 
                                    for catgories_cases_hosp,catgories_cases_hosp_dic in status_cases_hosp_dic.items():
                                        if catgories_cases_hosp == 'new':
                                       
                                            for band_cases_hosp,band_cases_hosp_dic in catgories_cases_hosp_dic.items():
                                                if band_cases_hosp == 'all':
                                                    print(band_cases_hosp_dic)
                                                
                                                    if band_cases_hosp_dic == None:
                                                        no_new_hosp = band_cases_hosp_dic
                                                    else: 
                                                        result = ('error: missing data')
    # if not missing data find ration
    if no_new_cases != [] or no_new_hosp != []:
        ratio = no_new_cases/no_new_hosp
        list_ratio.append(ratio)
        list_date.append(date)
        list_results = list_date + list_ratio
        result = tuple(list_results)
    return (results)

#2.4 prepare for ploting 
def generate_data_plot_confirmed(input_data, sex, max_age, status):
    #create empty variables 
    graph_data = []
    graph_date = []
    colour = ''
    # error message if no input for sex or max age
    if  sex == ''  and (max_age == '' or max_age == False):  
        error_message = ('Error: need input for either sex or max_age')
    
    #error if input for both age and max age
    if sex != True or sex != False or sex == '':
        error_message = 'Error in input value for sex'
    
    elif sex == False and  max_age == False :
        error_message = ('Error: can only have input  from at most one of sex or max_age allowed at a time ')
    # if only input female
    elif sex == 'female' and max_age == '':
        colour = 'indigo'
        # set status to defal to total if empty 
        if status == '':
            status = 'total'
        # find the number of confirmed cases for female
        for data,data_dic in covid_data.items():
            for date,date_dic in data_dic.items(): 
                if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                    graph_date.append(date)
                    for group, group_dic in date_dic.items():
                            if group == 'epidemiology':
                                for status_cases,status_cases_dic in group_dic.items():
                                    if status_cases == 'confirmed': 
                                        for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                            if catgories_cases == status:
                                                for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                    if band_cases == 'female':
                                                       graph_data.append(band_cases_dic)
 
    # find the number of confirmed cases for male
    elif sex == 'male' and max_age == '' or max_age == False:
        colour = 'green'
         # set status to defal to total if empty 
        if status == '':
            status = 'total'
        for data,data_dic in covid_data.items():
            for date,date_dic in data_dic.items(): 
                if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                    graph_date.append(date)
                    for group, group_dic in date_dic.items():
                        if group == 'epidemiology':
                            for status_cases,status_cases_dic in group_dic.items():
                                if status_cases == 'confirmed': 
                                    for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                        if catgories_cases == status:
                                            for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                if band_cases == 'male':
                                                    graph_data.append(band_cases_dic)
                                                           
    # find for max age 
    elif max_age != '' and sex == '' or sex == False:
         # set status to defal to total if empty 
        if status == '':
            status = 'total'
        # find age bins 
        hosp_age_bin = (covid_data['metadata']['age_binning']['hospitalizations'])
        counter = 0
        # for each age in max age 
        if max_age <= 25 :
            colour = 'green'
        elif max_age <= 50 :
            colour = 'orange'
        elif max_age <= 75:
            colour = 'indigo'
        else:
            colour = 'pink'
            # check against each age bin
        for age_bin in hosp_age_bin:
                counter = counter + 1 
                split = age_bin.split('-')
                # find upper and lower limit of age bin
                limit_upper_age_bin = (age_bin.partition('-')[2])
                limit_lower_age_bin = (age_bin.partition('-')[0])
                # turn limit to integer number
                if  limit_lower_age_bin != '':
                    limit_lower_age_bin = int(limit_lower_age_bin)
                    if limit_upper_age_bin != '' :
                        limit_upper_age_bin= int(limit_upper_age_bin)
                #upper limit not defined so define as 100 max age 
                    elif limit_upper_age_bin == '':
                        limit_upper_age_bin = int(100)
                # if age within age bin 
                if max_age <= limit_upper_age_bin and max_age >= limit_lower_age_bin:
                    # find age confirm cases for each day 
                    for data,data_dic in covid_data.items():
                        for date,date_dic in data_dic.items(): 
                            if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                                graph_date.append(date)
                                for group, group_dic in date_dic.items():
                                        if group == 'epidemiology':
                                            for status_cases,status_cases_dic in group_dic.items():
                                                if status_cases == 'confirmed': 
                                                    for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                                        if catgories_cases == status:
                                                            for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                                if band_cases == 'age':
                                                                    age_below = band_cases_dic[0:counter]
                                                                    sum_age_below_max = sum(age_below)
                                                                    graph_data.append(sum_age_below_max)
   
    return graph_data, graph_date, colour, error_message 

def create_confirmed_plot(input_data, sex=False, max_ages=[], status=..., save=...):
     # FIXME check that only sex or age is specified.
    if sex == False and max_ages == False:  
        print ('Error: need input for either sex or max_age, cannot input both at once')
    fig = plt.figure(figsize=(10, 10)) 
    # FIXME change logic so this runs only when the sex plot is required
    if sex != True or sex != False : 
      print('Error in input value for sex')
    if sex == True and (max_ages == False or max_ages == ''):
        for sex in ['male', 'female']:
            # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
            (graph_data, graph_date, colour) = generate_data_plot_confirmed(input_data,sex,max_ages,status)
            plt.plot( graph_date, graph_data, colour, label = (status + ' ' +  sex))
    # FIXME change logic so this runs only when the age plot is required
    elif max_ages != '' and sex == False or sex == '':
        for age in max_ages:
            str_age = str(age)
            if str_age.isdigit():
        # FIXME need to change `changeme` so it uses generate_data_plot_confirmed
                (graph_data, graph_date, colour) = generate_data_plot_confirmed(input_data,sex,age,status)
                plt.plot(graph_date, graph_data, colour, label = (status + ' younger than ' + str_age))
            else: 
               print ('Error: max_age input not digits')
    fig.autofmt_xdate()  # To show dates nicely
    # TODO add title with "Confirmed cases in ..."
    region_name = (input_data['region']['name'])
    plt.title('Confirmed cases in '+ region_name )
    # TODO Add x label to inform they are dates
    plt.xlabel('date')
    # TODO Add y label to inform they are number of cases
    plt.ylabel('# cases')
    # TODO Add legend
    plt.legend(loc=2, ncol=1)
    # TODO Change logic to show or save it into a '{region_name}_evolution_cases_{type}.png'
    #      where type may be sex or age
    if save == True: 
        region_name = (covid_data['region']['name'])
        if sex == True: 
            types = 'sex'
        else:
            types = 'max_ages'

        plt.savefig(region_name+'_evolution_cases_'+types+'.png', dpi=300, bbox_inches='tight')
    else:
        plt.show()

# 2.5 the effect of the weather 
def compute_running_average(data, window):
    # create variables 
    no_in_input = len(data) -1
    position_in_list = 0 
    output = []
    data_no_none = []
    n = position_in_list
    # for the number getting averaged 
    for num in data: 
        # if first number of cannot average over window size
        if n == 0 or n == no_in_input or n <int(window/2) or n > no_in_input - int(window/2):
            n += 1 
            output.append(None)
        else:
            # position of lower window limit
            min = n-int(window/2)
            # position of higher window limit
            max = n+int(window/2)
            # average over window 
            average_list = (data[min:max+1])
            # set variable to count sum 
            sum_num = 0
            # count number of non zer  numbrs in list 
            no_non_0_list = 0
            # add numbers in list 
            for t in average_list:
                # no count number if zero 
                if t == None :
                    continue
                else:
                    sum_num = sum_num + t 
                    no_non_0_list += 1
            n += 1
            # average over number in list
            if no_non_0_list >0:    
                average = sum_num/no_non_0_list
                output.append(average) 
            
              

    return output

def simple_derivative(data):
     # results start with None as coont have derivative of first value 
    # set /create variables 
    results = []
    position_in_list = 0
    # for number being calculated 
    for i in data:
        n = position_in_list  
        # if first number in list results is none
        if n == 0:
            results.append(None)

        elif n < len(data) and n> 0:
            # find vlaue of today and yesterday
            yesterday = data[n-1]
            today = data[n]
            
            # if none in string 
            # if none of the inputs is none append none
            if yesterday == None or today == None:
                results.append(None)

            # if no none find difference 
            else : 
                num1 = (data[n-1])
                num2 = (data[n])
                diff = num2 - num1
                results.append(diff)


        position_in_list += 1
    return results

def count_high_rain_low_tests_days(input_data):
    find the rainfall for each day 
    # set empty variables 
    list_rain = []
    list_test = []
    #find rainfall of each day
    for data,data_dic in covid_data.items():
                        for date,date_dic in data_dic.items(): 
                            if date[0:4].isdigit() and date[5:6].isdigit() and date[8:10]:
                                for group, group_dic in date_dic.items():
                                        if group == 'weather':
                                            for status_cases,status_cases_dic in group_dic.items():
                                                if status_cases == 'rainfall': 
                                                    #print('rain', status_cases_dic)
                                                    list_rain.append(status_cases_dic)

    # find the no. test for each day 
                                        if group == 'epidemiology':
                                            for status_cases,status_cases_dic in group_dic.items():
                                                if status_cases == 'tested': 
                                                    for catgories_cases,catgories_cases_dic in status_cases_dic.items():
                                                        if catgories_cases == 'new':
                                                            for band_cases,band_cases_dic in catgories_cases_dic.items():
                                                                if band_cases == 'all':
                                                                    list_test.append(band_cases_dic)
                                                                   

       
    # use compute_running_average to smooth data over one week ( 7 days)
    smooth_rain = compute_running_average(list_rain,7)
    smooth_test = compute_running_average(list_test,7)

    # use simple_derivative to fifnd if no of test and rain increased or decreased 
    simple_derivative_rain = simple_derivative(smooth_rain)
    simple_derivative_test = simple_derivative(smooth_test)
    #set variables to zero 
    increase_rain_count = 0
    decrease_test_increase_rain_count = 0
    # for rain and test data 
    for rain_days in simple_derivative_rain:
        for test_days in simple_derivative_test:
            
            if rain_days == None:
                rain_days = float(0.0)
            if test_days == None:
                test_days = float(0.0)
            # if increase in rain
            if rain_days > 0.0:
                increase_rain_count = increase_rain_count + 1 
                # if decrease in test add to count 
                if  test_days < 0: 
                    decrease_test_increase_rain_count = decrease_test_increase_rain_count + 1
    ratio = decrease_test_increase_rain_count/increase_rain_count
    
    return ratio                                                  
    #raise NotImplementedError
