# Wheels of Jeopardy
---

## Programming Guidelines
- Refer to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for any and all questions.
- Example of PEP 8 in the wild: [django](https://github.com/django/django)

### Names
- [Package and Module names](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions) should be lower case and either *alloneword* or *separated_by_underscores*
  - Underscores are discouraged here
- [Class names](https://www.python.org/dev/peps/pep-0008/#class-names) should be *CapWordConvention*
- [Function, Method, and Variable names](https://www.python.org/dev/peps/pep-0008/#function-names) should be lowercase *separated_by_underscores* when necessary
- [Private/Internal Member names](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) should begin with an *_underscore*
- [Constant names](https://www.python.org/dev/peps/pep-0008/#constants) are all *CAPITALIZED*

### Documentation
- [Indentations](https://www.python.org/dev/peps/pep-0008/#indentation) = 4 [spaces](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
- [Docstrings](https://www.python.org/dev/peps/pep-0257/#rationale) should start each module/class and functions. This will help with pyDoc and generally make your code easy to understand.

```python
#Docstring Example:
"""
This module_a does thing_a
"""
```

### Imports
- Import Statements should use the full module path

```python
#Import Example
import wheelsofjeopardy.[YOUR_PATH]
```

### Tests
- Append all unit test file names with "_tests"
- Run all unit tests before committing and/or pushing
- Run all unit tests (from *root*, not tests, directory):

```bash
#Run all unit Tests
python -m unittest tests.all
```

## About
- This is the repository for the Wheel of Jeopardy program. Please contribute **only** using Python.
- This program was designed and built during the 2016 Summer Semester of JHU 605.401
- Team Members include the following:
  - Brandon Tarney
  - John Wu
  - Farheen Ajmeri
  - Miranda Link
  - Victoria Scalfari
  - Cameron Dutro



## Motto
![](https://media.giphy.com/media/ALBfFB6gP1evu/giphy.gif)
