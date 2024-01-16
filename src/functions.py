import pandas as pd

# import numpy as np


def base_line(df: pd.DataFrame):
    pred = df.copy()
    pred["Exited"] = 0.5
    return pred[["id", "Exited"]]


# def getting_csv(prediction):
#     df = pd.DataFrame(data={"Hardness":prediction})
#     df["id"] = df.index
