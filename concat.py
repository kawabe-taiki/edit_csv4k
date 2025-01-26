import pandas as pd
import glob
import os
from datetime import datetime
import datetime
import time
from pathlib import Path

start = time.time()

folders = ["01", "02", "03", "04"]

now = datetime.date.today()
folders = glob.glob(f"./test/*")

# aとbを結合する処理
for f in folders:
    folder_name = Path(f).name
    all_df = pd.DataFrame()
    csv_list = glob.glob(f"{f}/*.csv")
    for path in csv_list:
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
    all_df.to_csv(f"./test/result/result_{str(now)}_{folder_name}.csv", index=False, header=False)

print(f"time:{time.time() - start}")
