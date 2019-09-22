"""
Deep Neural Net

(Name: Classic Feedforward)

"""

import numpy as np
import pickle, json
import sklearn.datasets
import random
import time
import os

# cataloguing the various activation functions and their derivatives

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))

def relU(z):
    return np.maximum(z, 0, z)

def relU_prime(z):
    return z * (z <= 0)

def tanh(z):
    return np.tanh(z)

def tanh_prime(z):
    return 1 - (tanh(z) ** 2)

def transform_target(y):
    t = np.zeros((10, 1))
    t[int(y)] = 1.0
    return t


class NeuralNet:

    def __init__(self, layers, learning_rate=0.05, reg_lambda=0.01):
        self.num_layers = len(layers)

        # initialising network parameters
        self.layers = layers
        self.biases = [np.zeros((y, 1)) for y in layers[1:]]
        self.weights = [np.random.normal(loc=0.0, scale=0.1, size=(y, x))
                                       for x, y in zip(layers[:-1], layers[1:])]
        self.learning_rate = learning_rate
        self.reg_lambda = reg_lambda

        # initialising network activation function
        self.nonlinearity = relU
        self.nonlinearity_prime = relU_prime

    def __feedforward(self, x):
        ''' Returns softmax probabilities for the output layer '''

        for w, b in zip(self.weights, self.biases):
            x = self.nonlinearity(np.dot(w, np.reshape(x, (len(x), 1))) + b)

        return np.exp(x) / np.sum(np.exp(x))

    def __backpropagation(self, x, y):
        '''
        Perform the forward pass followed by backprop
        :param x: input
        :param y: target

        '''

        weight_gradients = [np.zeros(w.shape) for w in self.weights]
        bias_gradients = [np.zeros(b.shape) for b in self.biases]

        # forward pass - transform input to output softmax probabilities
        activation = x
        hidden_activations = [np.reshape(x, (len(x), 1))]
        z_list = []

        for w, b in zip(self.weights, self.biases):
            z = np.dot(w, np.reshape(activation, (len(activation), 1))) + b
            z_list.append(z)
            activation = self.nonlinearity(z)
            hidden_activations.append(activation)

        t = hidden_activations[-1]
        hidden_activations[-1] = np.exp(t) / np.sum(np.exp(t))   # softmax layer

        # backward pass
        delta = (hidden_activations[-1] - y) * (z_list[-1] > 0)
        weight_gradients[-1] = np.dot(delta, hidden_activations[-2].T)
        bias_gradients[-1] = delta

        for l in range(2, self.num_layers):
            z = z_list[-l]
            delta = np.dot(self.weights[-l + 1].T, delta) * (z > 0)
            weight_gradients[-l] = np.dot(delta, hidden_activations[-l - 1].T)
            bias_gradients[-l] = delta

        return (weight_gradients, bias_gradients)

    def __update_params(self, weight_gradients, bias_gradients):
        ''' Update network parameters after backprop step '''
        for i in xrange(len(self.weights)):
            self.weights[i] += -self.learning_rate * weight_gradients[i]
            self.biases[i] += -self.learning_rate * bias_gradients[i]

    def train(self, training_data, validation_data=None, epochs=10):
        ''' Train the network for `epoch` iterations '''

        bias_gradients = None
        for i in xrange(epochs):
            random.shuffle(training_data)
            inputs = [data[0] for data in training_data]
            targets = [data[1] for data in training_data]

            for j in xrange(len(inputs)):
                (weight_gradients, bias_gradients) = self.__backpropagation(inputs[j], targets[j])
                self.__update_params(weight_gradients, bias_gradients)

            if validation_data:
                random.shuffle(validation_data)
                inputs = [data[0] for data in validation_data]
                targets = [data[1] for data in validation_data]

                for j in xrange(len(inputs)):
                    (weight_gradients, bias_gradients) = self.__backpropagation(inputs[j], targets[j])
                    self.__update_params(weight_gradients, bias_gradients)

            print("{} epoch(s) done".format(i + 1))

        print("Training done.")

    def test(self, test_data):
        test_results = [(np.argmax(self.__feedforward(x[0])), np.argmax(x[1])) for x in test_data]
        return float(sum([int(x == y) for (x, y) in test_results])) / len(test_data) * 100

    def dump(self, file):
        pickle.dump(self, open(file, "wb"))



if __name__ == "__main__":
    total = 5000
    training = int(total * 0.7)
    val = int(total * 0.15)
    test = int(total * 0.15)

    mnist = sklearn.datasets.fetch_mldata('MNIST original', data_home='./data')

    data = zip(mnist.data, mnist.target)
    random.shuffle(data)
    data = data[:total]
    data = [(x[0].astype(bool).astype(int), transform_target(x[1])) for x in data]

    train_data = data[:training]
    val_data = data[training:training+val]
    test_data = data[training+val:]

    print ("Data fetched")

    NN = NeuralNet([784, 32, 10]) # defining an ANN with 1 input layer (size 784 = size of the image flattened), 1 hidden layer (size 32), and 1 output layer (size 10, unit at index i will predict the probability of the image being digit i, where 0 <= i <= 9)

    NN.train(train_data, val_data, epochs=5)

    print ("Network trained")

    print ("Accuracy:", str(NN.test(test_data)) + "%")
