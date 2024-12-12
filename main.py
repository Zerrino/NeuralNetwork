import random

class Neuron:
    def __init__(self, inputs):
        #print("Neuron Created " + str(self))
        self.inputs = inputs
        self.bias = random.uniform(-1, 1)
        self.weights = [random.uniform(-1, 1) for _ in inputs]
        self.output = 0
    def check(self):
        return len(self.weights) == len(self.inputs)
    def calcul_output(self):
        self.output = 0
        if not self.check():
            return
        i = 0
        while i < len(self.inputs):
            self.output += self.inputs[i] * self.weights[i]
            i += 1
        self.output += self.bias
    def ReLU(self):
        if self.output < 0:
            self.output = 0

class NeuronNetwork:
    def __init__(self, input_number, hidden_number, hidden_layer_number, output_number, neuron_list=None):
        print("Neuron Network created!")
        self.input_number = input_number
        self.hidden_number = hidden_number
        self.hidden_layer_number = hidden_layer_number
        self.output_number = output_number

        self.input_layer = []
        self.hidden_layer = []
        self.output_layer = []
        self.output = []
        self.val = ""
        self.count = 0

        self.neuron_list = neuron_list if neuron_list is not None else []
        self.flag = 0
        if self.neuron_list:
            self.flag = 1
    def input_neuron_calcul(self):
        for x in self.input_number:
            if self.flag == 0:
                input_neuron = Neuron(
                    inputs=[x]
                )
            else:
                input_neuron = self.neuron_list[self.count]
                self.count += 1
            input_neuron.calcul_output()
            input_neuron.ReLU()
            self.neuron_list.append(input_neuron)
            self.input_layer.append(input_neuron.output)
            self.val += " ."
        self.val += "\n"
    def hidden_neuron_calcul(self):
        self.hidden_layer = self.input_layer
        i = 0
        while i < self.hidden_layer_number:
            output_new = []
            j = 0
            while j < self.hidden_number:
                if self.flag == 0:
                    hidden_neuron = Neuron(
                        inputs=self.hidden_layer
                    )
                else:
                    hidden_neuron = self.neuron_list[self.count]
                    self.count += 1
                hidden_neuron.calcul_output()
                hidden_neuron.ReLU()
                self.neuron_list.append(hidden_neuron)
                output_new.append(hidden_neuron.output)
                j += 1
                self.val += " ."
            self.hidden_layer = output_new
            self.val += "\n"
            i += 1
    def output_neuron_calcul(self):
        self.output_layer = self.hidden_layer
        i = 0
        while i < self.output_number:
            if self.flag == 0:
                output_neuron = Neuron(
                    inputs=self.output_layer
                )
            else:
                output_neuron = self.neuron_list[self.count]
                self.count += 1
            output_neuron.calcul_output()
            output_neuron.ReLU()
            self.neuron_list.append(output_neuron)
            self.output.append(output_neuron.output)
            i += 1
            self.val += " ."
    def print_visual(self):
        print(self.val)

MyNeuralNetwork = NeuronNetwork(
    input_number=[100],
    hidden_number=100,
    hidden_layer_number=100,
    output_number=10
)

MyNeuralNetwork.input_neuron_calcul()
MyNeuralNetwork.hidden_neuron_calcul()
MyNeuralNetwork.output_neuron_calcul()

print(MyNeuralNetwork.output)

NewNeuralNetwork = NeuronNetwork(
    input_number=[100, 15, 3],
    hidden_number=15,
    hidden_layer_number=5,
    output_number=3,
    neuron_list=MyNeuralNetwork.neuron_list
)

NewNeuralNetwork.input_neuron_calcul()
NewNeuralNetwork.hidden_neuron_calcul()
NewNeuralNetwork.output_neuron_calcul()

print(NewNeuralNetwork.output)

NewNeuralNetwork.print_visual()
