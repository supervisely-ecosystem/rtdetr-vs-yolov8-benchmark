import pandas as pd
import os
from checkpoints import checkpoints

input_dir = "benchmark"
model_names = list(checkpoints.keys())


resolution = "x640"
files = sorted([f for f in os.listdir(input_dir) if f.endswith(f"{resolution}.csv")])
dfs = []
for file in files:
    df = pd.read_csv(f"{input_dir}/{file}", index_col=0)
    dfs.append(df)

# join all dfs
df = pd.concat(dfs)
df.index = model_names
df.index.name = "Model"
df.reset_index(inplace=True)
df.to_csv(f"{input_dir}/speed_test_{resolution}_rtdetr.csv")
print(f"RT-DETR {resolution} speed test:")
print(df)


resolution = "x1280"
files = sorted([f for f in os.listdir(input_dir) if f.endswith(f"{resolution}.csv")])
dfs = []
for file in files:
    df = pd.read_csv(f"{input_dir}/{file}", index_col=0)
    dfs.append(df)

# join all dfs
df = pd.concat(dfs)
df.index = model_names
df.index.name = "Model"
df.reset_index(inplace=True)
df.to_csv(f"{input_dir}/speed_test_{resolution}_rtdetr.csv")
print(f"RT-DETR {resolution} speed test:")
print(df)