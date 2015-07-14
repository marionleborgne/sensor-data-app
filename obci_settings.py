DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

SENSOR = ['openbci']
METRICS = ['channel_0', 'channel_1', 'channel_2', 'channel_3', 'channel_4', 'channel_5', 'channel_6', 'channel_7']
COLUMNS = ['metric_value', 'prediction', 'anomaly_score', 'anomaly_likelihood']
SENSOR_ID = 'openbci_marion'

# threshold above which a metric will be considered anomalous
ANOMALY_LIKELIHOOD_THRESHOLD = 0.95


CONVERTED_DATA_DIR = "converted_data"

INPUT_DATA_DIR = "input_data"

MODEL_PARAMS_DIR = "model_params"

MODEL_RESULTS_DIR = "model_results"

PLOT_RESULTS_DIR = "plot_results"

PATIENT_IDS = ['retro2015-renata', 'retro2015-robert', 'retro2015-bob', 'retro2015-lorri', 'retro2015-autumn']

#INPUT_DATA_FILE = "trajectories-20150403-000430.csv"
INPUT_DATA_FILE = "trajectories-long-20150427-150483.csv"


