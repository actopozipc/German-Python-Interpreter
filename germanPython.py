import argparse

class KeywordTranslator:
    translations = {
        'und': 'and',
        'als': 'as',
        'prÃ¼fe': 'assert',
        'breche': 'break',
        'klasse': 'class',
        'fortsetze': 'continue',
        'def': 'def',
        'lösche': 'del',
        'andernfalls': 'elif',
        'sonst': 'else',
        'ausnahme': 'except',
        'Falsch': 'False',
        'finalisierend': 'finally',
        'fÃ¼r': 'for',
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
        'erhÃ¶he': 'raise',
        'RÃ¼ckkehr': 'return',
        'Wahr': 'True',
        'versuche': 'try',
        'solange': 'while',
        'mit': 'with',
        'erzeuge': 'yield',
        "reichweite" : "range",
        "selbst" : "self",
        "drucke" : "print",
        "mathe" : "math",
        "Wurzel" : "sqrt",
        "Nullteilungsfehler" : "ZeroDivisionError"
    }

    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.code = f.read()

    def translate_keywords(self):
        # Replace each German keyword with the corresponding English keyword
        for german, english in self.translations.items():
            self.code = self.code.replace(german, english)

    def execute(self):
        self.translate_keywords()
        exec(self.code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    args = parser.parse_args()

    translator = KeywordTranslator(args.file)

    translator.execute()


