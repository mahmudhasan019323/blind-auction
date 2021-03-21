logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print('Welcome to the secret auction program.')

users = {}

def secret_aution():
  user_name = input("What is your name? ")
  user_bid = int(input("What's your bid? $"))
  other_bidders = input("Are there other biddera? Type 'yes' or 'no'. \n").lower()
  users[user_name] = user_bid
  if other_bidders == "yes":
    print('\033c')
    secret_aution()
  else:
    winner = max(users, key=users.get)
    print(f'The winner is {winner} with a bid of ${users[winner]}')
secret_aution()
