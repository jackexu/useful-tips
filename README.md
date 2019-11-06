# useful-tips

For Mac user with latest macOS Majave - 10.14 version

# **Python**

### Set alias for python and pip
open bash_profile by running `nano /.bash_profile`
add following
```
alias python='python3'
alias pip='pip3'
```
then use control+X to exit and type Enter twice to save it.

### How to install tensorflow on Python 3.7:
```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
```

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

Use Brew install libomp.

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
delete following in the bash profile and then "control+x", then type "y", then "enter"
```
# added by Anaconda3 5.2.0 installer
export PATH="/Users/ody/anaconda3/bin:$PATH"
```
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
