# This is a basic neural network created using tensorflow

import numpy as np
from tensorflow import keras
# Creating first NN
model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

## Here y = 2x -1
xs = np.array([-1.0, 0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0 ], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 13.0, 15.0 ], dtype=float)

model.fit(xs, ys, epochs = 500)

# Now lets predict what will be the value of y for x=10
model.predict([10.0])