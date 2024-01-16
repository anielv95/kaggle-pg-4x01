import functions as f

# import numpy as np
import pandas as pd


def test_base_line():
    input_var = pd.DataFrame(data={"id": [0]})
    assert (
        pd.DataFrame(data={"id": [0], "Exited": [0.5]}) == f.base_line(input_var)
    ).all(axis=None)
    # input_var = pd.DataFrame(data={"col1": [1, 2], "col2": [1, 2]})
    # assert (np.array([4.647, 4.647]) == f.base_line(input_var)).all()
