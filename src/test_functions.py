import functions as f

# import numpy as np
import pandas as pd


def test_base_line():
    input_var = pd.DataFrame(data={"id": [0]})
    assert (
        pd.DataFrame(
            data={
                "id": [0],
                "Status_C": [0.628084],
                "Status_CL": [0.034788],
                "Status_D": [0.337128],
            }
        )
        == f.base_line(input_var)
    ).all(axis=None)
    # input_var = pd.DataFrame(data={"col1": [1, 2], "col2": [1, 2]})
    # assert (np.array([4.647, 4.647]) == f.base_line(input_var)).all()
