import pandas as pd
import numpy as np
from os import mkdir, path

path_to_raspisanie = "КБиСП 3 курс 1 сем.xlsx"  # !!!Получить название файла
path_to_json_raspisanie = path_to_raspisanie[:-4] + "json"  # Названия файла формата json

pd.set_option("display.max_rows", None, "display.max_columns", None)

group_name = "БСБО-06-18"

if path.exists("table_json") == False:
    mkdir("table_json")

if path.exists("taked_table_json") == False:
    mkdir("taked_table_json")



def convert_to_json_and_take(e, j):
    df = pd.read_excel("excel_file/" + e)  # Считать excel и записать в df
    df.to_json("table_json/" + j, force_ascii=False)  # Записать excel to json

    df = df[:-19]

    key_list = list(df)

    #ЗАМЕНИТЬ NaN
    # unknown = df[key_list[0]][3]
    # print(unknown)
    # for i in range(len(key_list)):
    #     for j in range(len(df.index)):
    #         if df[key_list[i]][j] == unknown:
    #
    #             df[key_list[i]][j] = " "
    #             print(df[key_list[i]][j])

    return df, key_list

groups_list = pd.DataFrame
key_list = []
groups_list, key_list = convert_to_json_and_take(path_to_raspisanie, path_to_json_raspisanie)
def find_group(groups_list, key_list):
    for i in range(0,len(key_list),5):
        if group_name in groups_list[key_list[i]][0]:
            lessons = key_list[i]  # Получить название группы
            lesson_type = key_list[i+1]  # Получить вид занятий
            teachers_names = key_list[i+2]  # Получеть фио перподов
            audience_number = key_list[i+3]  # Получить номер аудитории

            group_list = groups_list[[lessons, lesson_type, teachers_names, audience_number]]  # УСЛОВИЕ Взять расписание группы

            group_list = group_list.drop(group_list.index[[0, 1]])# ДРОПНУТЬ МУСОР

            group_list.to_json("taked_table_json/" + str(groups_list[lessons][0]) + ".json", force_ascii=False)  # Сохранить расписание группы в json

            return group_list
            break


my_group = pd.DataFrame
my_group = find_group(groups_list,key_list)

# print(my_group)
def show_odd_week(g):
    print(g[0:73:2])


# show_odd_week(my_group)


def show_even_week(g):
    print(g[1:74:2])


# show_even_week(group_list)

