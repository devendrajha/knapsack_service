class KnapsackVo:
    def __init__(self):
        self._values: list = []
        self._weight: list = []
        self._container: int = 0

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def container(self):
        return self._container

    @container.setter
    def container(self, container):
        self._container = container

    def __str__(self):
        return f"_weight_list {self._weight} | _values_list {self._values} | _container_size {self._container}"
