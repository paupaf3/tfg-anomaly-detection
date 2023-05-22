import numpy as np
import matplotlib.pyplot as plt

class DataVisualization():
    
    @staticmethod
    def training_test_loss(history):
        plt.plot(history.history['loss'], label='Training set loss')
        plt.plot(history.history['val_loss'], label='Test set loss',  color='r')
        # plt.set_xlabel('epochs')
        # plt.set_ylabel('loss')
        plt.legend(['Training set loss', 'Test set loss'])

    @staticmethod
    def data_reconstruction(original, reconstruction, index, features):
        plt.figure(figsize=(15,5))
        plt.subplot(1,2,1)
        plt.plot(original[index],'b')
        plt.plot(reconstruction[index],'r')
        plt.fill_between(np.arange(features), reconstruction[index], original[index], color='lightcoral')
        plt.legend(labels=["Original", "Reconstruction", "Error"])