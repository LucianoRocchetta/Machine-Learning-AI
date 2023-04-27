#Check Fibonacci with Artificial Intelligence

import tensorflow as tf;
import numpy as npy;

numbers = npy.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], dtype = int);
fibonacci_serie = npy.array([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], dtype = int)

layer = tf.keras.layers.Dense(units = 1, input_shape = [1]);
model = tf.keras.Sequential([layer]);

def training_model (input, output):
    model.compile(
        optimizer = tf.keras.optimizers.Adam(0.1),
        loss = "mean_squared_error",
    )
    
    history = model.fit(input, output, epochs = 2000, verbose = False);
    print("Model Trained!");

def check_value (value):
    result = int(model.predict([value]));
    print("The next number is: " + str(result));


training_model(numbers, fibonacci_serie);
user_value = 1;

while user_value != 0:
    user_value = int(input("Enter a number from Fibonacci series: "))
    check_value(user_value)
