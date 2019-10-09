from utils.data_transforming import batch_gen
from datasources.lin_datagen import LinearDataGenerator

class BatchLoader(LinearDataGenerator):

    def __init__(self, ds_len, poly_order, test_split, bs, valid_split=0.1):
        super().__init__(ds_len, poly_order, test_split)
        print(">>>Batching train and validation sets...")

        self.bs = bs

        self.train_x = self._x[:int(len(self) - (len(self) * valid_split))]
        self.train_y = self._y[:int(len(self) - (len(self) * valid_split))]

        self.valid_x = self._x[int(len(self) - (len(self) * (valid_split))):]
        self.valid_y = self._y[int(len(self) - (len(self) * (valid_split))):]

    def _getloaders(self):
        return batch_gen(self.train_x, self.train_y, self.bs), batch_gen(self.valid_x,
                                                                               self.valid_y, self.bs)