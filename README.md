# Solution for uncommon bugs in Python and R 

**Data Science Coding**

For Mac user with latest macOS Majave - 10.14 or higher version

# **Python**

## Python settings problem

### Set alias for python and pip

First, check if you are using bash or zsh: `echo $0`

Second, add following to the corresponding bash profile bewlow
```
alias python='python3'
alias pip='pip3'
```
then use control+X to exit and type Y/Enter twice to save it.

#### For zsh (default in macOS Catalina)
open profile by running `nano ~/.zshrc`

#### For bash (default in macOS 10.14 and before)
open bash_profile by running `nano ~/.bash_profile`

### How to Suppress warnings in Python:
```
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
```

### How to Suppress Tensorflow warnings:
#### For warning like "Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA"
```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
```
#### For Tensorflow deprecated warnings:
```
import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
```

## Python common installation problem

### Unable to install xgboost 

Common xgboost installation issue:

```
XGBoostLibraryNotFound: Cannot find XGBoost Library in the candidate path, did you install compilers and run build.sh in root path?
    List of candidates:
    ...
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

Solution to above is using brew install first and then manually build the package

```
brew install xgboost
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
mkdir lib
cd lib
ln -s /usr/local/Cellar/xgboost/0.90/lib/libxgboost.dylib ./libxgboost.dylib
cd ../python-package
python3 setup.py install
```

### How to install tensorflow on Python 3.7:
```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
```

### Unable to install Keras on Python 3.8 - looks like they solved now
Error meassage like below is due to unupdated h5py package (they haven't make any update for 3.8)
```
error: dlopen(libhdf5.dylib, 6): image not found
```
Solution is to build this package manually: Download the file from [wheels.scipy.org](wheels.scipy.org), cd to Download folder and run below
```
pip install h5py-2.10.0-cp38-cp38-macosx_10_9_x86_64.whl
```

## Python common issues 

### XCRUN error or command 'gcc' failed:
Sample error:
```
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
  error: command 'gcc' failed with exit status 1
```
Please run `xcode-select --install` in terminal

### If encounter SSL certificate problem
Error like when using Keras Mnist dataset:
```
Exception: URL fetch failure on https://s3.amazonaws.com/img-datasets/mnist.npz : None 
-- [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)
```
Go to Finder -> Go -> Go to Folder -> Type "/Applications/Python 3.7" -> Double click "Install Certificates.command" to run.

### OpenMP issue
Error like *It seems that scikit-learn cannot be built with OpenMP support.* or
```
    compile options: '-c'
    extra options: '-fopenmp'
    gcc: test_openmp.c
    clang: error: unsupported option '-fopenmp'
```

Use *brew install libomp* and add following into bash_profile
```
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
export CPPFLAGS="$CPPFLAGS -Xpreprocessor -fopenmp"
export CFLAGS="$CFLAGS -I/usr/local/opt/libomp/include"
export CXXFLAGS="$CXXFLAGS -I/usr/local/opt/libomp/include"
export LDFLAGS="$LDFLAGS -Wl,-rpath,/usr/local/opt/libomp/lib -L/usr/local/opt/libomp/lib -lomp"
```

### Unable load model in Flask for Tensorflow 2.0 and Keras 2.3
Error meassage like below will cuase a *HTTP 500 Internal Server Error* when apply model in Flask
```
AttributeError: '_thread._local' object has no attribute 'value'
```
Solution is to use below; instead of *import from Keras.models*
```
from tensorflow.keras.models import load_model
```

## Python IDE problem

### How to remove Anaconda3 completely
1. remove config
```
conda install anaconda-clean
anaconda-clean --yes
```
2. remove Anaconda and backup
```
rm -rf ~/anaconda3
rm -rf ~/.anaconda_backup
```
3. remove from bash profile

open bash profile by using following command
```
nano ~/.bash_profile
```
delete following in the bash profile
```
# added by Anaconda3 5.2.0 installer
export PATH="/Users/ody/anaconda3/bin:$PATH"
```
then "control+x", then type "y", then "enter"

4. remove hidden files
```
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-client.bom
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-client.plist
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-navigator.bom
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-navigator.plist
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-project.bom
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda-project.plist
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda.bom
rm -rf ~/Library/Receipts/io.continuum.pkg.anaconda.plist
rm -rf ~/.condarc ~/.conda ~/.continuum
```

### How to remove PyCharm completely
1. Configuration (idea.config.path):
```
~/Library/Preferences/<PRODUCT><VERSION>
```
  
2. Caches (idea.system.path):
```
~/Library/Caches/<PRODUCT><VERSION>
```
  
3. Plugins (idea.plugins.path):
```
~/Library/Application Support/<PRODUCT><VERSION>
```
  
4. Logs (idea.log.path):
```
~/Library/Logs/<PRODUCT><VERSION>
```

# **R**

### If encounter rJava error in R, try following command; if not working, update java then retry
```
sudo R CMD javareconf
```

### If encounter error like "# include <stdlib.h> when install any package in R" 
1. install xcode in terminal
```
install xcode-select
```
2. If you already have xcode installed (receive below message after run above command)
```
error: command line tools are already installed, use "Software Update" to install updates
```
then run following command (for macOS Mojave - 10.14), and install. 
```
open /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg
```
It may happen again everytime you update your system.

# **HomeBrew**

### How to install brew
```
rm -rf /usr/local/Cellar /usr/local/.git
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### Have permission error when using brew

run following command to fix:
```
sudo install -d -o $(whoami) -g admin /usr/local/Frameworks
```
### Install GraphViz

```
brew install graphviz
```
# **Install Gym**
sometimes couldn't run `pip intsall gym[all]`

### *Solution 1*
run `pip install gym[atari]` instead

### *Solution 2*
Install MuJoCo first (not recommended unless have to install gym[all]) then install it. Run following, and restart terminal after every step, 

#### Download MuJoCo files
Download "mujoco200_macos.zip" from https://www.roboti.us/index.html and rename to "mujoco200.zip".
Unzip it to the directory:
```
unzip mujoco200.zip -d ~/.mujoco/
```
#### Get the key file:

Go to https://www.roboti.us/license.html, and download file "getid_osx.dms" for mac.
Running following to get the computer id:
```
chmod 755 getid_osx.dms
./getid_osx.dms
```
Then copy Your MuJoCo computer id to the web and submit - get the "mjkey.txt" and move it by running
```
mv mjkey.txt ~/.mujoco/
```
#### Install MuJoCo
```
pip3 install -U 'mujoco-py<2.1,>=2.0'
```
If not working, run:
```
git clone https://github.com/openai/mujoco-py
cd mujoco-py
pip install -e . --no-cache
```
#### Install gym[all] again
```
pip3 install gym[all]
```
Also, you might need `brew install gcc` in order to install it.

# **RCC**
login method for midway 2 or Hadoop
```
ssh -Y <user>@midway2.rcc.uchicago.edu
ssh -Y <user>@hadoop.rcc.uchicago.edu
```

Find/change enviorment and install package
```
module avail python
module load Anaconda3/2019.03 
pip install --user seaborn
```

Run sbatch file and check job status
```
sbatch run.sbatch
squeue --user=<username>
