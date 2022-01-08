# Quiz Week - 4


**1.Using Image Generator, how do you label images?**

- [x]  It’s based on the directory the image is contained in

- [ ]  You have to manually do it

- [ ]  It’s based on the file name

- [ ]  TensorFlow figures it out from the contents


**2.What method on the Image Generator is used to normalize the image?**

- [ ]  normalize_image

- [ ]  normalize

- [ ]  Rescale_image

- [x]  rescale


**3.How did we specify the training size for the images?**

- [ ]  The target_size parameter on the validation generator

- [ ]  The training_size parameter on the validation generator

- [ ]  The training_size parameter on the training generator

- [x]  The target_size parameter on the training generator


**4.When we specify the input_shape to be (300, 300, 3), what does that mean**

- [x]  Every Image will be 300x300 pixels, with 3 bytes to define color

- [ ]  There will be 300 horses and 300 humans, loaded in batches of 3

- [ ]  There will be 300 images, each size 300, loaded in batches of 3

- [ ]  Every Image will be 300x300 pixels, and there should be 3 Convolutional Layers


**5.If your training data is close to 1.000 accuracy, but your validation data isn’t, what’s the risk here?**

- [ ]  You’re overfitting on your validation data

- [ ]  No risk, that’s a great result

- [x]  You’re overfitting on your training data

- [ ]  You’re underfitting on your validation data


**6.Convolutional Neural Networks are better for classifying images like horses and humans because:**

- [x]  There’s a wide variety of horses

- [x]  There’s a wide variety of humans

- [x]  In these images, the features may be in different parts of the frame


**7.After reducing the size of the images, the training results were different. Why?**

- [ ]  The training was faster

- [ ]  There was less information in the images

- [x]  We removed some convolutions to handle the smaller images

- [ ]  There was more condensed information in the images