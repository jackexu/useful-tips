# useful-tips

### How to install tensorflow on Python 3.7:
```
pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl
```
### How to remove Anaconda3
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

### How to remove PyCharm
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
### How to install brew
```
rm -rf /usr/local/Cellar /usr/local/.git
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
### If encounter rJava error in R, try following command; if not working, update java then retry
```
sudo R CMD javareconf
```
