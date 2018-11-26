# useful-tips

##### How to install tensorflow on Python 3.7:
```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.8.0-py3-none-any.whl
```
##### How to remove Anaconda3
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
3. remove from bash file
```
nano ~/.bash_profile
```
delete following and then "control+x", then type "y", then "enter"
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
