import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.tree import DecisionTreeRegressor
from tpot.builtins import StackingEstimator
from sklearn.preprocessing import FunctionTransformer
from copy import copy

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:-0.5645432770937358
exported_pipeline = make_pipeline(
    make_union(
        FunctionTransformer(copy),
        StackingEstimator(estimator=make_pipeline(
            StackingEstimator(estimator=DecisionTreeRegressor(max_depth=3, min_samples_leaf=14, min_samples_split=18)),
            DecisionTreeRegressor(max_depth=9, min_samples_leaf=20, min_samples_split=2)
        ))
    ),
    DecisionTreeRegressor(max_depth=5, min_samples_leaf=15, min_samples_split=8)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
