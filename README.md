ParticleStemmer
===============
Install
---------------
`pip install https://github.com/AndreyPerelygin/partstem/archive/master.zip`

Use
---------------
```python
from partstem import ParticleStemmer

st = ParticleStemmer() # language="english" default

print (st.stem("creation")) # >> creat

print (st.stem("creation", return_snowball=True)) # >> ('creat', 'creation')
```

Add custom rule
---------------
```python
st = ParticleStemmer(suffix_rule_list={
    "ation": {"with": ["ant", ""], "exception": []}
  })

print (st.stem("creation")) # >> cre
```
