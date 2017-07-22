# Netcat Example

Run it like this:

1. Start netcat in listening mode ("server mode"):

```
nc -s 127.0.0.1 -v -l -p 4321 -e doSomething
```

2. Connect to the server:

```
nc 127.0.0.1 4321
```
