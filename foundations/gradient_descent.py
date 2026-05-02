class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        for x in range (iterations):
            d = 2 * init
            init = init - (learning_rate*d)
        return round(init,5)