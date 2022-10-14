import tensorflow as tf
from tensorflow import keras
from tictac import Game

game = Game() 
input_shape = (game.board.shape[0],game.board.shape[1])
size = game.board.shape[0] * game.board.shape[1]
channels = 100

model = keras.Sequential([
    keras.layers.Reshape((size,),input_shape=input_shape),
    keras.layers.Dense(channels,activation="relu"),
    keras.layers.Dropout(0.05),
    keras.layers.Dense(channels,activation="relu"), 
    keras.layers.Dropout(0.05), 
    keras.layers.Dense(channels,activation="relu"),
    keras.layers.Dropout(0.05),
    keras.layers.Reshape(input_shape),
    keras.layers.Softmax()
])

model.compile(optimizer='adam', 
              loss=tf.losses.CategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])