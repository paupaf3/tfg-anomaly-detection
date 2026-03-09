# TFG Anomaly Detection

This project is focused on anomaly detection in photovoltaic inverter data using deep learning models (Autoencoder and LSTM Autoencoder). It is organized into several experiments and common utility modules.

## Project Structure

- **common/**: Shared Python utilities for data processing and visualization.
  - `data_frame_utils.py`: DataFrame manipulation and preprocessing functions.
  - `data_visualization.py`: Functions for plotting training/test loss and data reconstruction.
  - `parser_utils.py`: Utilities for loading and merging inverter and meteorological data.
- **experiment1/**: First experiment using an Autoencoder model.
  - `autoencoder_experiment_1.ipynb`: Jupyter notebook for the experiment.
  - `autoencoder_experiment_1.h5`: Trained model weights.
- **experiment2/**: Second experiment using an LSTM Autoencoder model.
  - `lstm_autoencoder_experiment_2.ipynb`: Jupyter notebook for the experiment.
  - `lstm_autoencoder_experiment_2.h5`: Trained model weights.
- **experiment3/**: Multiple experiments with different dataset sizes and models.
  - `1000_autoencoder_experiment_3.ipynb`, `2000_autoencoder_experiment_3.ipynb`, `4000_autoencoder_experiment_3.ipynb`: Autoencoder experiments with 1000, 2000, and 4000 samples.
  - `1000_lstm_autoencoder_experiment_3.ipynb`, `2000_lstm_autoencoder_experiment_3.ipynb`, `4000_lstm_autoencoder_experiment_3.ipynb`: LSTM Autoencoder experiments with 1000, 2000, and 4000 samples.

## How to Use

1. **Install dependencies**: Make sure you have Python 3.x and install required packages (e.g., pandas, numpy, scikit-learn, matplotlib, tensorflow, keras).
2. **Prepare data**: Place your inverter and meteorological CSV files in the expected `data/csv/` directory structure.
3. **Run experiments**: Open the desired Jupyter notebook in the `experiment1`, `experiment2`, or `experiment3` folders and execute the cells.