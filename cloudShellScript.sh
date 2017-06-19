#!/bin/bash

sudo yum -y update && upgrade

sudo yum -y install git-all centos-relese-SCL python-setuptools python-setuptools-devel python-devel
sudo yum -y groupinstall "Development Tools"

sudo easy_install pip

https://github.com/Daniega/SCE-Tirgul-2.git
cd SCE-Tirgul-2

sudo pip install -r requirements.txt

python db_create.py

#redirects all traffic from port 80 to 5000
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000

#run app
nohup python run.py > ../log.txt 2>&1 </dev/null &