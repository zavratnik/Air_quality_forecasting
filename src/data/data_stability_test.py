import pandas as pd
import numpy as np

from evidently import ColumnMapping

from evidently.report import Report
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.metrics import *

from evidently.test_suite import TestSuite
from evidently.tests.base_test import generate_column_tests
from evidently.test_preset import DataStabilityTestPreset, NoTargetPerformanceTestPreset
from evidently.tests import *

# Load your reference and current data as Pandas DataFrames
reference_data = pd.read_csv('data/processed/reference_data.csv')
current_data = pd.read_csv('data/processed/current_data.csv')

reference_data.rename(columns={'pm10': 'target'}, inplace=True)
reference_data['prediction'] = reference_data['target'].values + np.random.normal(0, 5, reference_data.shape[0])

current_data.rename(columns={'pm10': 'target'}, inplace=True)
current_data['prediction'] = current_data['target'].values + np.random.normal(0, 5, current_data.shape[0])

report = Report(metrics=[
    DataDriftPreset(),
])


report.run(reference_data=reference_data, current_data=current_data)
report
report.save_html("reports/DataDriftPreset_report.html")

tests = TestSuite(tests=[
    TestNumberOfColumnsWithMissingValues(),
    TestNumberOfRowsWithMissingValues(),
    TestNumberOfConstantColumns(),
    TestNumberOfDuplicatedRows(),
    TestNumberOfDuplicatedColumns(),
    TestColumnsType(),
    TestNumberOfDriftedColumns(),
])

tests.run(reference_data=reference_data, current_data=current_data)
tests
tests.save_html("reports/DataStabilityTest_report.html")
