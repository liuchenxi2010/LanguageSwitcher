# -*- coding=utf-8 -*-
"""
This package can switch the langauge you defined, there're 4 functions in this module: \n
:mod:`save()  load()  create()  delete()`;\n
You can code like this:: \n

    >>> import Language
    >>> Llist = [{'0':'Hello', '1':'World!'}]
    >>> Llist2 = [{'0':'Language', '1':'Switched!'}]  #In language list, there must a dictionary in the list 
    >>> en_US = Language(name = 'en_US', paths = 'language\\en_US.json')
    >>> zh_CN = Language(name = 'zh_CN', paths = 'language\\zh_CN.json')
    >>> en_US.create()
    >>> en_US.save(language = Llist)
    >>> enText = en_US.load(languageName = '0')
    >>> enText2 = en_US.load(languageName = '1')
    >>> zh_CN.create()
    >>> zh_CN.save(language = Llist2)
    >>> zhText = zh_CN.load(languageName = '0')
    >>> zhText2 = zh_CN.load(languageName = '1')
    >>> print(enText, enText2)
    >>> print(zhText, zhText2)
    >>> zh_CN.delete()
    >>> en_US.delete()

    Output: 
    >>> Hello World!
    >>> Language Switched!
"""

import json
import os
import sys

fileString = '''{
    "languageName": "*",
    "languageSettings":[{}]
}
'''

__version__ = '0.2.5'

languageList: list = []


class Language(object):
    def __init__(self, name, paths) -> None:
        self.name = name
        self.paths = paths

    def save(self, language: list):
        """
:mod:`save` function can save a language file. The type of language file must be :mod:`json`\n
Argument:\n
    language: the language list, in this list, there must be only a dictionary in the list;\n
    in the dictionary, the keys must be '0', '1', '2' ...,\n
    for example: :mod:`languageList: list = [{'0': 'language', '1':'list'}]`
"""
        try:
            with open(self.paths, 'w+', encoding='utf-8') as l:
                if self.paths not in languageList:
                    languageList.append(self.paths)
                    print('+!')
                if self.paths[-5:] != '.json':
                    raise TypeError(
                        'The type of language file must be ".json"')
                replace = fileString.replace('[{}]', str(language))
                replace = replace.replace('*', self.name)
                replace = replace.replace("'", '"')
                l.write(replace)
                l.close()
                return True
        except Exception as e:
            raise SyntaxError(e)

    def load(self, languagaeName: str):
        """
This function can find language texts in saved language file, you must use :mod:`save()` before this function\n
Argument:\n
    languageName: the value in language list. The function will find the value you input,\n
    if it didn't find, the function retrun None, if it found the text, retrun the text 
"""
        with open(self.paths, 'r+', encoding='utf-8') as l:
            if self.paths[-5:] != '.json':
                raise TypeError('The type of language file must be ".json"')
            json_ = json.load(l)
            language_name = json_["languageSettings"]
            language_name = language_name[0]
            l.close()
            try:
                return language_name[languagaeName]
            except:
                return None

    def create(self):
        """
Create an empty language file in the paths
"""
        with open(self.paths, 'w', encoding='utf-8') as l:
            if self.paths[-5:] != '.json':
                raise TypeError('The type of language file must be ".json"')
            l.write(fileString)
            l.close()
            if self.paths not in languageList:
                languageList.append(self.paths)
            return True

    def delete(self) -> bool:
        """
Delete the language you saved
"""
        try:
            os.remove(self.paths)
            languageList.remove(self.paths)
            return True
        except:
            return False

    def dir() -> list:
        """
Return the list of the languages    
"""
        return languageList

    def delete_all():
        for i in range(len(languageList)):
            try:
                os.remove(languageList[i])
            except Exception as e:
                print(e)
        languageList.clear()

