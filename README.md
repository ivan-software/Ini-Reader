# Ini-Reader
Ini-Reader For Python

# Installation

```pip
pip install ini-reader
```

# Documentation

First Import The Module:
```python
import ini_reader
```
After Lets Create File With Extension ".ini" And Name Will Be "Very Important".

```ini
[GITHUB]
username="hacker228"
password=12345
```

After Creating, Lets Read INI And Print It.

```python
import ini_reader
ini_reader.INIReader.IniRead("Very Important.ini")
ini_reader.INIReader.Read("GITHUB", "username", PRINT=1)
```

Result:

```python
>>> "hacker228"
```

Print=0 - Read Files Without Print It
Print=1 - Read Files And Print It

And Lets Get Help Offline:

```python
ini_reader.INIReader.Help()
```

This Is Full Documentation.

#
