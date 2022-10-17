# Little Piece Crisps

This a collection which contains part of my scripts.

## Contents

- THEOL
  - Post login request to eol of CDNU
  - [TO BE DONE] Parse the homework list. 

## Usage

- THEOL

```python
import lxml.etree as le
login = Login()
login.login('Your username', 'Your password')
le.tostring(login.hwlist()[0])
```
