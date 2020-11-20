# Python MeCab CGI : Optimized For XREA


## Installation

1. Put `index.py` to your XREA server. XREA server already installed Python3 and MeCab.
2. Set file permisson : `$ chmod 755 index.py`
3. Install `mecab-python3` : `$ python3 -m pip install mecab-python3 --user`
4. Create `.htaccess` and write following line to enable Python CGI : `AddHandler cgi-script .py`


## How To Use

- Browser
    - `http://example.s0.xrea.com/index.py`
    - With Query String : `http://example.s0.xrea.com/index.py?q=Text`
- Use `curl`
    - `$ curl 'http://example.s0.xrea.com/index.py?q=Text'`
    - `$ curl -X POST http://example.s0.xrea.com/index.py -d 'q=Text'`


## Links

- [Neo's World](https://neos21.net/)
