# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:31:04 2021

@author: Richards Paul
"""

import pandas as pd

def load_data():
    column_names = ["Name","Origin","Horsepower"]
    
    car_df = pd.DataFrame(columns = column_names)
    
    with open("./cars_input1.txt", "r") as file_car:
        for each_line in file_car:
            currentline = each_line.replace("\n", "").split(",")
            if currentline == column_names:
                continue
            else:
                car_df = car_df.append(
                    {
                        f"{column_names[0]}": currentline[0],
                        f"{column_names[1]}": currentline[1],
                        f"{column_names[2]}": float(currentline[2])
                    }, ignore_index=True)
                   
    return car_df

def return_required_data(df_car, N, O):
    df_1 = df_car[df_car["Origin"] == O]
    print(f"Average Horsepower of cars made in {O}: ", df_1["Horsepower"].mean())
    print(df_1[df_1["Horsepower"] > df_1["Horsepower"].mean()].head(int(N)))



N, O = input("Enter Number N and Origin O: ").split()
print(N, O, type(N), type(O))

df = load_data()

return_required_data(df, N,O)




