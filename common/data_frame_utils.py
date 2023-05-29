import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

class DataFrameClassification():

    INVERSOR_OK: int = 1
    INVERSOR_ERROR: int = 2
    ALTERNA_ERROR: int = 3 

class DataFrameUtils():

    @staticmethod
    def change_state_by_identifier(dataframe: pd.DataFrame):
        # Cambiar valores de los string por un identificador
        dataframe.loc[dataframe['Estado'] == 'Estado del inversor OK', 'Estado'] = DataFrameClassification.INVERSOR_OK
        dataframe.loc[dataframe['Estado'] == 'Fallo del inversor', 'Estado'] = DataFrameClassification.INVERSOR_ERROR
        dataframe.loc[dataframe['Estado'] == 'Fallo de alterna del inversor', 'Estado'] = DataFrameClassification.ALTERNA_ERROR

        return dataframe

    @staticmethod
    def train_test_split(dataframe: pd.DataFrame, test_size: float):
        train_df, test_df = train_test_split(dataframe, test_size=test_size)
        # Eliminar estados erróneos del dataframe de entreno
        test_df = pd.concat([test_df, \
            train_df[train_df.Estado == DataFrameClassification.INVERSOR_ERROR], \
            train_df[train_df.Estado == DataFrameClassification.ALTERNA_ERROR]])
        train_df = train_df[train_df['Estado'] == DataFrameClassification.INVERSOR_OK]
        # Ordenar por fecha
        train_df = train_df.sort_values('Data')
        test_df = test_df.sort_values('Data')

        train_df = train_df.drop('Data', axis=1)
        test_df = test_df.drop('Data', axis=1)

        train_df = train_df.drop('Fecha', axis=1)
        test_df = test_df.drop('Fecha', axis=1)

        return train_df, test_df

    @staticmethod
    def get_train_dataframe_as_preprocessed_np_array(dataframe: pd.DataFrame):
        dataframe = dataframe.drop('Estado', axis=1)
        min_max_scaler = MinMaxScaler()
        return min_max_scaler.fit_transform(dataframe.values)
    
    @staticmethod
    def get_test_mixed_dataframe_as_preprocessed_np_array(dataframe: pd.DataFrame):
        dataframe_state = dataframe['Estado']
        dataframe = dataframe.drop('Estado', axis=1)
        min_max_scaler = MinMaxScaler()
        return min_max_scaler.fit_transform(dataframe.values), dataframe_state

    @staticmethod
    def get_test_ok_dataframe_as_preprocessed_np_array(dataframe: pd.DataFrame):
        min_max_scaler = MinMaxScaler()
        dataframe_ok = dataframe[dataframe['Estado'] == DataFrameClassification.INVERSOR_OK]

        dataframe_ok = dataframe_ok.drop('Estado', axis=1)
        return min_max_scaler.fit_transform(dataframe_ok.values)

    @staticmethod
    def get_test_error_dataframe_as_preprocessed_np_array(dataframe: pd.DataFrame):
        min_max_scaler = MinMaxScaler()
        dataframe_error = pd.concat([dataframe[dataframe['Estado'] == DataFrameClassification.INVERSOR_ERROR], \
            dataframe[dataframe['Estado'] == DataFrameClassification.ALTERNA_ERROR]])

        dataframe_error = dataframe_error.drop('Estado', axis=1)
        return min_max_scaler.fit_transform(dataframe_error.values)

    @staticmethod
    def temporalize(X, y, lookback):
        output_X = []
        output_y = []
        for i in range(len(X)-lookback-1):
            t = []
            for j in range(1,lookback+1):
                t.append(X[[(i+j+1)], :])
            output_X.append(t)
            output_y.append(y[i+lookback+1])
        return output_X, output_y

    @staticmethod
    def detemporalize(output_X):
        return output_X[:, 0, :]