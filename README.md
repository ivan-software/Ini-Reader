# Ini-Reader 1.1
Ini-Reader For Python

# Documentation (UPDATED)

First Import The Module:
```python
import ini_reader
```
After Lets Create File With Extension ".ini" And File Name Will Be "Very Important".

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

Lets Write An Existing File

Ini:

(Name Will Be "Inf.ini"

```ini
None
```

```python
a = "[PASSWORDS]\npassword_user1=12345\npassword_user2=123456
ini_reader.INIReader.WriteIniFile("inf.ini", a)
```

Done

Lets Create File And Write In Some-Info!

```python
a = "[PASSWORDS]\npassword_user1=12345\npassword_user2=123456
ini_reader.CreateAndWriteIniFile("passwords.ini", a) 
```

Done

#
