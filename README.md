![University at Buffalo](http://www.nsm.buffalo.edu/Research/mcyulab//img/2-line_blue_gray.png)

***
# Identification of Handwritten digit images using different classification algorithms such as Multi-class Logistic Regression, Single Hidden Layer Neural Network and Convolutional Neural Network.

## Project Summary
***
We have trained our classification model on MNIST data using Multi-classLogistic Regression, Single Hidden Layer Neural Network, Convolutional Neural Network and predicted the labels of the digit images in both MNIST and USPS digit dataset.
### Logistic Regression:
  * We trained the model and tuned the hyperparameter i.e. learning rate, by using our own implementation of Logistic regression, we achieved an accuracy of 91.56% on MNIST test images and 45.15% on USPS test images at learning rate of 0.14 and lambda (regulariser) value of 0. 
  * Using tensorflow, we have achieved an accuracy of 92.41% on MNIST test images and 48.32% on USPS test images
### Single hidden layer neural network:
  * We trained the model and tuned the hyperparameter i.e. learning rate and number of units in hidden layer, we achieved an accuracy of 97.76% on MNIST test images and 64.6% on USPS test images.
### Convolutional Neural Network:
  * On training the model using CNN, we achieved an accuracy of 99.18% on MNIST test images and 75% on USPS test images.
### No Free Lunch theorem remains valid:
  * Accuracies of the models on the USPS data were way lower than the accuracies they gave for the MNIST dataset. After seeing such performance of all the three training models on the USPS data set which were trained on the MNIST data set we can conclude that our model is not the best in the general way but performs well on the dataset in which it was trained. Our model needs to have the training knowledge of the USPS data in order to perform well on the USPS data set.

## Approach
***
### Logistic Regression
* MNIST dataset files were downloaded from the website mentioned in the main.pdf have been read using the gzip library function of the python with the help of direction mentioned in this [website](https://martin-thoma.com/classify-mnist-with-pybrain/).
* Train and Test Images were then flattened into 2D numpy array, N x 784 size.
* Train image data and Test image data have been then standardised with zero mean and unit standard deviation.
* Previous two steps were performed similarly on the USPS test data.
* Weight numpy array was generated valus of 1s and dimension of K x D, where K is the number of classes i.e., 10 and D is the number of data features plus 1 bias feature i.e., (784 + 1).
* Column of 1s was added as the first column to both Train set and the Test sets of MNIST and USPS data making the total feature dimension of 785
* One hot vectors of MNIST data labels and USPS data labels were created.
* Separate functions for calculating the **Cross Entropy error**, **Gradient descent**, **Softmax**, and **Predicting** the image labels were created in the LRlibs.py file.
  * **Cross Entropy error** function was implemented as per the formula.
  * **Gradient descent** function was done using the pseudo code mentioned in the document provided along with the Project 3
  * **Softmax** function was implemented using the exp(x − max(x))/Σexp(x) formula.
  * **Predict** function was implemented by returning the column which had max of the W.dot(X) in each row.
* Model was trained on the Training data images with epoch count of 200
and varying learning rate of 0.01 to 0.14. ​The accuracies and the cross
entropy error have been tabulated in the tables 1.1 and 1.2 for both MNIST
and USPS data sets.
### Single Hidden Layer Neural Network
* This has been implemented using TensorFlow
* The model consists of one hidden layer and one output layer
* In hidden layer, we have initialized 784x1024 weights and 1024 bias for 1024 units by random values. Then, multiplied the input with the weights and added bias to it. On this value, applied ReLU activation function.
* The output of hidden layer is fed to the output layer. The output layer consists of 1024x10 weights and 10 bias for 10 units in this layer and are randomly initialized.
* The output of the model is obtained by multiplying these weights with output from hidden layer and adding bias of output layer. Output will be a one-hot representation of the predicted label
* We have trained the above model using AdamOptimizer with number of epochs = 20000 and input batch size = 50 in each epoch and chose that model which has the minimum cross-entropy error 
* We have tuned the hyperparameters such as number of units in hidden layer (784, 864, 944, 1024) and learning rate (0.01 to 0.05) and chose the model which has maximum accuracy on validation set
* Then, ran the model on MNIST and USPS test data to get test accuracy.
### Convolutional Neural Network
* This is also implemented using TensorFlow 
* The model consists of 4 layers: Convolution layer 1 (convolution with 32 features applied on 5x5 patch of image + 2D max pooling), convolution layer 2 (convolution with 64 features applied on 5x5 patch of image + 2D max pooling), fully connected layer with 1024 neurons and ReLU activation function, logit layer with 10 neurons corresponding to 10 labels.
* In fully connected layer, few neuron outputs are dropped out to prevent overfitting. The no_drop_prob placeholder makes sure that dropout occurs only during training and not during testing.
* Trained the model using AdamOptimizer with learning rate set to 1e-4 and number of epochs= 20000 on input batches of size 50 and chose that model which has the minimum cross-entropy error.
* Then, ran the model on MNIST and USPS test data to get test accuracy. USPS test set was divided.
* No need of tuning of hyperparameter in CNN.
### USPS data extraction:
* While extracting USPS image features, we have to make it resemble to the MNIST image features as close as possible so that our trained model can classify the images correctly.
* In order to do that, we followed below steps:
  * Resized the image to square shape i.e. width = height = max(width, height) it was done in such a way that the aspect ratio of the digits was not skewed.
  * Converted the image into grayscale.
  * Inverted the image pixels value, that is 255 - Image, black became white and vice-versa so has to follow same pixels values that of the MNIST images.
  * Resized the each image to 28x28
  * Normalized the image pixels with ([value-min]/[max-min]) formula
  * Flattened each image into 1x784 numpy array
  
 

## Results
***
### Logistic Regression
**Hyperparameters = learning_rate**

<table class="tableizer-table">
<thead><tr><td colspan=3><b>At epoch count = 200</b></td><td colspan=3><b>MNIST</b></td><td><b>USPS</b></td></tr></thead>
<thead><tr><th>Sr.</th><th>Learning_Rate</th><th>Regulariser</th><th>Training (%)</th><th>Val (%)</th><th>Test (%)</th><th>Test (%)</th></tr></thead><tbody>
 <tr><td>1</td><td>0.01</td><td>1</td><td>84.87</td><td>88.48</td><td>85.94</td><td>40.33</td></tr>
 <tr><td>2</td><td>0.02</td><td>1</td><td>84.925</td><td>88.54</td><td>85.98</td><td>40.39</td></tr>
 <tr><td>3</td><td>0.01</td><td>0</td><td>87.16</td><td>90.06</td><td>87.85</td><td>41.26</td></tr>
 <tr><td>4</td><td>0.02</td><td>0</td><td>88.87</td><td>91.36</td><td>89.3</td><td>41.95</td></tr>
 <tr><td>5</td><td>0.03</td><td>0</td><td>89.47</td><td>91.96</td><td>89.94</td><td>42.56</td></tr>
 <tr><td>6</td><td>0.04</td><td>0</td><td>89.94</td><td>92.32</td><td>90.39</td><td>42.96</td></tr>
 <tr><td>7</td><td>0.05</td><td>0</td><td>90.2</td><td>92.58</td><td>90.59</td><td>43.35</td></tr>
 <tr><td>8</td><td>0.06</td><td>0</td><td>90.49</td><td>92.68</td><td>90.82</td><td>43.6</td></tr>
 <tr><td>9</td><td>0.07</td><td>0</td><td>90.7</td><td>92.7</td><td>90.88</td><td>43.94</td></tr>
 <tr><td>10</td><td>0.08</td><td>0</td><td>90.88</td><td>92.78</td><td>90.98</td><td>44.18</td></tr>
 <tr><td>11</td><td>0.09</td><td>0</td><td>91.02</td><td>92.86</td><td>91.12</td><td>44.4</td></tr>
 <tr><td>12</td><td>0.1</td><td>0</td><td>91.15</td><td>92.9</td><td>91.22</td><td>44.51</td></tr>
 <tr><td>13</td><td>0.11</td><td>0</td><td>91.25</td><td>92.98</td><td>91.35</td><td>44.65</td></tr>
 <tr><td>14</td><td>0.12</td><td>0</td><td>91.37</td><td>93.1</td><td>91.4</td><td>44.84</td></tr>
 <tr><td>15</td><td>0.13</td><td>0</td><td>91.48</td><td>93.22</td><td>91.5</td><td>45.05</td></tr>
 <tr><td>16</td><td>0.14</td><td>0</td><td>91.54</td><td>93.3</td><td>91.56</td><td>45.15</td></tr>
 <tr><td>17</td><td>0.15</td><td>0</td><td>91.62</td><td>93.38</td><td>91.55</td><td>45.32</td></tr>
</tbody></table>

### Single Hidden Layer Neural Network
**Hyperparameters = number of units in hidden layer, learning_rate**

<table>
<thead><tr><td colspan=3><b>With epoch_count = 20000 and batch_size = 50</b></td><td colspan=3><b>MNIST</b></td><td><b>USPS</b></td></tr></thead>
<thead><tr><th>Sr.</th><th>Number of units in hidden layer</th><th>Learning Rate</th><th>Training (%)</th><th>Val (%)</th><th>Test (%)</th><th>Test (%)</th></tr></thead><tbody>
 <tr><td>1</td><td>784</td><td>0.01</td><td>99.27</td><td>97.42</td><td>97.35</td><td>63.18</td></tr>
 <tr><td>2</td><td>784</td><td>0.02</td><td>97.93</td><td>96.58</td><td>96.01</td><td>61.63</td></tr>
 <tr><td>3</td><td>784</td><td>0.03</td><td>95.08</td><td>94.32</td><td>93.87</td><td>56.88</td></tr>
 <tr><td>4</td><td>784</td><td>0.04</td><td>93.37</td><td>93.08</td><td>92.4</td><td>54.64</td></tr>
 <tr><td>5</td><td>784</td><td>0.05</td><td>88.87</td><td>88.42</td><td>88.37</td><td>47.09</td></tr>
 <tr><td>6</td><td>864</td><td>0.01</td><td>99.33</td><td>97.6</td><td>97.46</td><td>65.25</td></tr>
 <tr><td>7</td><td>864</td><td>0.02</td><td>97.36</td><td>95.32</td><td>95.77</td><td>59.63</td></tr>
 <tr><td>8</td><td>864</td><td>0.03</td><td>95.72</td><td>94.82</td><td>94.09</td><td>56.85</td></tr>
 <tr><td>9</td><td>864</td><td>0.04</td><td>92.08</td><td>91.16</td><td>90.94</td><td>52.24</td></tr>
 <tr><td>10</td><td>864</td><td>0.05</td><td>91.07</td><td>90.2</td><td>90.46</td><td>49.24</td></tr>
 <tr><td>11</td><td>944</td><td>0.01</td><td>99.13</td><td>97.74</td><td>97.47</td><td>64.2</td></tr>
 <tr><td>12</td><td>944</td><td>0.02</td><td>97.9</td><td>96.74</td><td>96.12</td><td>61.74</td></tr>
 <tr><td>13</td><td>944</td><td>0.03</td><td>95</td><td>94.16</td><td>93.8</td><td>56.89</td></tr>
 <tr><td>14</td><td>944</td><td>0.04</td><td>92.39</td><td>92.12</td><td>91.07</td><td>50.29</td></tr>
 <tr><td>15</td><td>944</td><td>0.05</td><td>91.67</td><td>91.3</td><td>91.09</td><td>50.27</td></tr>
 <tr><td>16</td><td>1024</td><td>0.01</td><td>99.25</td><td>97.52</td><td>97.81</td><td>64.6</td></tr>
 <tr><td>17</td><td>1024</td><td>0.02</td><td>97.6</td><td>96.2</td><td>95.57</td><td>59.59</td></tr>
 <tr><td>18</td><td>1024</td><td>0.03</td><td>95.46</td><td>94.2</td><td>94.16</td><td>54.95</td></tr>
 <tr><td>19</td><td>1024</td><td>0.04</td><td>90.61</td><td>90.38</td><td>89.97</td><td>52.33</td></tr>
 <tr><td>20</td><td>1024</td><td>0.05</td><td>89.56</td><td>89.08</td><td>88.83</td><td>49.46</td></tr>
</tbody></table>

#### Logistic Regression
Output for Learning rate 0.07
Current learning rate is 0.070000
<blockquote>
iteration 0/200: loss 2.303 </br>
iteration 10/200: loss 0.759 </br>
iteration 20/200: loss 0.583 </br>
iteration 30/200: loss 0.509 </br>
iteration 40/200: loss 0.468 </br>
iteration 50/200: loss 0.440 </br>
iteration 60/200: loss 0.421 </br>
iteration 70/200: loss 0.406 </br>
iteration 80/200: loss 0.394 </br>
iteration 90/200: loss 0.384 </br>
iteration 100/200: loss 0.376 </br>
iteration 110/200: loss 0.369 </br>
iteration 120/200: loss 0.362 </br>
iteration 130/200: loss 0.357 </br>
iteration 140/200: loss 0.352 </br>
iteration 150/200: loss 0.348 </br>
iteration 160/200: loss 0.344 </br>
iteration 170/200: loss 0.341 </br>
iteration 180/200: loss 0.338 </br>
iteration 190/200: loss 0.335 </br>
training set Accuracy is 0.907055 </br>
validation set Accuracy is 0.927000 </br>
Test set Accuracy is 0.908800 </br>
USPS set Accuracy is 0.439422
</blockquote>

#### Logistic Regression (using TensorFlow):
Output for learning rate 0.5, number of epochs: 10000
<blockquote>
The accuracy on MNIST test set: 92.41 </br>
The accuracy on USPS test set: 48.32 </br>
</blockquote>

#### Single Hidden Layer Neural Network:
Output for learning rate 0.01, number of epochs: 20000, number of units in hidden layer: 784
<blockquote>
MNIST validation accuracy: 97.42 </br>
MNIST test accuracy: 97.35 </br>
The accuracy on USPS test set: 63.18 </br>
</blockquote>

#### Convolutional Neural Network:
Output for learning rate 1e-4, number of epochs: 20000
<blockquote>
MNIST test accuracy: 99.18 </br>
The accuracy on USPS test set: 75.13 </br>
</blockquote>

## Documentation
***
Report and documentation can be found on this [Documentation](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/blob/master/Report/proj3.pdf) link

## Folder Tree
***
* [**Report**](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/tree/master/Report) contains summary report detailing our implementation and results.
* [**code**](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/tree/master/code)  contains the source code of our machine learning algorithm
* [**Materials**](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/tree/master/Materials) contains the project related informative materials
* [**Bonus**](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/tree/master/Bonus) contains source code of our machine learning algorithm using back-propogation.
* [**proj3_images**](https://github.com/swatishr/classification-using-logistic-regression-and-single-layer-neural-network/tree/master/proj3_imagest) contains image data for training, validation and testing

### Code outline
#### code:
* **logistic_main.py:** Run this file for execution of logistic regression model without using tensorflow
* **logistic_tensorflow_main.py:** Run this file for execution of logistic regression model using tensorflow. It creates the model, trains it, tests it on MNIST validation, test set and USPS test set
* **single_layer_NN_main.py:** Run this file for execution of single hidden layer NN model using tensorflow. It creates the model, trains it, tests it on MNIST validation, test set and USPS test set
* **cnn_main2.py:** Run this file for execution of CNN model using tensorflow. It creates the model, trains it, tests it on MNIST validation, test set and USPS test set
* **libs.py:**
  * **read_gz(images,labels):** To read MNIST gz data
  * **view_image(image, label=""):** to view single image from the MNSIT data
  * **yDash(trains_images, W):** for performing the W.dot(X)
  * **softmax(x):** for calculating the softmax of each row in W.dot(X)
  * **sgd(W, train_images, T, L2_lambda, epochNo, learning_rate):** gradient descend for optimising the weights
  * **cross_entropy(W, X, T, L2_lambda):** cacluating the loss in the model
  * **predict(W, X):** predicting the labels from the output of the model
* **single_layer_NN_lib.py:**
  * **create_single_hidden_layer_nn(number_hidden_units)**: create input layer,
one hidden layer with specified number of neurons and output layer
* **cnn_lib.py:**
  * **weight_init(shape):** Initialize weight variables
  * **bias_init(shape)**: Initialize bias variables
  * **convolution(x, W)**: convolves input with given weights and stride 1 and with zero padding
  * **maxpool(x)**: performs max pooling on window size of 2x2 and stride of 2 with zero padding
* **USPS_data_extraction.py:**
  * **make_square(im):** To make the image with equal height and width
  * **extract_usps_data():** Get USPS test images and labels. Usps_test_images is a Nx784 numpy array and Usps_test_labels is Nx10 numpy array (one-hot representation)
  
#### Bonus:This zip folder consists of implementation of Single Hidden Layer NN model using backpropagation
* **main.py:** Run this file for execution of single hidden layer NN model using back propogation. It creates the model, trains it, tests it on MNIST validation, test set and USPS test set
* **SNlibs.py:**
  * **read_gz(images,labels):** To read MNIST gz data
  * **view_image(image, label=""):** to view single image from the MNSIT data
  * **softmax(x):** for calculating the softmax of each row in W.dot(X)
  * **calculate_loss(model, X,y, reg_lambda):** Helper function to evaluate the total loss on the dataset 
  * **cross_entropy(W, X, T, L2_lambda):** cacluating the loss in the model
  * **predict(W, X):** predicting the labels from the output of the model
  * **build_model(nn_hdim, num_passes, X, y, reg_lambda, learning_rate, T):** This function learns parameters for the neural network and returns the model
* **USPS_data_extraction.py:**
  * **make_square(im):** To make the image with equal height and width
  * **extract_usps_data():** Get USPS test images and labels. Usps_test_images is a Nx784 numpy array and Usps_test_labels is Nx10 numpy array (one-hot representation)

  
## Instructor
***
  * **Prof. Sargur N. Srihari**
  
## Teaching Assistants
***
  * **Jun Chu**
  * **Tianhang Zheng**
  * **Mengdi Huai**

## References
***
  * [Stackoverflow.com](Stackoverflow.com)
  * Python, Numpy and TensorFlow documentations
  * [https://cs231n.github.io/convolutional-networks/](https://cs231n.github.io/convolutional-networks/)
  * [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
  * [https://martin-thoma.com/classify-mnist-with-pybrain/]/(https://martin-thoma.com/classify-mnist-with-pybrain/)

## License
***
This project is open-sourced under [MIT License](http://opensource.org/licenses/MIT)
