from itertools import cycle
import os
from serve import RTDETR
import torch
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument("--model_idx", type=int, default=0)
argparser.add_argument("--resolution", type=int, default=1280)
argparser.add_argument("--n", type=int, default=100)
args = argparser.parse_args()
print(args)

device = "cuda"
assert torch.cuda.is_available(), "CUDA is not available"


resolution_int = args.resolution
resolution = f"x{resolution_int}"
images = os.listdir(f"benchmark/{resolution}")
image_generator = cycle(images)

m = RTDETR(
    model_dir="models",
    use_gui=True,
    custom_inference_settings={
        "confidence_thresh": 0.05
    },
)
settings = {"confidence_thresh": 0.05}

model_idx = args.model_idx
m.gui._models_table.select_row(model_idx)
m.load_on_device(m.model_dir, device, imgsz=resolution_int)

# warmup 3 times
for img in images[:3]:
    image_path = f"benchmark/{resolution}/{img}"
    m.predict(image_path, settings=settings)

speed_tests = []
for i in range(args.n):
    image_path = f"benchmark/{resolution}/{next(image_generator)}"
    m.predict(image_path, settings=settings)
    speed_tests.append(m.speed_test)


# average tests
import pandas as pd
df = pd.DataFrame(speed_tests)
avg_df = df.mean().to_frame().T
std_df = df.std().to_frame().T
std_df.columns = [f"{col}_std" for col in std_df.columns]
df = pd.concat([avg_df, std_df], axis=1)
df.to_csv(f"benchmark/speed_test_{model_idx}_{resolution}.csv")

print(f"Average speed test (N={args.n}):")
print(avg_df)
print("Std speed test:")
print(std_df)
