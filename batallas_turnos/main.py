import random
from os import system, name 
from time import sleep 
from PyInquirer import prompt

class Game:
    def __init__(self):
        self.hero_life = 150
        self.vampire_life = 60
        self.game_over = False
        self.defense = False
        self.hero_fainted = False
        self.vampire_fainted = False
        self.potion_timeout = 0
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
        self.questions = [
            {
                'type': 'list',
                'name': 'game',
                'message': "What will the hero do?",
                'choices': [
                    "Use {}, AD: {}".format(self.weapons['hero'][0]['name'], self.weapons['hero'][0]['attack_damage']),
                    "Use {}, AD: {}".format(self.weapons['hero'][1]['name'], self.weapons['hero'][1]['attack_damage']),
                    "Use {}, AD: {}".format(self.weapons['hero'][2]['name'], self.weapons['hero'][2]['attack_damage']),
                    "Use potion",
                    "Defend herself",
                ],
            }
        ]

    def vampire_attacks(self, answer):
        choice = random.choice(self.weapons['vampire'])
        print("Vampire uses {}!".format(choice['name']))
        if choice['accuracy'] == 90/100:
            striked = random.randint(1, 100)

            if striked <= 90:
                damage = None
                attack_damage = None

                if self.defense:
                    attack_damage = choice['attack_damage'] - 5
                    damage = self.hero_life - attack_damage
                    self.hero_life = damage
                else:
                    damage = self.hero_life - choice['attack_damage']
                    attack_damage = choice['attack_damage']
                    self.hero_life = damage

                print("Vampire inflicts {} damage to the Hero!".format(attack_damage))
        elif choice['accuracy'] == 60/100:
            striked = random.randint(1, 100)

            if striked <= 60:
                damage = None
                attack_damage = None

                if self.defense:
                    attack_damage = choice['attack_damage'] - 5
                    damage = self.hero_life - attack_damage
                    self.hero_life = damage
                else:
                    attack_damage = choice['attack_damage']
                    damage = self.hero_life - choice['attack_damage']
                    self.hero_life = damage

                print("Vampire inflicts {} damage to the Hero!".format(attack_damage))
        elif choice['accuracy'] == 40/100:
            striked = random.randint(1, 100)

            if striked <= 40:
                damage = None
                attack_damage = None

                if self.defense:
                    attack_damage = choice['attack_damage'] - 5
                    damage = self.hero_life - attack_damage
                    self.hero_life = damage
                else:
                    attack_damage = choice['attack_damage']
                    damage = self.hero_life - choice['attack_damage']
                    self.hero_life = damage

                print("Vampire inflicts {} damage to the Hero!".format(attack_damage))
        return 

    def hero_attacks(self, answer):
        success = random.randint(1, 100)
        damage = None
        attack_damage = None

        if answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][0]['name'], self.weapons['hero'][0]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][0]['name']))

            if success <= 50:
                attack_damage = self.weapons['hero'][0]['attack_damage']
                self.vampire_life = self.vampire_life - attack_damage
                
                print("The hero inflicts {} damage to the Vampire!".format(attack_damage))

        elif answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][1]['name'], self.weapons['hero'][1]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][1]['name']))

            if success <= 25:
                attack_damage = self.weapons['hero'][1]['attack_damage']
                self.vampire_life = self.vampire_life - attack_damage
                
                print("The hero inflicts {} damage to the Vampire!".format(attack_damage))

        elif answer['game'] == "Use {}, AD: {}".format(self.weapons['hero'][2]['name'], self.weapons['hero'][2]['attack_damage']):
            print("Hero uses {}!".format(self.weapons['hero'][2]['name']))

            if success <= 12:
                attack_damage = self.weapons['hero'][2]['attack_damage']
                self.vampire_life = self.vampire_life - attack_damage
                
                print("The hero inflicts {} damage to the Vampire!".format(attack_damage))

        elif answer['game'] == 'Use potion': 
            self.potion_timeout = 4
            print("Hero uses {}!".format(self.weapons['hero'][3]['name']))
            sleep(2)
            print("The hero will recover all its health in the near future... But her abilities are unusuable for a while...")

        elif answer['game'] == 'Defend herself':
            print("Hero uses {}!".format(self.weapons['hero'][4]['name']))

            if success <= 80:
                self.defense = True
                print("The heroe reduces the attack damage of the vampire by 5!")
        return

def clear_screen():
    if name == 'nt': 
        system('cls') 
  
    else: 
        system('clear')

def defeated():
    clear_screen()
    print('The vampire has murdered the hero...')
    sleep(2)
    clear_screen()
    print('Now the town faces a great danger...')
    sleep(2)
    clear_screen()
    print('Game over!')
    clear_screen()
    game.game_over = True

def won():
    clear_screen()
    print('The hero has defeated the vampire!')
    sleep(2)
    clear_screen()
    print('Now the town is safe, for a least one more day...')
    sleep(3)
    clear_screen() 
    game.game_over = True

if __name__ == '__main__':
    clear_screen()
    game = Game()

    while game.game_over != True:
        if game.hero_life <= 30:
            game.hero_fainted = True
        
        if game.vampire_life <= 20:
            game.vampire_fainted = True

        if game.hero_life <= 0:
            defeated()
            break

        if game.vampire_life <= 0:
            won()
            break

        if game.potion_timeout > 1:
            game.potion_timeout = game.potion_timeout - 1

        elif game.potion_timeout == 1:
            game.potion_timeout = 0
            game.hero_life = 150

            clear_screen()
            print("The hero has recovered all her health!")
            sleep(2)
            clear_screen()


        print("Hero's healt: {} | Vampire's healt: {}".format(game.hero_life, game.vampire_life))

        answer = prompt(game.questions)

        clear_screen()

        game.defense = False

        if game.potion_timeout == 0:
            game.hero_attacks(answer)
        elif game.hero_fainted:
            game.hero_life = game.hero_life + 2
            print("The hero is passed out... But slowly recovering...")
            sleep(2)

        if game.vampire_fainted:
            game.vampire_life = game.vampire_life + 2
            if game.vampire_life >= 20:
                game.vampire_fainted = False

                print("The vampire has awaken again!")
                sleep(2)
            else:
                print("The vampire is passed out... But slowly recovering...")
                sleep(2)
        else:
            game.vampire_attacks(answer)

        sleep(2)

        clear_screen()

    clear_screen()

    system('exit')    
