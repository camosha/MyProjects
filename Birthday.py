""" Birthday Paradox Simulation"""
import datetime, random
def getBirthdays(numberOfBirthdays):
  #Returns a list of number random date objects for birthdays.
  birthdays = []
  for i in range(numberOfBirthdays):
    #This year is unimportant for our simulation
    startOfYear = datetime.date(2023,1,1)
    randomNumberOfDays = datetime.timedelta(random.randint(0,364))
    birthday = startOfYear + randomNumberOfDays
    birthdays.append(birthday)
  return birthdays
def getMatch(birthdays):
  """Returns the date object of a birthday that occurs more than once 
  in the Birthday list"""
  if len(birthdays) == len(set(birthdays)):
    return "None are Unique"
  for a, birthdayA in enumerate(birthdays):
    for b, birthdayB in enumerate(birthdays[a+1 :]):
      if birthdayA == birthdayB:
        return birthdayA
#Intro
print('Welcome to the birthday paradox. This paradox shows us that in a group of N people, the odds that two of them have matchin birthdays is surprisingly large This program does a Monte Carlo Simulation to explore this Concept')
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul',"Aug",'Sep', 'Oct', 'Nov', 'Dec')
while True: #Keep asking until the user enters a valid amount
      print('How many birthdays should i generate? (Max 100)')
      response = input(">>> ")
      if response.isdecimal() and (0 < int(response)<=100):
        numBdays = int(response)
        break
print()
#Generate and display the birthdays:
print("Here are", numBdays,'birthdays:')
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
  if i !=0:
    print(', ',end='')
monthName = MONTHS[birthday.month - 1]
dateText = '{} {}'.format(monthName, birthday.day)
print(dateText, end='')
print()
print()

 # Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
 monthName = MONTHS[match.month - 1]
 dateText = '{} {}'.format(monthName, match.day)
 print('multiple people have a birthday on', dateText)
else:
 print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
 94. # Report on the progress every 10,000 simulations:
 if i % 10_000 == 0:
  print(i, 'simulations run...')
 birthdays = getBirthdays(numBDays)
 if getMatch(birthdays) != None:
  simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
