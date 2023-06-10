import argparse
import re
class KeywordTranslator:
    translations = {
        'und': 'and',
        'als': 'as',
        'prüfe': 'assert',
        'abbrechen': 'break',
        'klasse': 'class',
        'fortsetzen': 'continue',
        'def': 'def',
        'lösche': 'del',
        'andernfalls': 'elif',
        'sonst': 'else',
        'erlaube': 'except',
        'Falsch': 'False',
        'schlussendlich': 'finally',
        'für': 'for',
        'von': 'from',
        'global': 'global',
        'wenn': 'if',
        'importiere': 'import',
        'aus': 'in',
        'ist': 'is',
        'lambda': 'lambda',
        'Nichts': 'None',
        'überlokal': 'nonlocal',
        'nicht': 'not',
        'oder': 'or',
        'weitergeben': 'pass',
        'erhöhe': 'raise',
        'gib': 'return',
        'Wahr': 'True',
        'versuche': 'try',
        'solange': 'while',
        'mit': 'with',
        'erzeuge': 'yield',
        "bereich" : "range",
        "selbst" : "self",
        "drucke" : "print",
        "mathe" : "math",
        "wurzel" : "sqrt"
    }
    #dictionary to interpret the exceptions
    translation_exceptions = {
    'Ausnahme': 'Exception',
    'Typfehler': 'TypeError',
    'Wertefehler': 'ValueError',
    'Namensfehler': 'NameError',
    'Indexfehler': 'IndexError',
    'Schlüsselfehler': 'KeyError',
    'Syntaxfehler': 'SyntaxError',
    'Einrückungsfehler': 'IndentationError',
    'Datei nicht gefunden Fehler': 'FileNotFoundError',
    'Nullteilungsfehler': 'ZeroDivisionError',
    'Überlauffehler': 'OverflowError',
    'Importfehler': 'ImportError',
    'Modul nicht gefunden Fehler': 'ModuleNotFoundError',
    'Attributfehler': 'AttributeError',
    'Behauptungsfehler': 'AssertionError',
    'Laufzeitfehler': 'RuntimeError',
    'Iterationsstopp': 'StopIteration',
    'Tastaturunterbrechung': 'KeyboardInterrupt',
    }
    #Dictionary to get name of the exception
    exception_translations = {
    'Exception': 'Ausnahme',
    'TypeError': 'Typfehler',
    'ValueError': 'Wertefehler',
    'NameError': 'Namensfehler',
    'IndexError': 'Indexfehler',
    'KeyError': 'Schlüsselfehler',
    'SyntaxError': 'Syntaxfehler',
    'IndentationError': 'Einrückungsfehler',
    'FileNotFoundError': 'DateiNichtGefundenFehler',
    'ZeroDivisionError': 'Nullteilungsfehler',
    'OverflowError': 'ÜberlaufFehler',
    'ImportError': 'Importfehler',
    'ModuleNotFoundError': 'ModulNichtGefundenFehler',
    'AttributeError': 'Attributfehler',
    'AssertionError': 'Behauptungsfehler',
    'RuntimeError': 'Laufzeitfehler',
    'StopIteration': 'Iterationsstopp',
    'KeyboardInterrupt': 'Tastaturunterbrechung',
    }
    errors_with_placeholders = {
    'unsupported operand type': 'nicht unterstützter Operandentyp',
    'division by zero': 'Division durch Null',
    'name \'{}\' is not defined': 'Name \'{}\' ist nicht definiert',
    'list index out of range': 'Listenindex außerhalb des gültigen Bereichs',
    'tuple index out of range': 'Tupelindex außerhalb des gültigen Bereichs',
    'invalid syntax': 'Ungültige Syntax',
    'indentation error': 'Einrückungsfehler',
    'file not found': 'Datei nicht gefunden',
    'attribute \'{}\' not found': 'Attribut \'{}\' nicht gefunden',
    'module \'{}\' not found': 'Modul \'{}\' nicht gefunden',
    'division or modulo by zero': 'Division oder Modulo durch Null',
    'key error': 'Schlüsselfehler',
    'invalid literal for int() with base {}: \'{}\'': 'Ungültiges Literal für int() mit Basis {}: \'{}\'',
    'unexpected indent': 'Unerwartete Einrückung',
    'not a valid identifier': 'Kein gültiger Bezeichner',
    'invalid syntax, unexpected {}: \'{}\'': 'Ungültige Syntax, unerwartetes {}: \'{}\'',
    'unsupported operand type(s) for {}: \'{}\' and \'{}\'': 'Nicht unterstützte Operandentypen für {}: \'{}\' und \'{}\'',
    }
    errors_without_placeholders = {
    'unsupported operand type': 'nicht unterstützter Operandentyp',
    'division by zero': 'Division durch Null',
    'name \'\' is not defined': 'Name \'\' ist nicht definiert',
    'list index out of range': 'Listenindex außerhalb des gültigen Bereichs',
    'tuple index out of range': 'Tupelindex außerhalb des gültigen Bereichs',
    'invalid syntax': 'Ungültige Syntax',
    'indentation error': 'Einrückungsfehler',
    'file not found': 'Datei nicht gefunden',
    'attribute \'\' not found': 'Attribut \'{}\' nicht gefunden',
    'module \'\' not found': 'Modul \'\' nicht gefunden',
    'division or modulo by zero': 'Division oder Modulo durch Null',
    'key error': 'Schlüsselfehler',
    'invalid literal for int() with base {}: \'\'': 'Ungültiges Literal für int() mit Basis {}: \'\'',
    'unexpected indent': 'Unerwartete Einrückung',
    'not a valid identifier': 'Kein gültiger Bezeichner',
    'invalid syntax, unexpected {}: \'\'': 'Ungültige Syntax, unerwartetes {}: \'\'',
    'unsupported operand type(s) for {}: \'\' and \'\'': 'Nicht unterstützte Operandentypen für {}: \'\' und \'\'',
    }
    #extracts variables, operators,... from exception text
    def extract_operators(self,error_message):
        pattern = r'\'(.*?)\'|//?|/'
        operators = re.findall(pattern, error_message)
        operators = [op for op in operators if op != '']
        return operators
    #removes operators
    def remove_operators(self, string, operators):
        for operator in operators:
            pattern = re.escape(operator)
            string = re.sub(pattern, '', string)
        return string
    def translate_exception(self,exception):
        exception_type = type(exception).__name__ #name of the exception
        translated_type = self.exception_translations.get(str(exception_type), str(exception_type)) #translated name
        for trans in self.errors_with_placeholders:
            try:
                operators = self.extract_operators(str(exception))
                t = trans.format(*self.extract_operators(str(exception)))
                if t == str(exception):
                    e = self.remove_operators(t, operators)
                    translated_output = self.errors_without_placeholders.get(e)
                    for op in operators:
                        translated_output = translated_output.replace("''", op) 
                    break
            except Exception as e:
                translated_output = self.errors_with_placeholders.get(str(exception))
        
        if translated_output is None: #if no translation is available
            translated_output = str(exception)
        return translated_output

    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.code = f.read()

    def translate_keywords(self):
        # Replace each German keyword with the corresponding English keyword
        for german, english in self.translations.items():
            self.code = self.code.replace(german, english)
        for german, english in self.translation_exceptions.items():
            self.code = self.code.replace(german, english)

    def execute(self):
        self.translate_keywords()
        exec(self.code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    translator = KeywordTranslator(args.file)
    try:
        translator.execute()
    except Exception as e:
    # Übersetze die Exception, wenn sie im Dictionary vorhanden ist
        translated_message = translator.translate_exception(e)
        print(f'Fehler aufgetreten: {translated_message}')


