# band_name_checker

A script to take a list of potential band names, generate possible domain names from them
and then run `whois` queries against them to see which ones are already taken.

## Dependencies

This script uses [pywhois](https://github.com/richardpenman/pywhois) for the `whois` lookups.

## Setup

Run `pip install -r requirements.txt` 

## Usage

```python
usage: band_name_checker.py [-h] [--file FILE] [name [name ...]]

Check if domains for possible band names are already taken

positional arguments:
  name         possible band names

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  file of possible band names, one per line
```