import pandas as pd
from pyforbes import ForbesList

def to_dict(data:str) -> dict:
    local_dict = {}
    data_con = data.split(";")
    for i in data_con:
        j = i.split(":")
        local_dict[j[0]] = j[1]
    print(local_dict)

frb_list = ForbesList()

# df = pd.read_csv("fblist.csv")
df = frb_list.get_df()
len = df.firstName.size
scorer = ['Automotive', 'Technology', 'Fashion & Retail', 'Finance & Investments',
          'Diversified', 'Media & Entertainment', 'Telecom', 'Food & Beverage',
          'Logistics', 'Real Estate', 'Metals & Mining', 'Manufacturing',
          'Gambling & Casinos', 'Healthcare', 'Service', 'Energy',
          'Construction & Engineering', 'Sports',]

for i in range(len):
    name = str(df.firstName[i]) + " " + str(df.lastName[i])
    industry = str(df.category[i])
    country = str(df.country[i])
    age = str(df.age[i])
    gender = "Male" if df.gender[i] == "M" else "Female"
    vip_score = 3

    for indus in scorer:
        if indus == industry:
            vip_score += 5


    data = f"name: {name}; industry: {industry}; country: {country}; age: {age}; gender: {gender}; vip_score:{vip_score}"

    to_dict(data)

