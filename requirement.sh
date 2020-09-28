#!/bin/bash
echo "Installing Required Files for InfinityTools!!!"
echo ""

apt-get install python3
echo ""
apt-get install python3-pip
echo ""
apt-get update && apt-get upgrade
echo ""
pip install pyfiglet

echo "Thanks for installing ! Have Fun"

