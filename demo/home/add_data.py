#from .models import *

import pandas as pd
import os
def fill_data(path):
    y_pred = pd.read_csv(os.path.join(path, "pred.csv"))
    x_test = pd.read_csv(os.path.join(path, "x_test.csv"))
    y_test = pd.read_csv(os.path.join(path, "y_test.csv"))
    


fill_data("../../datasets")