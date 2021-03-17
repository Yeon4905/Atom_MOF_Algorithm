import pandas as pd
import os
from collections import defaultdict
from tqdm import tqdm

os.chdir('C:\\Users\\HYU\\Desktop\\Lab\\OneDrive - 한양대학교\\해수부\\사고예측\\2020년 BPT\\')
ship_gam = pd.read_csv("선석배정_감만_utf_nan_drop.csv", sep=',', 
                       usecols = ['입항날짜', '입항시간','출항날짜','출항시간','선적','양하'], 
                       encoding = 'ANSI')
ship_shin = pd.read_csv("선석배정_신선대_utf_nan_drop.csv", sep=',', 
                       usecols = ['입항날짜', '입항시간','출항날짜','출항시간','선적','양하'], 
                       encoding = 'ANSI')


def dict_to_dataframe(x, Days):
    """dictionary를 데이터프레임 형식으로 바꿔주는 함수"""
    for i in tqdm(range(len(in_days)), desc = '데이터프레임 변환'):
        Days[i] = pd.DataFrame(x[i])
    return Days

def change_date(df):
    for i in range(len(df)):
        in_day = df.iloc[i]['입항날짜'] -20200000
        in_days[in_day].append(df.iloc[i])
        for j in range(len(in_days)):
            Days[j] = dict_to_dataframe(in_days, Days)
            in_time = Days[j]['입항시간'] // 100
            in_times[in_time].append(Days.iloc[i])
            
if __name__ == "__main__":
    in_times = defaultdict(list)
    in_days = defaultdict(list)
    Days = defaultdict(list)
    change_date(ship_gam)

def dict_to_dataframe(x, Days):
    """dictionary를 데이터프레임 형식으로 바꿔주는 함수"""
    for i in tqdm(range(len(in_days)), desc = '데이터프레임 변환'):
        Days[i] = pd.DataFrame(x[i])
    return Days
    
for i in range(len(ship_gam)):
    in_day = ship_gam.iloc[i]['입항날짜'] -20200000
    in_days[in_day].append(ship_gam.iloc[i])
    for j in range(len(in_days)):
        Days[j] = dict_to_dataframe(in_days, Days)
        in_time = Days[j]['입항시간'] // 100
        in_times[in_time].append(Days.iloc[i])