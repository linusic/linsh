## Installing
```shell
pip install linsh
```

## Usage
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
