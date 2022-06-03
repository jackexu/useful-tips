# Install Python 3.9.13

Run codes 
```
sudo apt update && sudo apt upgrade
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.9 -y
python3.9 --version
sudo apt install python3.9-dev -y
sudo apt install python3.9-venv -y
sudo apt install python3.9-distutils -y
sudo apt install python3.9-lib2to3 -y
sudo apt install python3.9-gdbm -y
sudo apt install python3.9-tk -y
sudo apt install python3.9-apt -y
```

## Set Python 3.9.13 as default
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2

sudo update-alternatives --config python3
```

## apt_pkg issue
fix 'ModuleNotFoundError: No module named 'apt_pkg'
```
ll cd /usr/lib/python3/dist-packages/apt_pkg.cpython*
# Copy from output above
sudo ln -s apt_pkg.cpython-{your-version-number}-x86_64-linux-gnu.so apt_pkg.so
```

# Install pip
In `~/.bashrc` add `export PATH="/usr/local/bin:$PATH"`

Then do `sudo apt install python3-pip`

Then log out then log back in

Then run `pip3 install pipenv`
