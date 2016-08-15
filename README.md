# Wheel of Jeopardy
---

## Programming Guidelines
- Refer to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for any and all questions.
- Example of PEP 8 in the wild: [django](https://github.com/django/django)

### Names
- [Package and Module names](https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions) should be lower case and either *alloneword* or *separated\_by\_underscores*
  - Underscores are discouraged here
- [Class names](https://www.python.org/dev/peps/pep-0008/#class-names) should be *CapWordConvention*
- [Function, Method, and Variable names](https://www.python.org/dev/peps/pep-0008/#function-names) should be lowercase *separated\_by\_underscores* when necessary
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
Import Statements should use the full module path:

```python
# import Example
import wheelofjeopardy.[YOUR_PATH]
```

For this reason, it's usually easier to run your code as a module using Python's `-m` option, which lets you pass in a module path instead of a filename. For example, if you wanted to run our text-based GUI, you might execute:

```bash
python wheelofjeopardy/gui/text_gui.py
```

Unfortunately this doesn't work because of Python's load path semantics. Instead, run it as a module using the `-m` option:

```bash
python -m wheelofjeopardy.gui.text_gui
```

(Notice the dots instead of slashes and the missing .py extension).

### Tests

Tests are written with the TestUnit functionality available in the Python standard library.

- Append all unit test file names with "_tests"
- Run all unit tests before committing and/or pushing

## Running the Program

There are two available GUIs (run these commands from the root directory of your project):

```bash
# PyQt GUI:
python -m wheelofjeopardy.gui.woj_application_window
```

### CHEAT (script the sector Order)
Set the "spinSequence" in the Options.ini file, i.e. "spinSequence=1 2 12"

```bash
# text-based GUI:
python -m wheelofjeopardy.gui.text_gui
```



### Debugging Events

Setting the `LOG_EVENTS` environment variable to `true` will print every event the system broadcasts to the console. For example:

```bash
LOG_EVENTS=true python -m wheelofjeopardy.gui.text_gui
```

## PyQt
Wheel of Jeopardy uses PyQt to privide a window-based GUI. We use Qt Creator to design each window, then use the `pyuic4` command to convert the resulting .ui files to .py files. We've got a handy script you can run to regenerate everything:

```bash
python -m wheelofjeopardy.gui.pyqt.regenerate
```


## Running Tests

Run all the tests at once:

```bash
python -m unittest tests.all
```

Run a single test file:

```bash
python -m unittest tests.text_helper_tests
```

Run a single test case:

```bash
python -m unittest tests.text_helper_tests.TestApostrophize
```

Run an individual test method:

```bash
python -m unittest tests.text_helper_tests.TestApostrophize.test_name_ends_with_s
```

## About This Project
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
