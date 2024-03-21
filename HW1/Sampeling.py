import hashlib
import os
from datetime import datetime as dt

import pandas as pd

df: pd.core.frame.DataFrame = pd.read_csv(r"F:\AI_IUST\HW1\Doc\onlinefraud.csv")


# fraction is the ratio of samples/data
def random_sample(df: pd.core.frame.DataFrame, fraction: float):
    sample_df = df.sample(frac=fraction)
    hash_object = hashlib.sha256(dt.now().strftime("%Y-%m-%d %H:%M:%S").encode())
    file_name = hash_object.hexdigest()[:8]
    file_name = "RANDOM_SAMPLE_ " + file_name
    os.mkdir(f"F:\AI_IUST\Samples\{file_name}")
    sample_df.to_csv(f"F:\AI_IUST\Samples\{file_name}\TRAIN.csv", index=False)
    remaining_df = df.drop(sample_df.index)
    remaining_df.to_csv(f"F:\AI_IUST\Samples\{file_name}\TEST.csv", index=False)
