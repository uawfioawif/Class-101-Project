import random

roll = 'y'

while roll == 'y':
  n = random.randint(1, 6)
  if n == 1:
    print('[-----]')
    print('[     ]')
    print('[  0  ]')
    print('[     ]')
    print('[-----]')
  if n == 2:
    print('[-----]')
    print('[     ]')
    print('[0   0]')
    print('[     ]')
    print('[-----]')
  if n == 3:
    print('[-----]')
    print('[     ]')
    print('[0 0 0]')
    print('[     ]')
    print('[-----]')
  if n == 4:
    print('[-----]')
    print('[0   0]')
    print('[     ]')
    print('[0   0]')
    print('[-----]')
  if n == 5:
    print('[-----]')
    print('[0   0]')
    print('[  0  ]')
    print('[0   0]')
    print('[-----]')
  if n == 6:
    print('[-----]')
    print('[0   0]')
    print('[0   0]')
    print('[0   0]')
    print('[-----]')
  roll = input("Do you want to roll again? ")