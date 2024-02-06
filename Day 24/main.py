with open('Day 24/input/letters/starting_letter.txt') as starting_letter:

  letter = starting_letter.read()
  names  = open('Day 24/input/names/names.txt').readlines()
  
  for i, name in enumerate(names):

    if i != len(names)-1:
      name= name[:-1] 

    with open(f'Day 24/output/ready_to_send/letter_for_{name}', mode='w') as sending_letter:
      dummy_letter = letter
      sending_letter.write(dummy_letter.replace('[name]', name))

