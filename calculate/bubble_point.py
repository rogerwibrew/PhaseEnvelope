import calculate.peng_robinson as pr
import numpy as np


def calc_bubble_point(mixture):
    pressure = estimate_pressure()
    liquid_fugacity = pr.calc_fugacity(mixture, pressure)
    mixture.y_i = estimate_vapour_composition()
    while True:
        while True:
            vapour_fugacity = pr.calc_fugacity(mixture, pressure, liquid=False)
            y_i_new = mixture.xi * liquid_fugacity / vapour_fugacity
            if check_tolerance():
                break
            else:
                mixture.yi = y_i_new
        if check_yi_sum():
            break
        else:
            mixture.P = mixture.P(np.sum(mixture.y_i))


def estimate_pressure():
    pass


def estimate_vapour_composition():
    pass


def check_tolerance():
    pass


def check_yi_sum():
    pass
