import os
import pandas as pd
from common.data_frame_utils import DataFrameUtils
from datetime import datetime

class ParserUtils():

    @staticmethod
    def get_full_dataframe(inversor_num: int, month: int, year: int): 
        inversor_df = ParserUtils.get_inversor_dataframe(inversor_num, month, year)
        meteo_df = ParserUtils.get_meteo_dataframe(month, year)

        main_df = pd.merge(inversor_df, meteo_df, how='inner', left_on='Data', right_on='Fecha')
        
        # Mover fecha al principio
        temp_cols=main_df.columns.tolist()
        index=main_df.columns.get_loc("Fecha")
        new_cols=temp_cols[index:index+1] + temp_cols[0:index] + temp_cols[index+1:]
        main_df=main_df[new_cols]
        DataFrameUtils.change_state_by_identifier(main_df)

        return main_df

    @staticmethod
    def get_inversor_dataframe(inversor_num: int, month: int, year: int): 
        if (inversor_num == None):
            inversor_path_1 = os.getcwd() + '/data/csv/inversor1.csv'
            inversor_df_1 = pd.read_csv(inversor_path_1)
            inversor_path_2 = os.getcwd() + '/data/csv/inversor2.csv'
            inversor_df_2 = pd.read_csv(inversor_path_2)
            inversor_path_3 = os.getcwd() + '/data/csv/inversor3.csv'
            inversor_df_3 = pd.read_csv(inversor_path_3)
            inversor_path_4 = os.getcwd() + '/data/csv/inversor4.csv'
            inversor_df_4 = pd.read_csv(inversor_path_4)
            inversor_path_5 = os.getcwd() + '/data/csv/inversor5.csv'
            inversor_df_5 = pd.read_csv(inversor_path_5)
            inversor_path_7 = os.getcwd() + '/data/csv/inversor7.csv'
            inversor_df_7 = pd.read_csv(inversor_path_7)
            inversor_df = pd.concat([inversor_df_1, inversor_df_2, inversor_df_3, inversor_df_4, inversor_df_5, inversor_df_7])
            inversor_df = inversor_df.drop('Inversor', axis=1)
            inversor_df = inversor_df.drop('kWh(Accumulated)', axis=1)
        else:
            inversor_path = os.getcwd() + '/data/csv/inversor' + str(inversor_num) + '.csv'
            inversor_df = pd.read_csv(inversor_path)
            inversor_df = inversor_df.drop('Inversor', axis=1)
            inversor_df = inversor_df.drop('kWh(Accumulated)', axis=1)
        
        if (month == None and year == None):
            return inversor_df
        
        else:
            month_str = str(month)
            
            if(len(month_str) == 1):
                month_str = '0' + month_str

            inversor_df = inversor_df[inversor_df['Data'].str.contains(month_str + '/' + str(year), na=False)]
            return inversor_df

    @staticmethod
    def get_meteo_dataframe(month: int, year: int):
        if (month == None and year == None):
            meteo_data_path_1 = os.getcwd() + '/data/meteo-2021-1.csv'
            meteo_df_1 = pd.read_csv(meteo_data_path_1)
            
            meteo_data_path_2 = os.getcwd() + '/data/meteo-2021-2.csv'
            meteo_df_2 = pd.read_csv(meteo_data_path_2)
            
            meteo_data_path_3 = os.getcwd() + '/data/meteo-2021-3.csv'
            meteo_df_3 = pd.read_csv(meteo_data_path_3)
            
            meteo_data_path_4 = os.getcwd() + '/data/meteo-2021-4.csv'
            meteo_df_4 = pd.read_csv(meteo_data_path_4)
            
            meteo_data_path_5 = os.getcwd() + '/data/meteo-2021-5.csv'
            meteo_df_5 = pd.read_csv(meteo_data_path_5)
            
            meteo_data_path_6 = os.getcwd() + '/data/meteo-2021-6.csv'
            meteo_df_6 = pd.read_csv(meteo_data_path_6)

            meteo_df = pd.concat([meteo_df_1, meteo_df_2, meteo_df_3, meteo_df_4, meteo_df_5, meteo_df_6])
            meteo_df = meteo_df.drop('Instalación', axis=1)
            return meteo_df

        else:
            meteo_path = os.getcwd() + '/data/meteo-' + str(year) + '-' + str(month) + '.csv'
            meteo_df = pd.read_csv(meteo_path)
            meteo_df = meteo_df.drop('Instalación', axis=1)
            return meteo_df

    @staticmethod
    def get_full_dataframe_without_error_previous_data(inversor_num: int, month: int, year: int, previous_data_num: int): 
        inversor_df = ParserUtils.get_inversor_dataframe_without_error_previous_data(inversor_num, month, year, previous_data_num)
        meteo_df = ParserUtils.get_meteo_dataframe(month, year)

        main_df = pd.merge(inversor_df, meteo_df, how='inner', left_on='Data', right_on='Fecha')
        
        # Mover fecha al principio
        temp_cols=main_df.columns.tolist()
        index=main_df.columns.get_loc("Fecha")
        new_cols=temp_cols[index:index+1] + temp_cols[0:index] + temp_cols[index+1:]
        main_df=main_df[new_cols]
        DataFrameUtils.change_state_by_identifier(main_df)

        return main_df
    
    @staticmethod
    def get_inversor_dataframe_without_error_previous_data(inversor_num: int, month: int, year: int, previous_data_num: int): 
        if (inversor_num == None):
            inversor_path_1 = os.getcwd() + '/data/csv/inversor1_' + str(previous_data_num) + '.csv'
            inversor_df_1 = pd.read_csv(inversor_path_1)
            inversor_path_2 = os.getcwd() + '/data/csv/inversor2_' + str(previous_data_num) + '.csv'
            inversor_df_2 = pd.read_csv(inversor_path_2)
            inversor_path_3 = os.getcwd() + '/data/csv/inversor3_' + str(previous_data_num) + '.csv'
            inversor_df_3 = pd.read_csv(inversor_path_3)
            inversor_path_4 = os.getcwd() + '/data/csv/inversor4_' + str(previous_data_num) + '.csv'
            inversor_df_4 = pd.read_csv(inversor_path_4)
            inversor_path_5 = os.getcwd() + '/data/csv/inversor5_' + str(previous_data_num) + '.csv'
            inversor_df_5 = pd.read_csv(inversor_path_5)
            inversor_path_7 = os.getcwd() + '/data/csv/inversor7_' + str(previous_data_num) + '.csv'
            inversor_df_7 = pd.read_csv(inversor_path_7)
            inversor_df = pd.concat([inversor_df_1, inversor_df_2, inversor_df_3, inversor_df_4, inversor_df_5, inversor_df_7])
            inversor_df = inversor_df.drop('Inversor', axis=1)
            inversor_df = inversor_df.drop('kWh(Accumulated)', axis=1)
        else:
            inversor_path = os.getcwd() + '/data/csv/inversor' + str(inversor_num) + '_' + str(previous_data_num) +  '.csv'
            inversor_df = pd.read_csv(inversor_path)
            inversor_df = inversor_df.drop('Inversor', axis=1)
            inversor_df = inversor_df.drop('kWh(Accumulated)', axis=1)
        
        if (month == None and year == None):
            return inversor_df
        
        else:
            month_str = str(month)
            
            if(len(month_str) == 1):
                month_str = '0' + month_str

            inversor_df = inversor_df[inversor_df['Data'].str.contains(month_str + '/' + str(year), na=False)]
            return inversor_df