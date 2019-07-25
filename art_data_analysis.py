#libraries
import tate
import matplotlib.pyplot as plt

#loading data file
artwork_db = tate.get_artwork()

#which medium do genders prefer
#functions

def count(list):
    x_list = []
    dict = {}
    for x in list:
        if x not in x_list:
            x_list.append(x)
    for x in x_list:
        dict[x] = list.count(x)
    return dict

def percent(numbers , list):
    perc_list = []
    for x in range(len(numbers)):
        percent_a = numbers[x] /len(list)
        percent_b = percent_a * 100
        perc_list.append(percent_b)
    return perc_list

def max_nums(dict):
    largest_num = []
    most = max(dict.values())

    # iterate through the dictionary
    max2 = 0
    for v in dict.values():
        if(v>=max2 and v<most):
                max2 = v
    max3 = 0
    for v in dict.values():
        if(v>=max3 and v<max2):
                max3 = v
    max4 = 0
    for v in dict.values():
        if(v>=max4 and v<max3):
                max4 = v
    max5 = 0
    for v in dict.values():
        if(v>=max5 and v<max4):
                max5 = v
    largest_num.append(most)
    largest_num.append(max2)
    largest_num.append(max3)
    largest_num.append(max4)
    largest_num.append(max5)
    return largest_num

def other_nums(dict,largest_num):
    other_nums = []

    for v in dict:
        if v not in largest_num:
            other_nums.append(dict[v])
    return other_nums

def max_names(largest_nums , dict):
    names = []
    for x in dict:
        if dict[x] in largest_nums:
            names.append(x)
    return names

def pie_chart(file_name , count , colors):

    largest_num = max_nums(count)
    largest_name = max_names(largest_num, count)

    other_num = other_nums(count , largest_num)


    other_perc = percent(other_num, count)
    other = sum(other_perc)
    largest_perc = percent(largest_num, count)

    #graphing pie chart

    labels = largest_name
    labels.append("other")

    data = largest_perc
    data.append(other)
    
    plt.figure(file_name)
    plt.pie( data , labels=labels, colors=colors, startangle=90, autopct='%.1f%%')
    plt.suptitle("Mediums Prefered By " + file_name)
    plt.savefig(file_name + '.png')

#lists
male = []
female = []
na = []

#getting data and putting them in lists
for x in artwork_db:
    art = x['artist']
    gender = art['gender']
    data = x['data']
    medium = data['medium']
    if gender == "Male":
        male.append(medium)
    elif gender == "Female":
        female.append(medium)
    else:
        na.append(medium)

#getting dictionaries of the counts
male_count = count(male)
female_count = count(female)
na_count = count(na)


#MALE PERCENT AND GRAPH =================================================

#largest_num_m = max_nums(male_count)
#largets_name_m = max_names(largest_num_m , male_count)

#other_num_m = other_nums(male_count , largest_num_m)


#other_perc_m = percent(other_num_m , male_count)
#other_m = sum(other_perc_m)
#largest_perc_m = percent(largest_num_m,male_count)

#graphing pie chart

#labels_m = largets_name_m
#labels_m.append("other")

#data_m = largest_perc_m
#data_m.append(other_m)

colors_m = ["deepskyblue",'dodgerblue','royalblue','blue']
#plt.pie( data_m , labels=labels_m, colors=colors_m, startangle=90, autopct='%.1f%%')
#plt.suptitle("Mediums Prefered By Males")
#plt.savefig('male.png')

pie_chart('male' , male_count , colors_m)

#FEMALE PERCENT AND GRAPH ============================================================

#largest_num_f = max_nums(female_count)
#largets_name_f = max_names(largest_num_f, female_count)

#other_num_f = other_nums(female_count , largest_num_f)


#other_perc_f = percent(other_num_f, female_count)
#other_f = sum(other_perc_f)
#largest_perc_f = percent(largest_num_f, female_count)

#graphing pie chart

#labels_f = largets_name_f
#labels_f.append("other")

#data_f = largest_perc_f
#data_f.append(other_f)


colors_f = ["hotpink",'deeppink','mediumvioletred','darkmagenta']
#plt.pie( data_f , labels=labels_f, colors=colors_f, startangle=90, autopct='%.1f%%')
#plt.suptitle("Mediums Prefered By Females")
#plt.savefig('female.png')

pie_chart('female' , female_count , colors_f)

#NA PERCENT AND GRAPH ============================================================
#na is being weird

#largest_num_na = max_nums(na_count)
#largets_name_na = max_names(largest_num_na, na_count)

#other_num_na = other_nums(na_count , largest_num_na)


#other_perc_na = percent(other_num_na, na_count)
#other_na = sum(other_perc_na)
#largest_perc_na = percent(largest_num_na, na_count)

#graphing pie chart

#labels_na = largets_name_na
#labels_na.append("other")

#data_na = largest_perc_na
#data_na.append(other_na)


#colors_na = ["salmon",'tomato','orangered','red']
#plt.pie( data_f , labels=labels_f, colors=colors_na, startangle=90, autopct='%.1f%%')
#plt.suptitle("Mediums Prefered By Unknowns")
#plt.savefig('na.png')

#pie_chart('unknown' , na_count , colors_na)
