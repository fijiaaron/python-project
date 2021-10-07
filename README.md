this works:

python -m library.module3.class3

but this doesn't work:

python library/module3/class3.py


```
$python module1/class1.py 
in file: module1/class1.py
initializing Class1
```

```
$python -m module1.class1
in file: /home/aaron/scratch/python-project/module1/class1.py
initializing Class1
```

```
$python module2/class2.py 
in file: module2/class2.py
initializing Class2
```

```
$python -m module2.class2
in file: /home/aaron/scratch/python-project/module2/class2.py
initializing Class2
```

```
$python module3/class3.py 
in file: module3/class3.py
Traceback (most recent call last):
  File "module3/class3.py", line 3, in <module>
    from module1.class1 import Class1
ModuleNotFoundError: No module named 'module1'
```

```
$python -m module3.class3
in file: /home/aaron/scratch/python-project/module3/class3.py
in file: /home/aaron/scratch/python-project/module1/class1.py
in file: /home/aaron/scratch/python-project/module2/class2.py
initializing Class3
initializing Class1
initializing Class2
```

```
$python using_module1_and_module2.py 
in file: /home/aaron/scratch/python-project/module1/class1.py
in file: /home/aaron/scratch/python-project/module2/class2.py
in file: using_module1_and_module2.py
name: __main__
initializing Class1
initializing Class2
```

```
$python using_class3_with_both_modules_relative.py 
in file: /home/aaron/scratch/python-project/module3/class3.py
in file: /home/aaron/scratch/python-project/module1/class1.py
in file: /home/aaron/scratch/python-project/module2/class2.py
initializing Class3
initializing Class1
initializing Class2
```