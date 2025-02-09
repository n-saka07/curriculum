import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

x, y = range(3), [[8, 10, 9],[3, 1, 2]]

label = 'time(h)'
fontname = 'MS Gothic' # Windows
# fontname = 'IPAexGothic' # mac(インストール必要)
loc = ['upper left', 'upper right']
title = ['「あなた」の直近３日間の勤務時間', '「あなた」の直近３日間の勉強時間']

fig, axes = plt.subplots(ncols=2)

for i in range(2):
    axes[i].plot(x, y[i], label=label)
    axes[i].set_title(title[i], fontname=fontname)
    axes[i].legend(loc=loc[i])

plt.show()