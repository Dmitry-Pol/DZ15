import unittest
from loto import Card, Play_game
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
        game = Play_game()
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



