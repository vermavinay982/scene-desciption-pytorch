pytorch based captopn generator using attention encoder and LSTM

torch is used to create the neural network
torchvision is used for transformations in image before training

skimage again for transform 
scipy for reading image and resizing it

device = torch.device('cuda' if torch.cuda.is_avaialable() else 'cpu')

this will select one word from cuda or cpu and assign it to the variable device - that decides where the weights or the data to train should go

in pytorch - the dataset or the model both should be on the same device - either cuda or cpu 
if there is mismatch then it will throw an error

variable.to(device) will help in moving the data from one device to another 

## caption image beam search 
it takes encoder, decoder, image path (or we can make it take image as input), word_map and finally beam size 

encoder - model is used to move the image to a latent space with different dimensions of the data. It used hidden neural network layers that make the input change its shape and dimension.

decoder - encoder created a latent space, that particular latent space is taken as an input by the decoder that convert the image back to original dimension 

the role of encoder decoder is just to provide a latent space - why we need that? that space gives us flexibility to work with the data - remove noise from the data
converting to latent space will reduce some information and that means will keep the important features only from the input.
the final result in latent space consist of good features only that can be taken up for prediction easily 
the prediction would be faster due to less features
the noise will be removed
the autoencoder thus is used to remove the noise from images as it just focusses the important features of the input.

word map - it is just a map of words that are taken by LSTM to generate the output in sequence
 there are 9489 words in wordmap in a series and saved in JSON - java script object notation

beam_size - length or number of sequences to be considered at decode step - combining the 3 words to make a prediction

diction means saying - pre means before 


k = beam_size - 3
vocab size = len(word_map) - it is a json 
 

read the image - matrix form - ndarray 
convert image to RGB channel instead of RGBA 
the 4 channel will make the neural network disturb

if 4 channel 
	make it 3 by removing the alpha channel
if 3 channel 
	do nothing
if 2 channel 
	np.concatenate([img, img, img], axis=2)
	3 channel image is converted now


resize to (256, 256) square image
transpose to 2,0,1 - channel, height, width
normalize the image by 255
convert image and put to device - cuda or cpu

normalize the image again with respect to the prescribed mean and standard deviation

mean - average of the pixels in all 3 channels
std - deviation from mean in all 3 channels

transform the normalized image
unsqueeze
get latent space output
side of encoded value
view encoder
flatten


