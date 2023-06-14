import argparse
import re
import os

class KeywordTranslator:
    translations = {
        'und': 'and',
        'als': 'as',
        'prüfe': 'assert',
        'breche': 'break',
        'Klasse': 'class',
        'fortsetze': 'continue',
        'def': 'def',
        'lösche': 'del',
        'andernfalls': 'elif',
        'sonst': 'else',
        'Ausnahme': 'except',
        'Falsch': 'False',
        'schlussendlich': 'finally',
        'für': 'for',
        'von': 'from',
        'global': 'global',
        'wenn': 'if',
        'importiere': 'import',
        'in': 'in',
        'ist': 'is',
        'lambda': 'lambda',
        'Nichts': 'None',
        'nichtlokal': 'nonlocal',
        'nicht': 'not',
        'oder': 'or',
        'passe': 'pass',
        'erhöhe': 'raise',
        'Rückkehr': 'return',
        'Wahr': 'True',
        'versuche': 'try',
        'solange': 'while',
        'mit': 'with',
        'erzeuge': 'yield',
        "reichweite" : "range",
        "selbst" : "self",
        "drucke" : "print",
        "mathe" : "math",
        "wurzel" : "sqrt"
    }
    #dictionary to interpret the exceptions
    translation_exceptions = {
    'Ausnahme': 'Exception',
    'TypFehler': 'TypeError',
    'WerteFehler': 'ValueError',
    'NamensFehler': 'NameError',
    'IndexFehler': 'IndexError',
    'SchlüsselFehler': 'KeyError',
    'SyntaxFehler': 'SyntaxError',
    'EinrückungsFehler': 'IndentationError',
    'DateiNichtGefundenFehler': 'FileNotFoundError',
    'NullteilungsFehler': 'ZeroDivisionError',
    'überlaufFehler': 'OverflowError',
    'ImportFehler': 'ImportError',
    'ModulNichtGefundenFehler': 'ModuleNotFoundError',
    'AttributFehler': 'AttributeError',
    'BehauptungsFehler': 'AssertionError',
    'LaufzeitFehler': 'RuntimeError',
    'IterationStoppen': 'StopIteration',
    'TastaturUnterbrechung': 'KeyboardInterrupt',
    }
    #Dictionary to get name of the exception
    exception_translations = dict((val,key) for key, val in translation_exceptions.items())

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
        with open(file_path, 'r', encoding='utf-8') as f:
            self.code = f.read()


    def split_formmated(self, code: str) -> str:
        string_pattern = re.compile(r'(f)(\"(.*?)\"|\'(.*?)\')')
        any_formatted_pattern = re.compile(r'{(.*?)}')

        strings = string_pattern.findall(code)
        original_strings = [string[1] for string in strings]

        for i, string in enumerate(strings):
            content = string[1]
            format_indicator = string[0]
            quark_type = content[0]

            if format_indicator:
                formatted = any_formatted_pattern.findall(content)
                formatted_fitted = [
                    f'{quark_type} + str({i}) + {quark_type}' for i in formatted]
                
                for original, fitted in zip(formatted, formatted_fitted):
                    content = content.replace(f"{{{original}}}", fitted)

            strings[i] = content

        for original, split in zip(original_strings, strings):
            code = code.replace(original, split)

        return code


    def obfuscate_strings(self, code: str) -> tuple[str, dict[int, str]]:
        string_pattern = re.compile(r'\"(.*?)\"|\'(.*?)\'')

        strings = string_pattern.findall(code)
        strings = ["".join(string) for string in strings]
        string_replacements = {}

        for i, string in enumerate(strings):
            if re.match(r'^\s*$', string):
                continue

            string_replacements[i] = string
            code = code.replace(string, f'__{i}__')

        return code, string_replacements


    def deobfuscate_strings(self, code: str, replacements: dict[int, str]) -> str:
        for i, v in replacements.items():
            code = code.replace(f'__{i}__', v)

        return code


    def translate_keywords(self):
        # Replace each German keyword with the corresponding English keyword

        self.code = self.split_formmated(self.code)
        self.code, self.string_replacements = self.obfuscate_strings(self.code)

        for german, english in self.translations.items():
            self.code = re.sub(r"\b" + re.escape(german) + r"\b", english, self.code) #self.code.replace(german, english)
        for german, english in self.translation_exceptions.items():
            self.code = self.code.replace(german, english)

        self.code = self.deobfuscate_strings(self.code, self.string_replacements)

    def execute(self):
        self.translate_keywords()
        exec(self.code)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    if not args.file.endswith('.sch'):
        print('Dateiendung muss .sch sein!')
        exit(-1)

    if not os.path.exists(args.file):
        print('Datei existiert nicht!')
        exit(-1)

    translator = KeywordTranslator(args.file)
    try:
        translator.execute()
    except Exception as e:
    # Übersetze die Exception, wenn sie im Dictionary vorhanden ist
        translated_message = translator.translate_exception(e)
        print(f'Fehler aufgetreten: {translated_message}')
