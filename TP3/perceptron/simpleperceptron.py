from math import copysign

class SimplePerceptron:
    def __init__(self, weights, learning_rate):   
        self.weights = weights
        self.learning_rate = learning_rate

    def predict(self, point):
        h = 0
        for idx, coord in enumerate(point):
            h += coord*self.weights[idx]
        return copysign(1, h)
    
    def train(self, point, expected):
        predicted = self.predict(point)
        for idx, coord in enumerate(point):
            n = self.learning_rate * (expected - predicted)
            delta_w = n * coord
            self.weights[idx] = self.weights[idx] + delta_w 

    def predict_list(self, point_list):
        predicted_list = list()
        for point in point_list:
            predicted_list.append(self.predict(point))
        return predicted_list
            
    def train_list(self, point_list, expected_list):
        for idx, point in enumerate(point_list):
            self.train(point, expected_list[idx])

    def __str__(self):
        nl = '\n'
        op = '{'
        cl = '}'
        return f'{op}{nl} weights: {self.weights}{nl} rate: {self.learning_rate}{nl}{cl}'
