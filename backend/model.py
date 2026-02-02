import tensorflow as tf

MODEL_PATH = "colorizer_generator"

generator = tf.keras.models.load_model(MODEL_PATH)
generator.trainable = False
