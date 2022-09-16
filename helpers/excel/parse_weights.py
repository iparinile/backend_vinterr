from math import isnan

import pandas


def parse_weights(excel_file_path: str) -> dict:
    excel_data_df = pandas.read_excel(excel_file_path)

    data_dict = excel_data_df.to_dict()

    dict_1c_articles = data_dict['КодАртикул']
    dict_values = data_dict['Вес']

    remains_dict = dict()

    for row_number in range(len(dict_1c_articles)):
        if row_number != 0:
            article = dict_1c_articles[row_number]
            weight = dict_values[row_number]

            if isnan(weight):
                weight = None

            remains_dict[article] = weight

    return remains_dict
