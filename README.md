# Deep Learning Workshop

## Expectations

- learn the basic concepts of deep learning
- learn the general structure of neural networks
- learn the general structure of convolution neural networks
- achieve auc 0.85 on KKTV Data Game 17.11


# Installation

There are, at least, two ways confirmed to prepare and install your environment
for this workshop project. The 1st one is through the classical Virtualenv and Pip.
The 2nd is to leverage the new proposal of Python package management, Pipenv.

Oh, forgot to mention that the workshop is tested on Python 2.7.
We haven't examed it on Python 3, but you can try and let us know :)

## 1. Virtualenv & Pip

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

## 2. Pipenv

In this installation through pipenv, package *tensorflow* is installed,
instead of *tensorflow-gpu*. You can manually update the *Pipfile* before
running through the following steps then.

* install pipenv through the [official doc](https://docs.pipenv.org/install/).
* clone this repo
* `cd datateam_workshop_dl`
* `pipenv install jupyter tensorflow keras matplotlib scipy sklearn git+https://www.github.com/keras-team/keras-contrib.git#egg=keras-contrib`
* download datasets:
  - ./datasets/v0_eigens.npz
  - ./datasets/sample.png
  - ./datasets/inception.png
* `pipenv run jupyter notebook`
* explore the notebooks in your browser.

PS. Supposedly, it should be super easy to just run `pipenv install` with the *Pipfile* to take care of all installation.
Unfortunately, there is still some bug in pipenv such that in some environment, some dependency sub-packages wouldn't
get installed. Therefore, there is no lazy magic here, right now.
You can still try `pipenv install`. 
And if it didn't work, try the lousy and lengthy one provided in the above ;)


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
