from math import isnan

import pandas


def parse_remains(excel_file_path: str) -> dict:
    excel_data_df = pandas.read_excel(excel_file_path)

    data_dict = excel_data_df.to_dict()

    dict_1c_ids = data_dict['Характеристика.Код']
    dict_values = data_dict['Итого по всем складам']

    remains_dict = dict()

    for row_number in range(len(dict_1c_ids)):
        if row_number != 0:
            id_1c = dict_1c_ids[row_number]
            amount = dict_values[row_number]

            if id_1c != 'Итого':

                if isnan(amount):
                    amount = 0

                remains_dict[id_1c] = amount

    return remains_dict


if __name__ == '__main__':
    print(parse_remains("ОстаткиАктуальные.xlsx"))
