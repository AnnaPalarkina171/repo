import json
import random
import re


class FlashCards():
    def __init__(self, path_to_file: str):
        '''
        Прочитает пары слов из указанного файла в формате json.
        Создаст все требующиеся атрибуты.
        '''
        with open("file.json", "r") as read_file:
            self.__data = json.load(read_file)
            self._words = list(self.__data.keys())

    def play(self) -> str:
        '''
        Выдает русские слова из словаря в рандомном порядке,
        сверяет введенный пользователем перевод с правильным
        (регистр введенного слова при этом не важен),
        пока слова в словаре не закончатся.
        Возвращает строку с количеством правильных ответов/общим количеством
        слов в словаре (см пример работы).
        '''

        right = 0
        play_data = self.__data
        if play_data != {}:
            rus_list = list(play_data.keys())
            random.shuffle(rus_list)
            for rus_word in rus_list:
                print('Word: ', rus_word)
                eng_word = input('Translation: ')
                if eng_word.lower() == play_data[rus_word]:
                    right += 1
            return 'Done! {} of {} words correct.'.format(right, len(rus_list))
        if play_data == {}:
            return "Dictionary is empty!"

    def add_word(self, russian: str, english: str) -> str:
        '''
        Добавляет в словарь новую пару слов,
        если русского слова еще нет в словаре.
        Возвращает строку в зависимоти от результата (см пример работы).
        '''
        match_rus = re.match("^[а-яА-ЯёЁ]", str(russian))
        match_eng = re.match("^[a-zA-Z]", str(english))
        if bool(match_rus) == True and bool(match_eng) == True:
            if russian not in self.__data:
                self.__data[russian] = english
                self._words.append(russian)
                return 'Succesfully added word {}'.format(russian)
            else:
                return '{} already in the dictionaty'.format(russian)
        else:
            return 'Russian and english words are expected'

    def delete_word(self, russian: str) -> str:
        '''
        Удаляет из словаря введенное русское слово
        и соответсвующее ему английское.
        Возвращает строку в зависимоти от результата (см пример работы).
        '''
        match = re.match("^[а-яА-ЯёЁ]", str(russian))
        if bool(match):
            if self.__data != {}:
                if russian not in self.__data:
                    return '{} not in the dictionary'.format(russian)
                else:
                    del self.__data[russian]
                    self._words.remove(russian)
                    return '{} succesfully deleted'.format(russian)
            else:
                return 'Dictionary is empty!'
        else:
            return 'Cyrillic word is expected'

# if __name__ == '__main__':
#    fc = FlashCards('file.json')
