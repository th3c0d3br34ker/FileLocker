FileLocker
===
This python script is a file locker.
It locks the file with a Key which is again encrypted by a password using AES Encryption.
If the key is lost then it becomes immpossible to recover the file.

Dependences
---
1. tqdm
2. pycrypto

Known Problems
---
1. Exceptional Handling
2. Setting the path to the files (lock, unlock, KEY), i.e., getting it from the user.

To do:
---
1. Add password feature.
2. Make log more comprehensive.
