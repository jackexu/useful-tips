# Install Python 3.9.13

Recommend Manual Way
```
sudo apt update && sudo apt upgrade

wget https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tar.xz

tar -xf Python-3.9.13.tar.xz

sudo mv Python-3.9.13 /opt/

sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev pkg-config make -y

cd /opt/Python-3.9.13/

./configure --enable-optimizations --enable-shared

make

sudo make altinstall

cd && sudo ldconfig /opt/Python-3.9.13

python3.9 --version
```

## Set Python 3.9.13 as default
```
sudo update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.9 1

sudo update-alternatives --config python3
sudo update-alternatives --config python
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
