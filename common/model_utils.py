from tensorflow.keras.models import Model
class ModelUtils():

    @staticmethod
    def save_keras_model(model: Model, file_name: str):
        model.save(file_name + '.h5')
