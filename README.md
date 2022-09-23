## Installing
```shell
pip install linsh
```

## Usage
### sync(run)
```python
from linsh import LinSH as s
```

`only` return `returncode`; directly `print` result
```python
returncode = s("ls -al") >None
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

### async(Popen)
```python
from linsh import LinSH as s

# No Output (But it did work)
s("ls -al") & None
# you can try it  
s("touch 1.py") & None
```


```python
from linsh import LinSH as s

sp_list = []
for x in range(5):
    sp = s("sleep 5") & ...
    # sp.communicate()
    sp_list.append(sp)


for _sp in sp_list:
    _sp.communicate()

```
