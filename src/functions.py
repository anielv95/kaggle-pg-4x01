import pandas as pd

# import numpy as np


def base_line(df: pd.DataFrame):
    pred = df.copy()
    pred[["Status_C", "Status_CL", "Status_D"]] = [0.628084, 0.034788, 0.337128]
    return pred[["id", "Status_C", "Status_CL", "Status_D"]]


# def getting_csv(prediction):
#     df = pd.DataFrame(data={"Hardness":prediction})
#     df["id"] = df.index
