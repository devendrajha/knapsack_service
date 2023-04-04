from app.custom_errors.insufficien_data_found_exception import InsufficientDataFound, BothListSizesNotMatch
from app.service.knapsack_optimizer_interface import IKnapsackOptimizer


class KnapsackOptimizer(IKnapsackOptimizer):

    def __init__(self, vo):
        self.tmp_2d_array = []
        self.vo = vo

    def optimize_maximum(self) -> float:

        if len(self.vo.weight) != len(self.vo.values):
            raise BothListSizesNotMatch("both list data should be same length")
        if len(self.vo.weight) == len(self.vo.values) == 0:
            raise InsufficientDataFound("both list are empty")

        c_size = self.vo.container
        number_of_items = len(self.vo.weight)
        self.tmp_2d_array = [[-1 for i in range(c_size + 1)] for j in range(number_of_items + 1)]
        return self.knapsack(self.vo.weight, self.vo.values, c_size, number_of_items)

    def knapsack(self, weight_list: list, value_list: list, container, number_of_items)-> float:
        if number_of_items == 0 or container == 0:
            return 0
        if self.tmp_2d_array[number_of_items][container] != -1:
            return self.tmp_2d_array[number_of_items][container]

        if weight_list[number_of_items - 1] <= container:
            self.tmp_2d_array[number_of_items][container] = max(
                value_list[number_of_items - 1] + self.knapsack(
                    weight_list, value_list, container - weight_list[number_of_items - 1], number_of_items - 1),
                self.knapsack(weight_list, value_list, container, number_of_items - 1))
            return self.tmp_2d_array[number_of_items][container]
        elif weight_list[number_of_items - 1] > container:
            self.tmp_2d_array[number_of_items][container] = self.knapsack(weight_list, value_list, container,
                                                                          number_of_items - 1)
            return self.tmp_2d_array[number_of_items][container]
