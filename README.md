# FileLocker

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b61e794ca5244153abe657af497f9473)](https://www.codacy.com/manual/th3c0d3br34ker/FileLocker?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=th3c0d3br34ker/FileLocker&amp;utm_campaign=Badge_Grade)

This python script is a file locker.
It locks the file with a Key which is again encrypted by a password using AES Encryption.
If the key is lost then it becomes immpossible to recover the file.

## Dependences

1.  tqdm
2.  pycryptodome

## Known Problems

1.  Exceptional Handling
2.  Setting the path to the files (lock, unlock, KEY), i.e., getting it from the user.

## TODO

1.  Add password feature.
2.  Make log more comprehensive.
3.  Make Locking and Unlocking functions into classes.
