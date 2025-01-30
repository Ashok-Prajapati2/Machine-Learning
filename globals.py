# globals.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error, 
    median_absolute_error, explained_variance_score, max_error, 
    mean_poisson_deviance, mean_gamma_deviance, classification_report, confusion_matrix
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

print("Global dependencies loaded successfully")
