# FileLocker

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
1.  Make log more comprehensive.  
1.  Make Locking and Unlocking functions into classes.  
1.  Setup cli for testing.
