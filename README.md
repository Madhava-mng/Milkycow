# Milkycow

MILKY COW SIMPLE ENCRYPTION

## INSTALATION:

```sh
$ python3 -m pip install milkycow
```

## ENCRYPT:

```python
>>> import milkycow as mc
>>> enc1 = mc.encrypt("hello 1", "pass")
>>> enc2 = mc.encrypt("hello 2", "password", rotate=100, layer=1, 3)
```

## DECRYPT:

```python
>>> dec1 = mc.decrypt(enc1, "pass")
>>> print(dec1)
hello 1
>>> dec2 = mc.decrypt(enc2, "password", 100, 1, 3)
>>> print(dec1)
hello 2
```

## FILE ENCRYPTION:

```python
>>> f =  mc.encrypt(open("file.txt", "r").read(), "p@55w0rd")
>>> open("file.enc", "w").write(f)
```
