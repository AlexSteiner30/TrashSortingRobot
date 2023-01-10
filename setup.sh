# Raspberry Pi Setup
sudo apt update
sudo apt upgrade

# Install pip3
sudo apt install python3-pip

sudo apt install libatlas-base-dev

pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.9.0-py3-none-any.whl

# Check if tenserflow was installed
pip3 show tensorflow