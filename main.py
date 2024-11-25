from greets import greets
from translate import Translator

translator = Translator(to_lang='ro')

for g in greets:
    print(translator.translate(g).title() + "!")