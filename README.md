# UA-framer
[![Library-discord.py](https://img.shields.io/badge/Python-3.7-3778ae?logo=Python&logoColor=ffffff)](https://python.org)

# Overview
Draw the frame of the Ukrainian flag on the image.    

# Install
Python 3 or higher is required.    
```cmd
# Linux/OS X
$ python -m pip install -U ua-framer

# Windows
> py -3 -m pip install -U ua-framer
```    

# Example
Draw the frame.    
```py
import framer

from PIL import Image

framer("example.png", 10).save("example.png")
```
