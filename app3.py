import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
from japanmap import picture

df = pd.read_csv("data/cases_cumulative_daily (1).csv", encoding=("utf - 8"))

date = "2021/7/26"
df_with_date = df[df["Date"] == date]

if df_with_date.empty:
    print("データが見つかりません")
# japanmapが日本語対応していないためリネームする作業をしている？
# 訂正 japanmapがあらかじめ漢字で設定している
else:
    prefecture_name_mapping = {
        "Hokkaido": "北海道",
        "Aomori": "青森県",
        "Iwate": "岩手県",
        "Miyagi": "宮城県",
        "Akita": "秋田県",
        "Yamagata": "山形県",
        "Fukushima": "福島県",
        "Ibaraki": "茨城県",
        "Tochigi": "栃木県",
        "Gunma": "群馬県",
        "Saitama": "埼玉県",
        "Chiba": "千葉県",
        "Tokyo": "東京都",
        "Kanagawa": "神奈川県",
        "Niigata": "新潟県",
        "Toyama": "富山県",
        "Ishikawa": "石川県",
        "Fukui": "福井県",
        "Yamanashi": "山梨県",
        "Nagano": "長野県",
        "Gifu": "岐阜県",
        "Shizuoka": "静岡県",
        "Aichi": "愛知県",
        "Mie": "三重県",
        "Shiga": "滋賀県",
        "Kyoto": "京都府",
        "Osaka": "大阪府",
        "Hyogo": "兵庫県",
        "Nara": "奈良県",
        "Wakayama": "和歌山県",
        "Tottori": "鳥取県",
        "Shimane": "島根県",
        "Okayama": "岡山県",
        "Hiroshima": "広島県",
        "Yamaguchi": "山口県",
        "Tokushima": "徳島県",
        "Kagawa": "香川県",
        "Ehime": "愛媛県",
        "Kochi": "高知県",
        "Fukuoka": "福岡県",
        "Saga": "佐賀県",
        "Nagasaki": "長崎県",
        "Kumamoto": "熊本県",
        "Oita": "大分県",
        "Miyazaki": "宮崎県",
        "Kagoshima": "鹿児島県",
        "Okinawa": "沖縄県",
    }
df_with_date = df_with_date.rename(columns=prefecture_name_mapping)

# newdataでデータとALL列を削除している。 iloc[0]は最初の行を取得するためのコード
new_data = df_with_date.drop(columns=["Date", "ALL"]).iloc[0]

# 都道府県ごとのデータによって対応する色を設定（この時点での感染者数の合計が10000人を超えていた場合、赤色。それ以外は白色、となる）
prefecture_colors = {}
for pref, cases in new_data.items():
    color = "red" if cases > 10000 else "white"
    prefecture_colors[pref] = color

plt.figure(figsize=(10, 10))
# imshow = image show
plt.imshow(picture(prefecture_colors))
# fで変数と一緒に使えるよ
plt.title(f"コロナの累計感染者数が1万人を上回っている県 {date}")
plt.show()
