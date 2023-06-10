# German-Python-Interpreter
An alternative python interpreter that accepts german keywords
## Usage
    python Schlange.py test.py
    
## Example
![grafik](https://github.com/actopozipc/German-Python-Interpreter/assets/48481041/93bd66c2-1b2d-477d-8943-dc95d7ecc92f)

## Supported keywords and functions
### Keywords

| Englisch     | Deutsch         |
| ------------ | --------------- |
| `and`        | `und`           |
| `as`         | `als`           |
| `assert`     | `prüfe`         |
| `break`      | `abbrechen`     |
| `class`      | `klasse`        |
| `continue`   | `fortsetzen`    |
| `def`        | `def`           |
| `del`        | `lösche`        |
| `elif`       | `andernfalls`   |
| `else`       | `sonst`         |
| `except`     | `ausgenommen`   |
| `False`      | `Falsch`        |
| `finally`    | `schlussendlich`|
| `for`        | `für`           |
| `from`       | `von`           |
| `global`     | `global`        |
| `if`         | `wenn`          |
| `import`     | `importiere`    |
| `in`         | `aus`           |
| `is`         | `ist`           |
| `lambda`     | `lambda`        |
| `None`       | `Nichts`        |
| `nonlocal`   | `überlokal`     |
| `not`        | `nicht`         |
| `or`         | `oder`          |
| `pass`       | `passe`         |
| `raise`      | `erhöhe`        |
| `return`     | `gib`           |
| `True`       | `Wahr`          |
| `try`        | `versuche`      |
| `while`      | `solange`       |
| `with`       | `mit`           |
| `yield`      | `erzeuge`       |

### Exceptions
| Exception             | Übersetzung                |
| --------------------- | -------------------------- |
| `Exception`           | 'Ausnahme'                 |
| `TypeError`           | 'Typfehler'                |
| `ValueError`          | 'Wertefehler'              |
| `NameError`           | 'Namensfehler'             |
| `IndexError`          | 'Indexfehler'              |
| `KeyError`            | 'Schlüsselfehler'          |
| `FileNotFoundError`   | 'DateiNichtGefundenFehler' |
| `SyntaxError`         | 'Syntaxfehler'             |
| `IndentationError`    | 'Einrückungsfehler'        |
| `ImportError`         | 'Importfehler'             |
| `ModuleNotFoundError` | 'ModulNichtGefundenFehler' |
| `ZeroDivisionError`   | 'Nullteilungsfehler'       |
| `ArithmeticError`     | 'Rechenfehler'             |
| `OverflowError`       | 'Überlauffehler'           |
| `AssertionError`      | 'Behauptungsfehler'        |
| `AttributeError`      | 'Attributfehler'           |
| `RuntimeError`        | 'Laufzeitfehler'           |
| `KeyError`            | 'Schlüsselfehler'          |
| `StopIteration`       | 'Iterationsstopp'          |
| `PermissionError`     | 'Berechtigungsfehler'      |
| `TypeError`           | 'Typfehler'                |


## TODO
* Intellisense support
* Workaround so that strings do not get altered by the interpreter
* Executable compiled file that interprets files with .sch extension -> Schlange test.sch should be possible

