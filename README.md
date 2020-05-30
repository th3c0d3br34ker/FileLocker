# FileLocker

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8a1e9a664c1341829e8dc3addb062450)](https://www.codacy.com?utm_source=github.com&utm_medium=referral&utm_content=th3c0d3br34ker/FileLocker&utm_campaign=Badge_Grade)

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
