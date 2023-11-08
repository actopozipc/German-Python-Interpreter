# Schlange, an interpreter for german python
An alternative python interpreter that accepts german keywords
## Usage
    python Schlange.py test.sch
or

    ./Schlange test.sch
    
## Example
![grafik](https://github.com/actopozipc/German-Python-Interpreter/assets/48481041/93bd66c2-1b2d-477d-8943-dc95d7ecc92f)

## Supported keywords and functions
### Keywords

| Englisch     | Deutsch      |
| ------------ | ------------ |
| `and`        | `und`        |
| `as`         | `als`        |
| `assert`     | `prüfe`     |
| `async`     | `asynch`     |
| `await`     | `erwarte`     |
| `break`      | `brechen`    |
| `class`      | `Klasse`     |
| `continue`   | `fortsetze` |
| `def`        | `def`  |
| `del`        | `lösche`     |
| `elif`       | `andernfalls`  |
| `else`       | `sonst`      |
| `except`     | `Ausnahme`|
| `False`      | `Falsch`     |
| `finally`    | `schlussendlich`|
| `for`        | `für`        |
| `from`       | `von`        |
| `global`     | `global`     |
| `if`         | `wenn`       |
| `import`     | `importiere` |
| `in`         | `in`         |
| `is`         | `ist`        |
| `lambda`     | `lambda`     |
| `None`       | `Nichts`      |
| `nonlocal`   | `nichtlokal` |
| `not`        | `nicht`      |
| `or`         | `oder`       |
| `pass`       | `passe`|
| `raise`      | `erhöhe`     |
| `return`     | `Rückkehr`   |
| `True`       | `Wahr`       |
| `try`        | `versuche`   |
| `while`      | `solange`    |
| `with`       | `mit`        |
| `yield`      | `erzeuge`     |

### Exceptions
| Englisch | Deutsch |
| --- | --- |
| `Exception` | `Ausnahme` |
| `TypeError` | `Typfehler` |
| `ValueError` | `Wertefehler` |
| `NameError` | `Namensfehler` |
| `IndexError` | `Indexfehler` |
| `KeyError` | `Schlüsselfehler` |
| `FileNotFoundError` | `DateiNichtGefundenFehler` |
| `SyntaxError` | `Syntaxfehler` |
| `IndentationError` | `Einrückungsfehler` |
| `ImportError` | `Importfehler` |
| `ModuleNotFoundError` | `ModulNichtGefundenFehler` |
| `ZeroDivisionError` | `Nullteilungsfehler` |
| `ArithmeticError` | `Rechenfehler` |
| `OverflowError` | `Überlauffehler` |
| `AssertionError` | `Behauptungsfehler` |
| `AttributeError` | `Attributfehler` |
| `RuntimeError` | `Laufzeitfehler` |
| `KeyError` | `Schlüsselfehler` |
| `StopIteration` | `IterationStoppen` |
| `PermissionError` | `Berechtigungsfehler` |
| `TypeError` | `Typfehler` |
### Built-in Functions
| Englisch      | Deutsch      |
|--------------|--------------|
| all          | alle         |
| any          | irgendein    |
| breakpoint   | brechpunkt   |
| callable     | aufrufbar    |
| compile      | kompiliere   |
| complex      | komplex      |
| delattr      | löschattr    |
| enumerate    | enumerate (missing)   |
| getattr      | bekommeattr  |
| globals      | globale      |
| hasattr      | hatattr      |
| help         | hilfe        |
| input        | eingabe      |
| isinstance   | istinstanz   |
| issubclass   | istsubklasse |
| len          | län          |
| list         | liste        |
| locals       | lokale       |
| map          | karte        |
| next         | nächstes     |
| object       | objekt       |
| open         | öffne        |
| property     | eigenschaft  |
| range        | reichweite   |
| reversed     | rückwärts    |
| round        | runde        |
| setattr      | setzattr     |
| sorted       | sortiere     |
| staticmethod | statischemethode |
| slice        | slice (missing)        |
| tuple        | tupel        |
| type         | typ          |
| print        | drucke       |
| math         | mathe        |
| sqrt         | wurzel       |



## TODO
* Intellisense support
* More function names (numpy, matplotlib)
* Adding missing translations (enumerate, slice)
* More german keywords (see discussions)
