import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from .base import OptionPricingModel

class MonteCarloPricing(OptionPricingModel):
    def __init__(self, underlying_spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, number_of_simulations):
        self.S_0 = underlying_spot_price
        self.K = strike_price
        self.T = days_to_maturity
        self.r = risk_free_rate
        self.sigma = sigma

        self.N = number_of_simulations
        self.num_of_steps = days_to_maturity
        self.dt = self.T / self.num_of_steps

    def simulate_prices(self):
        np.random.seed(20)
        self.simulation_results = None

        S = np.zeros((self.num_of_steps, self.N))
        S[0] = self.S_0

        for t in range(1, self.num_of_steps):
            Z = np.random.standard_normal(self.N)
            S[t] = S[t-1] * np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + (self.sigma * np.sqrt(self.dt) * Z))

        self.simulation_results_S = S

    def _calculate_call_option_price(self):
        if self.simulation_results_S is None:
            return -1
        return np.exp(-self.r * self.T) * 1 / self.N * np.sum(np.maximum(self.simulation_results_S[-1] -self.K, 0))
    
    def _calculate_put_option_price(self):
        if self.simulation_results_S is None:
            return -1
        return np.exp(-self.r * self.T) * 1 / self.N * np.sum(np.maximum(self.K - self.simulation_results_S[-1], 0))
    
    def plot_simulation_results(self, num_of_movements):
        try:
            fig, ax = plt.subplots()
            # Example plotting code; replace with actual plotting logic
            ax.plot(self.simulation_results[:num_of_movements])
            ax.set_title('Monte Carlo Simulation Results')
            ax.set_xlabel('Simulations')
            ax.set_ylabel('Price')
            return fig
        except Exception as e:
            print(e)
            return None