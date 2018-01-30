# Deep Learning Workshop

## Expectations

- learn the basic concepts of deep learning
- learn the general structure of neural networks
- learn the general structure of convolution neural networks
- achieve auc 0.85 on KKTV Data Game 17.11

# Installation

* python 2.7
* virtualenv (if you don't know what virtualenv is, you definitely need it.)
* clone this repo
* `cd datateam_workshop_dl`
* `virtualenv venv` (-p /path/to/python2 if it's python3)
* `source venv/bin/activate`
* `pip install jupyter`
* `pip install tensorflow` or `pip install tensorflow-gpu` if you have gpu
* `pip install keras`
* `pip install matplotlib`
* `pip install scipy`
* `pip install sklearn`
* `pip install git+https://www.github.com/keras-team/keras-contrib.git`
* download datasets:
  - ./datasets/v0_eigens.npz
  - ./datasets/sample.png
  - ./datasets/inception.png
* `jupyter notebook`
* explore the notebooks in your browser.

# Source Code

- 00_requirements.ipynb : run all cells to meet all requirements.
- 01_tensors.ipynb : tensor basics.
- 02_handicrafts.ipynb : a handcrafted shallow neural network.
- 03_dense.ipynb : basic neural networks on keras.
- 04_convolution.ipynb : what convolution neural network is.
- 05_convnet.ipynb : basic convolutional neural networks on keras.


# Before the Workshop

- clone the repo and install everything.
- make sure all cells in 00_requirements.ipynb work fine.
- join the workshop competition on kaggle.
- try to understand 01_tensors.ipynb before the workshop (optional).
