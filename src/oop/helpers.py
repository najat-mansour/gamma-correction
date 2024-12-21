import random as rand
from enum import Enum

class Constants(Enum):
    MAX_GRAY_LVL = 255
    SCALING_FACTOR = 0.5
    MIN_GAMMA_VAL = 0.04
    MAX_GAMMA_VAL = 5  

class RandomNumberGenerator:
    @staticmethod
    def generate_random_number():
        while True:
            gamma = rand.uniform(Constants.MIN_GAMMA_VAL.value, Constants.MAX_GAMMA_VAL.value) 

            if gamma < 1:
                gamma = round(gamma, 2)
                return gamma

            elif gamma >= 2:
                gamma = int(gamma)
                return gamma