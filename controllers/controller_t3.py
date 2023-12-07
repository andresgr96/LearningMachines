import numpy as np
from controller import Controller
from src.LearningMachines.utils.deep_l import tanh_activation, sigmoid_activation
from src.LearningMachines.utils.computer_vision import red_mask, green_mask, detect_objects
from src.LearningMachines.utils.infra_sensors import gripper, get_irs_sensors


class RoboboController(Controller):
    def __init__(self, rob):
        # Number of hidden neurons
        self.n_hidden_neurons = 11
        self.n_hidden = [self.n_hidden_neurons]
        self.number_of_sensors = 13
        self.number_of_actions = 2
        self.rob = rob
        
        # Irs Sensors
        self.back_L = 0
        self.back_R = 0
        self.back_C = 0
        self.front_LL = 0
        self.front_L = 0
        self.front_C = 0
        self.front_R = 0
        self.front_RR = 0

        self.green_left = 0
        self.green_center = 0
        self.green_right = 0
        self.red_left = 0
        self.red_center = 0
        self.red_right = 0

        self.food_in_gripper = 0

    def step(self, controller: np.array):
        left, right = self.control(controller)

        self.rob.move(left, right, 500)

    def control(self, controller: np.array):
        inputs = self.build_inputs()
        # print(inputs)
        if self.n_hidden[0] > 0:

            # Biases for the n hidden neurons
            bias1 = controller[:self.n_hidden[0]].reshape(1, self.n_hidden[0])
            # Weights for the connections from the inputs to the hidden nodes
            weights1_slice = len(inputs) * self.n_hidden[0] + self.n_hidden[0]
            weights1 = controller[self.n_hidden[0]:weights1_slice].reshape((len(inputs), self.n_hidden[0]))

            # Outputs activation first layer.
            output1 = tanh_activation(inputs.dot(weights1) + bias1)

            # Preparing the weights and biases from the controller of layer 2
            bias2 = controller[weights1_slice:weights1_slice + self.number_of_actions].reshape(1,
                                                                                               self.number_of_actions)
            weights2 = controller[weights1_slice + self.number_of_actions:].reshape(
                (self.n_hidden[0], self.number_of_actions))

            # Outputting activated second layer. Each entry in the output is an action
            output = tanh_activation(output1.dot(weights2) + bias2)[0]
        else:
            bias = controller[:self.number_of_actions].reshape(1, self.number_of_actions)
            weights = controller[self.number_of_actions:].reshape((len(inputs), self.number_of_actions))

            output = sigmoid_activation(inputs.dot(weights) + bias)[0]

        left_wheel = int(30 * output[0])
        right_wheel = int(30 * output[1])

        return [left_wheel, right_wheel]

    def build_inputs(self):
        img = self.rob.get_image_front()
        masked_red = red_mask(img)
        masked_green = green_mask(img)
        vals = np.array([
            *get_irs_sensors(self.rob),
            *detect_objects(masked_red),
            *detect_objects(masked_green),
            *gripper(self.rob),
        ], float)

        return np.nan_to_num(vals)
