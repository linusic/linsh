## Installing
```shell
pip install linsh
```

## Usage

### LinSH

```python
from linsh import LinSH as s
```

return `None`; directly `print` result
```python
s("ls -al") >None
```

return `<subprocess.CompletedProcess>` and `not print`  
```python
result = s("ls -al") >...
print(result.stdout)
print(result.stderr)
```

return `stdout` and `not print`  
```python
out = s("ls -al") > 1
print(out)
```

return `stderr` and `not print`  
```python
err = s("llll") > 2
print(err)
```


pipeline
```python
s("ps aux | grep 1 | grep root") >None

# same usage 👇
cmd = "ps aux"
cmd2 = "grep 1"
cmd3 = "grep root"
s(cmd)| cmd2 | cmd3 > None
```

### init

add `your_script.py`

```python
from linsh import init

available_names = init()
print(available_names) # ['_1', '_2', '_3', '__3', '__2', '__1']

# after below >> python your_script.py a b c
# you can see the result
print(_1, _2, _3)    # a b c   # index        (1-based)
print(__1, __2, __3) # c b a   # reverse-index(-1-based)

print(__)            # ['a', 'b', 'c']   # equal to sys.argv[1:]
```

run `your_script.py`

```shell
python your_script.py a b c
```
