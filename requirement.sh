#!/bin/bash
echo "Installing Required Files for InfinityTools!!!"
echo ""

apt-get install python
echo ""
apt-get update && apt-get upgrade
echo ""
pip install pyfiglet
chmod +x infinity.py

echo "Thanks for installing ! Have Fun"

