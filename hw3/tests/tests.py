import unittest
from flash_cards import FlashCards
from unittest.mock import patch


class FlashCardsTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = FlashCards('file.json')

    # тестируем поведение add_word при неподходящих входных данных
    def test_flashcards_incorrect_add_word_input(self):
        for name, parsed_name in [
            (('watermelon', 'watermelon'), ('Russian and english words are expected')),
            (('яблоко', 'apple'), ('яблоко already in the dictionaty')),
            (('арбуз', 'watermelon'), ('Succesfully added word арбуз')),
            ((123, 123), ('Russian and english words are expected'))]:
            self.assertEqual(self.parser.add_word(name[0], name[1]), parsed_name)

    # тестируем поведение delete_word при неподходящих входных данных
    def test_flashcards_incorrect_delete_word_input(self):
        for name, parsed_name in [
            ('watermelon', 'Cyrillic word is expected'),
            ('виноград', 'виноград not in the dictionary'),
            ('яблоко', 'яблоко succesfully deleted'),
            (123, 'Cyrillic word is expected')]:
            self.assertEqual(self.parser.delete_word(name), parsed_name)

    # тестируем попытку удалить слово при пустом словаре
    def test_flashcard__empty_dictionary(self):
        words = ['яблоко', 'хурма']
        for word in words:
            self.parser.delete_word(word)
        self.assertEqual(self.parser.play(), 'Dictionary is empty!')
        self.assertEqual(self.parser.delete_word('яблоко'), 'Dictionary is empty!')

    # тестируем атрибут words
    def test_flashcard_words(self):
        self.assertEqual(self.parser._words, ['яблоко', 'хурма'])

    # тестируем play() когда 1 из всех слов точно верно
    @patch('builtins.input', return_value='apple')
    def test_flashcard_play1(self, mock_input):
        result = self.parser.play()
        self.assertEqual(result, 'Done! 1 of 2 words correct.')

    # тестируем play() когда слово точно неверно
    @patch('builtins.input', return_value='watermelon')
    def test_flashcard_play2(self, mock_input):
        result = self.parser.play()
        self.assertEqual(result, 'Done! 0 of 2 words correct.')


# запустить все тесты
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
