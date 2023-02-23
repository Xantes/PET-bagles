class LanguageProvider():
    def __init__(self):
        self.providers = {}

    def add_language(self, language_name, language):
        self.providers[language_name] = language

    def provide_language(self, language_name):
        return self.providers[language_name]


language_factory = LanguageProvider()
language_factory.add_language('English', 'languages/english.yaml')
language_factory.add_language('Russian', 'languages/russian.yaml')
language_factory.add_language('Spanish', 'languages/spanish.yaml')
