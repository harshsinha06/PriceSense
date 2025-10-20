# ...existing code...
import json
import pickle
import numpy as np
from pathlib import Path

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bath, bhk):
    """Note: parameter order = location, sqft, bath, bhk (matches server.py)"""
    try:
        loc = location.lower()
        loc_index = __data_columns.index(loc)
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    base_dir = Path(__file__).resolve().parent          # server/
    artifacts_dir = base_dir / "artifacts"               # server/artifacts

    cols_path = artifacts_dir / "columns.json"
    model_path = artifacts_dir / "banglore_home_prices_model.pickle"

    if not cols_path.exists() or not model_path.exists():
        raise FileNotFoundError(f"Missing artifacts. Expected: {cols_path} and {model_path}")

    with open(cols_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first three are sqft, bath, bhk

    if __model is None:
        with open(model_path, "rb") as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names()[:10])
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
# ...existing code...