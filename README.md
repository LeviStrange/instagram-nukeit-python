# Instagram Nuke It - Python

A simple script to untag, unlike and unsave your Instagram photos. 

## Getting Started

### Prerequisites

Make sure that pip is up to date, Python is installed and you are running chromedriver version 2.42.

```
pip install --upgrade pip
brew install Python
```

To check your chromedriver version

```
chromedriver --version
```

If your version is not 2.42 do one of the following:

```
brew uninstall chromedriver
brew tap homebrew/cask
brew cask install chromedriver
chromedriver --version
```

or download it from here:

https://chromedriver.storage.googleapis.com/index.html?path=2.42/


### Installing

A step by step series of examples that tell you how to get the project up and running

```
git clone https://github.com/levistrange/instagram-nukeit-python.git
cd instagram-nukeit-python
pip install -r requirements.txt
cp config.cfg.example config.cfg
```

Now populate the config.cfg file with username and password for your instagram

```
CONFIG.cfg
[instagram]
username = 
password =
```

Then run the python instagram nukeit file

```
python instagram-nukeit.py
```

The script will run automatically and untag every single photo of the given user, until there are no tagged photos left. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This is a modification of Adrian Goris' facebook-nukeit-python script - https://github.com/adriangoris/facebook-nukeit-python
* Check out https://github.com/adriangoris/social-nukeit-python to see both the Instagram-Nukeit and Facebook-Nukeit from the same directory
