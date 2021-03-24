import pandas as pd
import os
from collections import defaultdict
from tqdm import tqdm
from functools import partial  # tqdm progressbar 오류 잡아주는 코드
tqdm = partial(tqdm, position = 0, leave = True )


df_dir = 'C:\\Users\\HYU\\Desktop\\Lab\\OneDrive - 한양대학교\\해수부\\사고예측\\2020년 BPT\\'
os.chdir(df_dir)
ship_gam = pd.read_csv("선석배정_감만_utf_nan_drop.csv", sep=',',
                       usecols = ['입항날짜', '입항시간','출항날짜','출항시간','선적','양하'],
                       encoding = 'ANSI')
ship_shin = pd.read_csv("선석배정_신선대_utf_nan_drop.csv", sep=',',
                       usecols = ['입항날짜', '입항시간','출항날짜','출항시간','선적','양하'],
                       encoding = 'ANSI')


# def dict_to_dataframe(x, Days):
#     """dictionary를 데이터프레임 형식으로 바꿔주는 함수"""
#     for i in tqdm(range(len(in_days)), desc = '데이터프레임 변환'):
#         Days[i] = pd.DataFrame(x[i])
#     return Days

# def change_date(df):
#     for i in range(len(df)):
#         in_day = df.iloc[i]['입항날짜'] -20200000
#         in_days[in_day].append(df.iloc[i])
#         for j in range(len(in_days)):
#             Days[j] = dict_to_dataframe(in_days, Days)
#             in_time = Days[j]['입항시간'] // 100
#             in_times[i][in_time].append(Days.iloc[i])

def dict_to_dataframe(x, Days):
    """dictionary를 데이터프레임 형식으로 바꿔주는 함수"""
    for i in range(in_day):
        if not x[i]:
            continue
        else:
            Days[i] = pd.DataFrame(x[i])
    return Days
def search_date_time(in_day, in_days, times):
    for i in range(len(in_days)):
        for j in range(len(in_days[i])):
            in_day_time = in_days[in_day][j]
            time = in_days[in_day][j][1] // 100
            print(time)
            print(in_day_time)
            times[i][time].append(in_day_time)
    return times[i]

# def time_factor(*x):
#     for i in range(len(times[i])):
#         if time < 100:
#             times[i][i].append(in_day_time)
#         elif time < 200:
#             times[i][i].append(in_day_time)
#         elif time < 3

def search_time(k, In, haul):
    if In < 100:
        times[k][0] += haul
    elif In < 200:
        times[k][1] += haul
    elif In < 300:
        times[k][2] += haul
    elif In < 400:
        times[k][3] += haul
    elif In < 500:
        times[k][4] += haul
    elif In < 600:
        times[k][5] += haul
    elif In < 700:
        times[k][6] += haul
    elif In < 800:
        times[k][7] += haul
    elif In < 900:
        times[k][8] += haul
    elif In < 1000:
        times[k][9] += haul
    elif In < 1100:
        times[k][10] += haul
    elif In < 1200:
        times[k][11] += haul
    elif In < 1300:
        times[k][12] += haul
    elif In < 1400:
        times[k][13] += haul
    elif In < 1500:
        times[k][14] += haul
    elif In < 1600:
        times[k][15] += haul
    elif In < 1700:
        times[k][16] += haul
    elif In < 1800:
        times[k][17] += haul
    elif In < 1900:
        times[k][18] += haul
    elif In < 2000:
        times[k][19] += haul
    elif In < 2100:
        times[k][20] += haul
    elif In < 2200:
        times[k][21] += haul
    elif In < 2300:
        times[k][22] += haul
    elif In < 2400:
        times[k][23] += haul
    return times[k], times


if __name__ == "__main__":
    in_times_shin = defaultdict(list)
    in_days_shin = defaultdict(list)
    Days_shin = ['D' + str(i) for i in range(1, 1233)]

    in_times_gam = defaultdict(list)
    in_days_gam = defaultdict(list)
    Days_gam = ['D' + str(i) for i in range(1, 1233)]

    # Days = defaultdict(DataFrame)
    # change_date(ship_gam)
    Days = [[] for _ in range(1, 1233)]
    # times = [[0 for _ in range(0, 2400, 100)] for _ in range(len(Days[k]))]


    for i in tqdm(range(len(ship_gam))):
        in_gam = ship_gam.iloc[i]
        in_date_ = ship_gam.iloc[i]['입항날짜']
        in_day = ship_gam.iloc[i]['입항날짜'] -20200000
        in_days_gam[in_day].append(ship_gam.iloc[i])
        # times[i] = search_date_time(in_day, in_days, times[i])
        # In_days = pd.DataFrame([[k] + j for k,v in in_days.items() for j in v], columns = ['입항날짜', '입항시간','양하'])
        # Days_gam[in_day] = pd.DataFrame(in_days_gam[in_day])
        # dict_to_dataframe(in_days_gam, Days_gam)

    for j in tqdm(range(len(ship_shin))):
        in_shin = ship_shin.iloc[j]
        in_date = ship_shin.iloc[j]['입항날짜']
        in_day = ship_shin.iloc[j]['입항날짜'] -20200000
        in_days_gam[in_day].append(ship_shin.iloc[j])
        # Days_shin[in_day] = pd.DataFrame(in_days_shin[in_day])
    dict_to_dataframe(in_days_gam, Days)

    for k in tqdm(range(len(in_days_gam))):
        # times = [[0 for _ in range( for _ in range(1, 1233)]
        # Times = [0 for _ in range(1, 1233)]
        # haul = [[[] for _ in range(0, 2400, 100)] for _ in range(1, 1233)]
        # In = [[[] for _ in range(0, 2400, 100)] for _ in range(1, 1233)]
        for l in range(len(Days[k])):
            times = [[0 for _ in range(0, 2400, 100)] for _ in range(1, 1233)]
            Times = [[0 for _ in range(0, 2400, 100)] for _ in range(1, 1233)]
            haul = Days[k].iloc[l][4]
            In = Days[k].iloc[l][1]

            if In < 100:
                times[k][0] += haul
            elif In < 200:
                times[k][1] += haul
            elif In < 300:
                times[k][2] += haul
            elif In < 400:
                times[k][3] += haul
            elif In < 500:
                times[k][4] += haul
            elif In < 600:
                times[k][5] += haul
            elif In < 700:
                times[k][6] += haul
            elif In < 800:
                times[k][7] += haul
            elif In < 900:
                times[k][8] += haul
            elif In < 1000:
                times[k][9] += haul
            elif In < 1100:
                times[k][10] += haul
            elif In < 1200:
                times[k][11] += haul
            elif In < 1300:
                times[k][12] += haul
            elif In < 1400:
                times[k][13] += haul
            elif In < 1500:
                times[k][14] += haul
            elif In < 1600:
                times[k][15] += haul
            elif In < 1700:
                times[k][16] += haul
            elif In < 1800:
                times[k][17] += haul
            elif In < 1900:
                times[k][18] += haul
            elif In < 2000:
                times[k][19] += haul
            elif In < 2100:
                times[k][20] += haul
            elif In < 2200:
                times[k][21] += haul
            elif In < 2300:
                times[k][22] += haul
            elif In < 2400:
                times[k][23] += haul

            print("time-" + str(k) +":", times[k])
            # times[k] = (search_time(k, In, haul))
            # print("time-" + str(k) +":", times[k])
            # Times[k] = pd.DataFrame(times[k])
            # Times[k].to_csv(df_dir + "양하\\양하" + str(k) + ".csv")
            # Days['sum_haul'] = times[i]
    # for k in tqdm(range(1, 1233)):
    #     if not Days_gam[k] or Days_shin[k]:
    #         continue
    #     else:
    #         pd.merge([Days_gam, Days_shin])
    #     # Days_gam[in_day].to_csv(df_dir + "감만_new\\선석배정_감만" + str(in_day) + ".csv", columns = ['입항날짜', '입항시간', '양하'], index = False, encoding = 'ANSI')

# print(in_days[101])
    # for j in range(len(in_days)):
    #     Days[j] = dict_to_dataframe(in_days, Days)
        # in_time = Days[j]['입항시간'] // 100
        # in_times[i][in_time].append(Days.iloc[i])
