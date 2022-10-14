# coding: utf-8

import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
relu = keras.activations.relu()

class Network():
    def __init__(self, board_width, board_height, num_ships, model_file=None):
        self.board_width = board_width
        self.board_height = board_height
        self.num_ships = num_ships
        self.num_input_dimension = self.num_ships + 1
        self.input_shape = self.num_input_dimension * self.board_height * self.board_width
        self.board_size = self.board_width * self.board_height
        self.hidden_units = self.board_size
        self.output_units = self.board_size
        self.model_file = model_file
        self.type = tf.float32
        
        self.make_network(self)

    def make_network(self): 
        # Define the tensorflow neural network
        # 1. Input:
        self.model = keras.Sequential([
                keras.layers.Conv2D(filters=32,padding='same',acivation=relu,input_shape=[1, self.input_shape]),
                keras.layers.Conv2D(filters=64,padding='same',actiovation=relu),
                keras.layers.Conv2D(filters=self.num_input_dimension,padding='same',activation=relu),
                keras.layers.Dense(self.board_size),
                keras.layers.Softmax()
        ])
        
        opt = keras.optimizers.Adam(learning_rate=0.001)
        self.model.compile(optimizer=opt)
        
        history = self.model.fit(self.train_images,self.train_labels,self.train_dataset
        ,epochs=10,loss=tf.losses.SparseCategoricalCrossentropy())

        if self.model_file:
            print('Loading model from file: ', self.model_file)
            self.model.load_weights(self.model_file)

    def getBoardProbabilities(self, input_dimensions):
        """
        input: a batch of states
        output: a batch of action probabilities and state values
        """
        return self.session.run(
                self.probabilities,
                feed_dict={self.input_dimensions: input_dimensions}
                )

    def runTrainStep(self, input_dimensions, labels, learning_rate):
        """perform a training step"""
        entropy, _ = self.session.run(
                [self.cross_entropy, self.optimizer],
                feed_dict={self.input_dimensions: input_dimensions,
                           self.labels: labels,
                           self.learning_rate: learning_rate
                           })
        return entropy

    def saveModel(self):
        self.model.save_weights(self.model_file)

    def restoreModel(self, model_path):
        self.model.load_weights(self.model_file)


class Network_tf1():
    def __init__(self, board_width, board_height, num_ships, model_file=None):
        self.board_width = board_width
        self.board_height = board_height
        self.num_ships = num_ships
        self.num_input_dimension = self.num_ships + 1
        self.board_size = self.board_width * self.board_height
        self.hidden_units = self.board_size
        self.output_units = self.board_size
        self.model_file = model_file
        self.type = tf.float32
        
        self.make_network_tensorflow1(self)

    def make_network_tensorflow1(self): 
        tf.reset_default_graph()
        # Define the tensorflow neural network
        # 1. Input:
        self.input_dimensions = tf.placeholder(
                self.type, shape=[1, self.num_input_dimension * self.board_height * self.board_width])
        self.input_dimensions_reshaped = tf.reshape(
                self.input_dimensions, [-1, self.board_height, self.board_width, self.num_input_dimension])
        # 2. Networks Layers
        self.layer1 = tf.layers.conv2d(inputs=self.input_dimensions_reshaped,
                                      filters=32, kernel_size=[3, 3],
                                      padding="same", activation=tf.nn.relu)
        self.layer2 = tf.layers.conv2d(inputs=self.layer1, filters=64,
                                      kernel_size=[3, 3], padding="same",
                                      activation=tf.nn.relu)
        self.layer3 = tf.layers.conv2d(inputs=self.layer2, filters=self.num_input_dimension,
                                            kernel_size=[1, 1], padding="same",
                                            activation=tf.nn.relu)
        self.layer3_reshaped = tf.reshape(
                self.layer3, [-1, self.board_height * self.board_width * self.num_input_dimension])

        # Alternative network structure, simple but not effective compared to CNN
        # self.layer1 = tf.layers.dense(inputs=self.input_dimensions, units=self.num_input_dimension * self.board_size, activation=tf.nn.relu)
        # self.layer2 = tf.layers.dense(inputs=self.layer1, units=self.num_input_dimension * self.board_size, activation=tf.nn.relu)
        self.logits = tf.layers.dense(inputs=self.layer3_reshaped, units=self.board_size)
        self.probabilities = tf.nn.softmax(self.logits)

        # Training step
        self.labels = tf.placeholder(tf.int64)
        self.learning_rate = tf.placeholder(self.type, shape=[])
        self.cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
                logits=self.logits, labels=self.labels)
        # Define loss
        self.loss = tf.reduce_sum(tf.multiply(self.learning_rate, self.cross_entropy))
        self.optimizer = tf.train.AdamOptimizer(learning_rate=0.0005).minimize(self.loss)

        # Start TF session
        self.session = tf.Session()
        init = tf.initialize_all_variables()
        self.session.run(init)

        # For saving and restoring
        self.saver = tf.train.Saver()
        if self.model_file:
            print('load model', self.model_file)
            self.restoreModel(self.model_file)

    def getBoardProbabilities(self, input_dimensions):
        """
        input: a batch of states
        output: a batch of action probabilities and state values
        """
        return self.session.run(
                self.probabilities,
                feed_dict={self.input_dimensions: input_dimensions}
                )

    def runTrainStep(self, input_dimensions, labels, learning_rate):
        """perform a training step"""
        entropy, _ = self.session.run(
                [self.cross_entropy, self.optimizer],
                feed_dict={self.input_dimensions: input_dimensions,
                           self.labels: labels,
                           self.learning_rate: learning_rate
                           })
        return entropy

    def saveModel(self, model_path):
        self.saver.save(self.session, model_path)

    def restoreModel(self, model_path):
        self.saver.restore(self.session, model_path)