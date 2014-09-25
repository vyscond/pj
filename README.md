# PJ

CLI for python json library



## Runtime

- python [3][1] or [2][2]

## Installation

### 1. clone

    git clone https://github.com/vyscond/pj.git


### 2. build

    cd pj/
    python setup.py bdist_wheel


### 3. install

replace X for the available version

    cd dist/
    pip install pj-X-py2.py3-none-any.whl




## Usage

### Commands

#### **pjget**

1 - Getting values from _root_ structs

```
pjget [file] [key]
```

Example:
       
- file.json 
```json
{
    "foo" : "foo_v"
}
```
- input 
```
pjget file.json foo
```
                  
- output 
```
foo_v
```

2 - Getting values from _deep-in_ structs

```
pjget [file] [key] [struct_path]
```

The [struct_path] is a string based on the attribute access syntax on OO languages like python itself. So to define the symbol that will be used as the **delimiter** insert him at the beginning of the string

Example: getting the value store at **"loo"**
        
- file.json 
```json
  {
      "foo" : {
        "boo" : {
            "doo" : {
                "loo" : "loo_v"
            }
        }
      }
  }
```
- input 

```
pjget file.json loo .foo.boo.doo
```
                  
- output 

```
loo_v
```
  
This example can be rewrited to make use of **#** as the demiliter
  
- input 
```
pjget file.json loo #foo#boo#doo
```
                  
- output 
```
loo_v
```

#### **pjset**

_soon_

#### **pjpop**

_soon_

### License

MIT

[1]: https://www.python.org/download/releases/3.4.1/
[2]: https://www.python.org/download/releases/2.7.8/