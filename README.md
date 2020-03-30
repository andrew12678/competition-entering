# Competition Entering with Auto-fill

Opens all competitions that are expiring today. The reasoning behind doing this as opposed to 7 days is to reduce the amount of pages needed to be opened at one time and the fact that some competitions may suddenly appear/be registered.

## Requirements

This program will require a Google Chrome version `80.x` to be installed and a version of `python3` (https://www.python.org/downloads/).

Open terminal to check whether you have installed `python3` successfully with:

```console
python3 --version
``` 

The output should be `Python 3.x.x` 

We then need to install Selenium via

```console
pip3 -r install requirements.txt
```

## Execution

You can run the script with: 

```python3
python3 open_pages.py
```

The pages should remain open for 10 minutes. To enable Chrome auto-fill functionality to save time enter (chrome://settings/addresses) in your browser and add an address 