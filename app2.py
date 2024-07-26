# 今回は多種類のグラフを複合したグラフを製作する
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding="utf-8")

# dfにCumulative_Iwateを作り、それはdfのIwateの列と同じ？
# 累計感染者数の計算

df["Cumulative_Iwate"] = df["Iwate"].diff().fillna(0)
# df["Cumulative_Iwate"] = df["Iwate"].cumsum()

df["Date"] = pd.to_datetime(df["Date"])

# df_iwateは、dfのDateとIwateの情報を持つよってこと？
# Iwate のデータだけ抜き出している
df_iwate = df[["Date", "Iwate"]]

# fig = figure
# 2つの軸を持つグラフエリアを作成
fig, ax1 = plt.subplots(figsize=(10, 5))

# 1つ目のグラフを設定する（棒グラフ）
ax1.bar(df_iwate["Date"], df_iwate["Iwate"], color="b", label="岩手の累計感染者数")

# x軸を共有するよ的な
ax2 = ax1.twinx()
# ２つ目のグラフを設定する
ax2.plot(df["Date"], df["Cumulative_Iwate"], label=" 岩手の1日あたりの感染者数", color="r")


ax1.set_ylabel("岩手の累計感染者数")
ax2.set_ylabel("岩手の1日あたりの感染者数")

ax1.set_xlabel("日付")
ax1.set_title("岩手県の累計感染者数と1日あたりの感染者数")


fig.tight_layout
# loc = location
fig.legend(loc="upper left")
plt.show()
