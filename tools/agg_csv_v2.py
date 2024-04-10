import re
import os
import pandas as pd

input_dir = "."

model_names = {
    "rtdetr_r18vd": "R18",
    "rtdetr_r34vd": "R34",
    "rtdetr_r50vd_m": "R50-m",
    "rtdetr_r50vd": "R50",
    "rtdetr_r101vd": "R101",
}

files = sorted([f for f in os.listdir(input_dir) if f.endswith(f"yml.csv")])
dfs: list = [None] * len(model_names)
for file in files:
    df = pd.read_csv(f"{input_dir}/{file}", index_col=0)
    name_raw = str(re.findall(r"(rtdetr_r\d+vd(_m)?)_6x", file)[0][0])
    name = model_names[name_raw]
    df.index = [name]
    idx = int(list(model_names.keys()).index(name_raw))
    dfs[idx] = df

# join all dfs
df = pd.concat(dfs)
# df.index = model_names
df.index.name = "Model"
df.reset_index(inplace=True)
df.to_csv(f"{input_dir}/agg.csv")
# print(f"RT-DETR {resolution} speed test:")
print(df)
