# Time : 
# @Author : Vic
# @File : 
# @desc:
import numpy as np
import pandas as pd
import warnings

from sklearn.ensemble import  AdaBoostRegressor, GradientBoostingRegressor, HistGradientBoostingRegressor,\
    AdaBoostClassifier, GradientBoostingClassifier, HistGradientBoostingClassifier
from xgboost.sklearn import XGBRegressor, XGBClassifier
from lightgbm import LGBMRegressor, LGBMClassifier
from catboost import CatBoostRegressor,CatBoostClassifier
from sklearn.ensemble import ExtraTreesRegressor, ExtraTreesClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
RANDOM_SEED = 42

random_state = RANDOM_SEED
base_model = {
    "AdaBoost": AdaBoostRegressor(n_estimators=100),
    "GTBoost": GradientBoostingRegressor(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0),
    "HBGBoost": HistGradientBoostingRegressor(max_iter=100),
    "xgboost": XGBRegressor(eval_metric=['logloss', 'auc', 'error']),
    #"LightGBM": LGBMRegressor(learning_rate=0.1, max_depth=3, num_leaves=16),
    "CatBoost": CatBoostRegressor(learning_rate=0.1, depth=6, iterations=100, verbose=False),
}

final_model = RandomForestRegressor(max_depth=5, n_estimators=150)
