#!/bin/sh

python -c "a=raw_input('press any key to continue')"
sudo ./utils/librfid-tool -s
python update.py
rm file.txt
sudo ./start1.sh


