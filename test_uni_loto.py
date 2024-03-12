import unittest
from loto import Card, play_game
import numpy as np
import mock
import builtins

class TestLoto(unittest.TestCase):
    def test_init(self):
        card = Card()
        print(card.user_card.shape)
        self.assertEqual(card.user_card.shape, (3, 9))
        self.assertEqual(card.name_card, '')


    def test_generate_card(self):
        card = Card()
        res = card.generate_card()
        print(res, np.sum(res))
        self.assertGreater(np.sum(res), 0)

    def test_answer_people(self):
        game = play_game()
        # rea = game.answer_people([80])
        # self.assertEqual(res, 1)
        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            assert game.answer_people([[80]]) == 1
        with mock.patch.object(builtins, 'input', lambda _: 'Y'):
            assert game.answer_people([[]]) == 0
        with mock.patch.object(builtins, 'input', lambda _: 'N'):
            assert game.answer_people([[80]]) == 0
        with mock.patch.object(builtins, 'input', lambda _: 'N'):
            assert game.answer_people([[]]) == 1


    def test_str1(self):
        card = Card()
        with mock.patch.object(builtins, 'print', lambda _: card):
            assert card.__str__() != None

    def test_str2(self):
        game = play_game()
        with mock.patch.object(builtins, 'print', lambda _: game):
            assert game.__str__() == 'Вы играете в игру лото, созданную Полещенко Д.'