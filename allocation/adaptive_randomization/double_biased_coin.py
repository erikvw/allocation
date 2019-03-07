import math
import random


class DoubleBiasedCoin(object):

    def __init__(self, control_success, control_trials,
                 treatment_success, treatment_trials,
                 control_name=None, treatment_name=None,
                 seed=None):
        if control_trials < control_success:
            raise ValueError('`control_trials` must be greater than or equal '
                             'to `control_success`')
        if treatment_trials < treatment_success:
            raise ValueError('`treatment_trials` must be greater than or equal '
                             'to `treatment_success`')

        self.control_name = control_name or "Control"
        self.treatment_name = treatment_name or "Treatment"

        self.seed = (seed + 10 * control_trials + treatment_trials
                     if seed else None)
        random.seed(seed)

        if control_trials > 1:
            self.p_c = float(control_success) / control_trials
        else:
            self.p_c = 0.5
        if treatment_trials > 1:
            self.p_t = float(treatment_success) / treatment_trials
        else:
            self.p_t = 0.5

    def minimize(self):
        cut = math.sqrt(self.p_c) / (math.sqrt(self.p_c) + math.sqrt(self.p_t))
        test = random.random()

        if test < cut:
            group = self.control_name
        else:
            group = self.treatment_name
        return group

    def urn(self):
        cut = (1 - self.p_t) / ((1 - self.p_t) + (1 - self.p_c))
        test = random.random()
        if test < cut:
            group = self.control_name
        else:
            group = self.treatment_name
        return group


def double_biased_coin_minimize(*args, **kwargs):
    dbc = DoubleBiasedCoin(*args, **kwargs)
    return dbc.minimize()


def double_biased_coin_urn(*args, **kwargs):
    dbc = DoubleBiasedCoin(*args, **kwargs)
    return dbc.urn()
