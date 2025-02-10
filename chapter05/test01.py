import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

# 勤務時間と学習時間を乱数で生成しcsv書き出し

dates = pd.date_range(start='2025-02-01', end='2025-02-28').date

rng = np.random.default_rng()
df_work = pd.DataFrame(rng.integers(0, 8, size=28),
                       index=dates,
                       columns=['勤務時間'])

df_study = pd.DataFrame(rng.integers(0, 24, size=28),
                       index=dates,
                       columns=['学習時間'])

df_work.index.name = '日付'
df_study.index.name = '日付'

df_work.to_csv("df_work.csv")
df_study.to_csv("df_study.csv")

# csv読み込み
df_work = pd.read_csv("df_work.csv",
                     index_col='日付',
                     parse_dates=True)
df_study = pd.read_csv("df_study.csv",
                     index_col='日付',
                     parse_dates=True)

today = pd.Timestamp.today().date()

# 取得したい日数
d = 3

days = pd.Timedelta(days=(d - 1))
df_work = df_work.loc[(today - days):today,'勤務時間']
df_study = df_study.loc[(today - days):today, '学習時間']

# グラフ描画
name = 'sakane'
y = [df_work, df_study]
x = range(d)
label = 'time(h)'
fontname = 'MS Gothic'
loc = ['upper left', 'upper right']
title = [f'{name}の直近{len(x)}日間の勤務時間', f'{name}の直近{len(x)}日間の勉強時間']

fig, axes = plt.subplots(ncols=len(y))

for i in range(len(y)):
    axes[i].plot(x, y[i], label=label)
    axes[i].set_title(title[i], fontname=fontname)
    axes[i].legend(loc=loc[i])

plt.show()