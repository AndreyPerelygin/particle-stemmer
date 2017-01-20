ParticleStemmer
===============
Install
---------------
`pip install https://github.com/AndreyPerelygin/partstem/archive/master.zip`

Use
---------------
  ```from partstem import ParticleStemmer
  
  st = ParticleStemmer() # language="english" default
  
  print (st.stem("creation"))
  creat
  
  print (st.stem("creation", , return_snowball=True))
  ('creat', 'creation')```
