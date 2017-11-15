#data-loader.py
#loads the training , validation and test data from the MNIST data files
from struct import unpack
import gzip

# Third-party libraries
from numpy import zeros, uint8, float32
def read_gz():

	"""Read input-vector (image) and target class (label, 0-9) and return
	   it as list of tuples.
	"""
	# Open the images with gzip in read binary mode
	images = gzip.open('../MNIST-data/train-images-idx3-ubyte.gz', 'rb')
	labels = gzip.open('../MNIST-data/train-labels-idx1-ubyte.gz', 'rb')

	# Read the binary data

	# We have to get big endian unsigned int. So we need '>I'

	# Get metadata for images
	images.read(4)  # skip the magic_number
	number_of_images = images.read(4)
	number_of_images = unpack('>I', number_of_images)[0]
	rows = images.read(4)
	rows = unpack('>I', rows)[0]#28
	cols = images.read(4)
	cols = unpack('>I', cols)[0]#28

	# Get metadata for labels
	labels.read(4)  # skip the magic_number
	N = labels.read(4)
	N = unpack('>I', N)[0] #60000
	# print(number_of_images);

	if number_of_images != N:
	    raise Exception('number of labels did not match the number of images')

	# Get the data
	x = zeros((N, rows, cols), dtype=float32)  # Initialize numpy array #60000X28X28
	y = zeros((N, 1), dtype=uint8)  # Initialize numpy array
	for i in range(N):
	    # if i % 1000 == 0:
	        # print("i: %i" % i)
	    for row in range(rows):
	        for col in range(cols):
	            tmp_pixel = images.read(1)  # Just a single byte
	            tmp_pixel = unpack('>B', tmp_pixel)[0]
	            x[i][row][col] = tmp_pixel
	    tmp_label = labels.read(1)
	    y[i] = unpack('>B', tmp_label)[0]
	    # print(y.shape)#60000X1
	return (x, y)