import random
import numpy as np

class Card():
    def __init__(self):
        self.user_card = np.zeros((3, 9))
        self.user_card = self.generate_card()
        self.name_card = ''

    def generate_card(self):
        for j in range(3):
            flag = np.zeros(10)
            while np.sum(flag) < 5:
                rand_kegs = random.randint(1, 90)
                if rand_kegs in self.user_card:
                    continue
                # print(rand_kegs)
                if rand_kegs < 10:
                    flag[0] = 1
                    self.user_card[j][0] = rand_kegs
                elif rand_kegs == 90:
                    flag[9] = 1
                    self.user_card[j][8] = rand_kegs
                else:
                    rand_kegs = str(rand_kegs)
                    flag[int(rand_kegs[0])] = 1
                    self.user_card[j][int(rand_kegs[0])] = rand_kegs
        return self.user_card

    def visual_card(self):
        self.user_card[0][5] = -1
        print(self.name_card)
        print(self.user_card)


class Play_game():
    user_card = None
    komp_card = None

    def __init__(self):
        self.all_kegs = list(range(1, 91))
        self.user_card = Card()
        self.komp_card = Card()

    def answer_people(self, find_kegs_user):
        answer = input('Зачеркнуть цифру? Y/N')
        if answer == 'Y' and len(find_kegs_user[0]) >= 1:
            return 1
        if answer == 'Y' and len(find_kegs_user[0]) < 1:
            return 0
        if answer == 'N' and len(find_kegs_user[0]) >= 1:
            return 0
        if answer == 'N' and len(find_kegs_user[0]) < 1:
            return 1

    def play_round(self):
        if len(self.all_kegs) >= 1:
            rand_kegs = random.sample(self.all_kegs, 1)
            # print(self.all_kegs)
            rand_kegs_index = self.all_kegs.index(rand_kegs[0])
            del self.all_kegs[rand_kegs_index]
            print(f'выпал бочонок {rand_kegs}, осталось {len(self.all_kegs)} бочонков')
            find_kegs_user = np.where(rand_kegs == self.user_card.user_card)
            find_kegs_comp = np.where(rand_kegs == self.komp_card.user_card)
            print('Твоя карта')
            print(self.user_card.user_card)
            print('Карта компьютера')
            print(self.komp_card.user_card)
            if self.answer_people(find_kegs_user):
                if len(find_kegs_user[0]) >= 1:
                    print(find_kegs_user[0][0], find_kegs_user[1][0])
                    self.user_card.user_card[find_kegs_user[0][0]][find_kegs_user[1][0]] = -1
            else:
                return 2
            if len(find_kegs_comp[0]) >= 1:
                print(find_kegs_comp[0][0], find_kegs_comp[1][0])
                self.komp_card.user_card[find_kegs_comp[0][0]][find_kegs_comp[1][0]] = -1

        if np.sum(self.user_card.user_card) == -15:
            return 1
        elif np.sum(self.komp_card.user_card) == -15:
            return 2

        return 0


if __name__ == '__main__':
    game = Play_game()
    while True:
        res = game.play_round()
        print(res)
        if res == 1:
            print('Вы выиграли')
            break
        if res == 2:
            print('Вы проиграли')
            break

