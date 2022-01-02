# __Week 4__ of Introduntion to Tensorflow.

In this week we will learn how to apply the neural networks to the real world dataset. It is often easy for the neural networks to train for the data let's say, for a convolutional Neural Network it is easy if the image present in the dataset is centered and the resolution is low eg: 28 x 28. But what if the images aren't grayscale and the size of the image is in mega pixels and the dataset images are not centered, here comes the real world challenge and in this week we will be learning how to cope up with the real world challenges when applying the neural networks.

## ImageGenerator

The ImageGenerator is pulls the images from the file system and feeds them into the neural network for training.
Data augmentation is an approach for increasing the amount of data by employing techniques such as cropping, padding, flipping, and so on.
Data augmentation makes the model more resistant to minor alterations, preventing it from overfitting.
It is neither practicable nor efficient to store the augmented data in memory, which is where Keras' ImageDataGenerator class (also included in TensorFlow's high level API: tensorflow.keras) comes in. ImageDataGenerator creates tensor image data in batches with real-time data augmentation. And the best thing is... It only takes one line of code!

Also, the generator's output images will have the same output dimensions as the input photos.

Reference : [ImageDataGenerator in TensorFlow](https://towardsdatascience.com/exploring-image-data-augmentation-with-keras-and-tensorflow-a8162d89b844)