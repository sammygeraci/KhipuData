from pathlib import Path
from os import listdir
import pandas as pd

import re


def bool_to_bin(b):
    if b:
        return 1
    return 0


dirlist = listdir("C:/Users/sammy/PycharmProjects/KhipuData/khipu/full")

headings = {
    'Cord_Name': [],
    'Twist': [],
    'Attachment': [],
    'Knots': [],
    'Length': [],
    'Termination': [],
    'Thickness': [],
    'Color': [],
    'Value': [],
    'Alt_Value': [],
    'Position': [],
    'Color_Solid': [],
    'Primary_Length': [],
    'Primary_Color': [],
    'Primary_Color_Solid': [],
    'Khipu': []
}

perm_df = pd.DataFrame(headings)

for xlsx in dirlist:
    print(xlsx)
    xlsx_file = Path('khipu', 'full', xlsx)
    df = pd.read_excel(xlsx_file, sheet_name='Cords')
    primary = pd.read_excel(xlsx_file, sheet_name='PrimaryCord')
    primary_length = float(primary.loc[2].at['!-- Primary Cord Data'][7:])
    primary_color = primary.loc[3].at['!-- Primary Cord Data'][6:]
    primary_solid_color = len(primary_color) < 3
    khipu = pd.read_excel(xlsx_file, sheet_name='Khipu').loc[0]
    solid_colors = []
    primary_lengths = []
    primary_colors = []
    primary_solid_colors = []
    khipus = []
    for i in range(len(df)):
        solid_colors.append(bool_to_bin(len(str(df.loc[i].at['Color'])) < 3))
        primary_lengths.append(primary_length)
        primary_colors.append(primary_color)
        primary_solid_colors.append(bool_to_bin(primary_solid_color))
        khipus.append(str(khipu))
    df['Color_Solid'] = solid_colors
    df['Primary_Length'] = primary_lengths
    df['Primary_Color'] = primary_colors
    df['Primary_Color_Solid'] = primary_solid_colors
    df['Khipu'] = khipus
    df = df.drop(columns=['Notes'])
    perm_df = pd.concat([df, perm_df], ignore_index=True)

    knot_count = []
    for ind in perm_df.index:
        k = 0

        value_str = ''
        try:
            value_str = str(int(perm_df['Value'][ind]))
        except ValueError:
            print("value error:")
            print(perm_df['Value'][ind])

        for digit in value_str:
            k += int(digit)

        knot_count.append(k)
        # print("Value: " + str(perm_df['Value'][ind]) + ", count: " + str(k))

perm_df['Knot_Count'] = knot_count
print(perm_df)

perm_df.to_stata('KhipuData.dta')
