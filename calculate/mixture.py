import numpy as np


class Mixture:
    def __init__(self, composition, T):
        self.import_constants()
        self.x_i = np.array([composition])
        self.T = T
        self.y_i = self.estimate_y_i()
        self.p = self.estimate_p()
        self.Tr = self.calc_Tr()
        self.a_i = self.calc_ai()
        self.b_i = self.calc_bi()

    def import_constants(self):
        self.Tc = np.genfromtxt('properties\critical_temperature.csv', delimiter=',')
        self.Pc = np.genfromtxt('properties\critical_pressure.csv', delimiter=',')
        self.w = np.genfromtxt('properties/accentric_factor.csv', delimiter=',')
        self.k_ij_alpha = np.genfromtxt('properties/alpha.csv', delimiter=',')
        self.components = np.genfromtxt('properties\components.csv', delimiter=',')

    def estimate_y_i(self):
        pass

    def estimate_p(self):
        pass

    def calc_Tr(self):
        pass

    def calc_ai(self):
        pass

    def calc_bi(self):
        pass
