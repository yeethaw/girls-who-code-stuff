#libraries
import tate
import matplotlib.pyplot as plt

#loading data file
artwork_db = tate.get_artwork()

#which medium do genders prefer
male = []
female = []
na = []

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
