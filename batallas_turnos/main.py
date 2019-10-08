import random
from PyInquirer import prompt

class Game:
    def __init__(self):
        self.hero_life = 150
        self.vampire_life = 60
        self.game_over = True
        self.questions = [
            {
                'type': 'list',
                'name': 'game',
                'message': "What will the hero do? | HP: {}".format(self.hero_life),
                'choices': [
                    "Use {}, AD: {}".format(self.weapons['hero'][0]['name'], self.weapons['hero'][0]['attack_damage']),
                    "Use {}, AD: {}".format(self.weapons['hero'][1]['name'], self.weapons['hero'][1]['attack_damage']),
                    "Use {}, AD: {}".format(self.weapons['hero'][2]['name'], self.weapons['hero'][2]['attack_damage']),
                    "Use potion",
                    "Defend herself",
                ],
            }
        ]
        self.weapons = {
            'hero': [ 
                {
                    'name': "Punch",
                    'attack_damage': 7,
                    'accuracy': 50/100,
                },
                {
                    'name': "Basic sword",
                    'attack_damage': 15,
                    'accuracy': 25/100,
                },
                {
                    'name': "Hero's sword",
                    'attack_damage': 30,
                    'accuracy': 12/100,
                },
                {
                    'name': "Shield",
                    'accuracy': 80/100,
                },
                {
                    'name': "Potion",
                },
                {
                    'name': "Hero's shield"
                }
            ],
            'vampire': [
                {
                    'name': "Vampire punch",
                    'attack_damage': 5,
                    'accuracy': 90/100,
                },
                {
                    'name': "Blood steal",
                    'attack_damage': 10,
                    'accuracy': 60/100,
                },
                {
                    'name': "Bloody Marie's blood sword",
                    'attack_damage': 20,
                    'accuracy': 40/100,
                }
            ]
        }

    def vampire_attacks(self, answer):
        choice = random.choice(self.weapons['vampire'])
        print("Vampire uses {}".format(choice['name']))
        if choice['accuracy'] == 90/100:
            striked = random.randint(90, 100)

            if striked * choice['accuracy'] == 90:
                self.hero_life = self.hero_life - choice['attack_damage']
                print("Vampire inflicts {} damage to the Hero!".format(choice['attack_damage']))
        elif choice['accuracy'] is 60/100:
            return
        elif choice['accuracy'] is 40/100:
            return
        return 

    def hero_attacks(self, answer):
        if answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][0]['name'], self.weapons['hero'][0]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][0]['name']))
        elif answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][1]['name'], self.weapons['hero'][1]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][1]['name']))
        elif answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][2]['name'], self.weapons['hero'][2]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][2]['name']))
        elif answer['game'] == 'Use potion': 
            print("Hero uses {}!".format(self.weapons['hero'][3]['name']))
        elif answer['game'] == 'Defend herself':
            print("Hero uses {}!".format(self.weapons['hero'][5]['name']))
        return

if __name__ == '__main__':
    game = Game()

    while game.game_over is not True or vampire_life == 0 or hero_life == 0:
        answer = prompt(questions)
        hero_attacks(answer)
        vampire_attacks(answer)
