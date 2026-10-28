# Conjunto de datos.
CITIES = ['auckland', 'christchurch']
START_DATE = '2018-01-01'
END_DATE = '2025-12-31'
SAITS_BOUNDARY_YEAR = 2024 # Límite entre entrenamiento y validación.
VAL_BOUNDARY_YEAR = 2023 # Límite entre entrenamiento y validación.
TEST_BOUNDARY_YEAR = 2024 # Límite entre validación y pruebas.

# Hiperparámetros de modelos.
WINDOW_SIZE = 30 # Número de días que contiene una ventana.
MISSING_VALUES = 0.1 # Porcentaje de datos a ocultar.
HORIZON_DAYS = 30 # Conjunto de días a predecir.
NUM_EPOCHS_OPTUNA = 20 # Número de procesamientos de todo el conjunto de datos de entrenamiento.
NUM_EPOCHS_SAITS = 50
NUM_EPOCHS_LSTM = 80
MAX_ITERATIONS = 1500 # Número máximo de árboles de decisión.
NUM_TRIALS = 20 # Número de experimentos individuales de Optuna con una configuración específica.
PATIENCE = 50 # Número de épocas consecutivas sin mejora en la métrica para parar un entrenamiento.
PATIENCE_OPTUNA = 5

# Factores de tráfico.
SLOW_LANE_TRUCK_FACTOR = 1.4 # Factor de tráfico pesado para carril lento o único.
CENTER_LANE_TRUCK_FACTOR = 0.8 # Factor de tráfico pesado para carriles centrales (más de dos carriles).
FAST_LANE_TRUCK_FACTOR = 0.3 # Factor de tráfico pesado para carril rápido (dos o más carriles).

# Factores ambientales.
STRONG_WIND = 25.0 # Velocidad mínima en millas por hora.
EXTREME_HEAT = 50.0 # Temperatura máxima en Celsius.