import numpy as np

class PerturbationVector(np.ndarray):

    def find_zero_elements(self):
        return [i for i, e in enumerate(self) if e == 0.0]


x = PerturbationVector(shape=(4,), buffer=np.array([1.0,0.0,0.0, 4.0]), dtype=float)

print x.find_zero_elements()
