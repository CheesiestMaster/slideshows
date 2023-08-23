# Desktop Background Slideshow for Linux Mint

## Description
This is a simple script that changes the desktop background at a set interval. It is intended to be run at startup.

## Installation
1. Download the script and place it in a folder of your choice.
2. Add the script to your startup applications. You do not need to specify the python interpreter, as the script has a shebang.

## Usage
The script takes three arguments: the path to the folder containing the images, the interval in seconds, and whether or not to shuffle the images. The default values are `~/Pictures`, `60`, and `False`, respectively.
```bash
slideshow/app.py [PATH] [INTERVAL] [SHUFFLE]
```

## Dependencies
* Python 3

## License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Credits
Made by [CheesiestMaster](github.com/CheesiestMaster)