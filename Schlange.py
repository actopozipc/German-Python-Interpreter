import argparse
import re
import os
import sys
import importlib
import types
'''
Naming convention: 
    Keywords: Written like in german (e.g. Klasse = class) besides Wahr and Falsch (to ensemble pythons True and False)
    Exceptions: PascalCase (e.g TypFehler for TypeError)
    Classes: snakeCase
    (built in) Functions: lowercase (e.g drucke for print)

'''
class KeywordTranslator:
    translations = {
        'und': 'and',
        'als': 'as',
        'prüfe': 'assert',
        'asynch': 'async',
        'erwarte': 'await',
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
        "selbst": "self"
    }
    
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

    translation_functions = {
        "alle": "all",
        "irgendein": "any",
        "brechpunkt": "breakpoint",
        "aufrufbar": "callable",
        "kompiliere": "compile",
        "komplex": "complex",
        "löschattr": "delattr",
        "enumerate": "enumerate",
        "bekommeattr": "getattr",
        "globale": "globals",
        "hatattr": "hasattr",
        "hilfe": "help",
        "eingabe": "input",
        "istinstanz": "isinstance",
        "istsubklasse": "issubclass",
        "län": "len",
        "liste": "list",
        "lokale": "locals",
        "karte": "map",
        "nächstes": "next",
        'objekt': 'object',
        "öffne": "open",
        "eigenschaft": "property",
        "reichweite": "range",
        "rückwärts": "reversed",
        "runde": "round",
        "setzattr": "setattr",
        "sortiere": "sorted",
        "statischemethode": "staticmethod",
        "slice": "slice",
        "tupel": "tuple",
        "typ": "type",
        "drucke": "print",
        "mathe": "math",
        "wurzel": "sqrt"
    }


    exception_translations = dict((val, key) for key, val in translation_exceptions.items())
    
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
        'No module named \'{}\' ' : 'Kein Modul namens \'{}\'' 
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
         'No module named \'{}\' ' : 'Kein Modul namens \'{}\'' 
    }

    def extract_operators(self, error_message):
        pattern = r'\'(.*?)\'|//?|/'
        operators = re.findall(pattern, error_message)
        operators = [op for op in operators if op != '']
        return operators

    def remove_operators(self, string, operators):
        for operator in operators:
            pattern = re.escape(operator)
            string = re.sub(pattern, '', string)
        return string

    def translate_exception(self, exception):
        exception_type = type(exception).__name__
        translated_type = self.exception_translations.get(str(exception_type), str(exception_type))
        translated_output = None
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
            except Exception:
                translated_output = self.errors_with_placeholders.get(str(exception))
        
        if translated_output is None:
            translated_output = str(exception)
        return translated_output

    def __init__(self, file_path):
        self.file_path = file_path
        self.module_registry = {}
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
    def translate(self, part: str) -> str:
        for german_keyword, english_keyword in self.translations.items():
            part = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, part)
        for german_keyword, english_keyword in self.translation_exceptions.items():
            part = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, part)
        for german_keyword, english_keyword in self.translation_functions.items():
            part = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, part)
        for german_keyword, english_keyword in self.translation_array_methods.items():
            part = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, part)
        return part
    def translate_code(self):
        translated_code = self.split_formmated(self.code)
        for german_keyword, english_keyword in self.translations.items():
            translated_code = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, translated_code)
        for german_keyword, english_keyword in self.translation_exceptions.items():
            translated_code = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, translated_code)
        for german_keyword, english_keyword in self.translation_functions.items():
            translated_code = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, translated_code)
        for german_keyword, english_keyword in self.translation_array_methods.items():
            translated_code = re.sub(r'\b{}\b'.format(german_keyword), english_keyword, translated_code)
        self.translated_code = translated_code

    def extract_imports(self):
        imports = re.findall(r'import\s+([a-zA-Z0-9_]+)', self.translated_code)
        return imports

    def dynamic_import(self, module_name):
        try:
            if module_name in self.module_registry:
                return self.module_registry[module_name]
            module_code = self.load_module_code(module_name)
            translated_module_code = self.translate(module_code)
            module = self.execute_module(module_name, translated_module_code)
            self.module_registry[module_name] = module
            return module
        except ImportError as e:
            pass #Exception will be handled by the other try except anyway

    def load_module_code(self, module_name):
        try:
            directory_path = self.file_path.split('/')[0]
            with open(f"{directory_path}/{module_name}.sch", "r", encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise ImportError(f"Modul {module_name} nicht gefunden  ")

    def execute_module(self, module_name, code):
        module = types.ModuleType(module_name)
        exec(code, module.__dict__)
        sys.modules[module_name] = module
        return module

    def execute(self):
        exec(self.translated_code, globals())




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Führt eine Schlange-Datei aus')
    parser.add_argument('file', type=str, help='Pfad zu der Schlange-Datei')
    args = parser.parse_args()
    if not args.file.endswith('.sch'):
        print('Dateiendung muss .sch sein!')
        exit(-1)

    if not os.path.exists(args.file):
        print('Datei existiert nicht!')
        exit(-1)
    translator = KeywordTranslator(args.file)
    translator.translate_code()
    imports = translator.extract_imports()
    for module in imports:
        translator.dynamic_import(module)
    try:
        translator.execute()
    except Exception as e:
    # Übersetze die Exception, wenn sie im Dictionary vorhanden ist
        
        translated_message = translator.translate_exception(e)
        print(f'Fehler aufgetreten: {translated_message}')
