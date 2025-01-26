import pandas as pd
import glob
import os
from datetime import datetime
import datetime
import time
from pathlib import Path

start = time.time()

pair = {"01":"02", "03":"04"}

now = datetime.date.today()
folder = "./test/result"

# aとbを結合する処理

all_df = pd.DataFrame()
csv_list = glob.glob(f"{folder}/*.csv")
for path in csv_list:
    filename = Path(path).name
    filename = filename.replace(".csv","")
    s = filename.split("_")
    end = s[-1]
    # if  in pair.keys()
    df_a = pd.read_csv(path, header=None)
    df_a.insert(0, "new", df_a.iloc[0, 0])
    df_a["concat"] = df_a["new"].copy()
    for column_name in df_a.columns.values:
        if column_name != "new":
            df_a["concat"] += df_a[column_name].astype(str)
        # df_a["concat"] = df_a["new"] + df_a[0].astype(str) + df_a[1].astype(str) + df_a[2].astype(str)
    df_a = df_a.drop(0)
    df_a = df_a.replace({4:{':':''}},  regex=True)
    all_df = pd.concat([all_df, df_a])

    all_df = all_df[all_df[4] != "No list."]

os.makedirs("./test/result", exist_ok=True)
all_df.to_csv(f"./test/result/result_{str(now)}_{filename}.csv", index=False, header=False)

print(f"time:{time.time() - start}")
