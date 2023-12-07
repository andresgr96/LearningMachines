
import numpy as np


class Controller(object):
    def control(self):
        action1 = np.random.choice([-10, 10])
        action2 = np.random.choice([-10, 10])

        return [action1, action2]
