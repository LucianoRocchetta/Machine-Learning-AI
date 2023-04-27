import tensorflow as tf;
import numpy as npy;

pesos_values = npy.array([230, 150, 540, 220, 843, 228, 391, 120, 98], dtype= float);
dolar_values = npy.array([1.17, 0.56, 2.74, 1.12, 4.28, 1.16, 1.99, 0.61, 0.50], dtype=float);

layer = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([layer]);

model.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = "mean_squared_error"
)

history = model.fit(pesos_values, dolar_values, epochs = 2000, verbose = False)
print("Model Trained!")

#Training values
initial_loop = 1;

while initial_loop != 0:
    initial_loop = float(input("Enter a number (Different to 0): "));
    result = model.predict([initial_loop]);
    print(result);
