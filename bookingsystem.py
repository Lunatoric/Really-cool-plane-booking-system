
import string
# haha yolo! asmr is cool aaaaaaaa
class plane: #Create a dedicated plane class, allowing multiple planes.
  def __init__(self):
    self.businessclass = [['X', 'X', 'X', 'X', '', '', '', ''], # The seats as given
                         ['X', 'X', 'X', 'X', 'X', '', '', ''],
                         ['X', 'X', 'X', 'X', 'X', 'X', 'X', ''],
                         ['', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '']]
    self.economyclass = [['X', 'X', 'X', 'X', '', '', '', 'X', 'X', ''], # The seats as given
                         ['X', 'X', 'X', 'X', 'X', '', '', '', '', ''],
                         ['X', 'X', 'X', 'X', 'X', 'X', 'X', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', ''],
                         ['', '', '', '', '', '', '', '', '', '']]
  def economyclassadd(self, numpeople):
    if numpeople > 4: # If too many send a response saying too many
      return 400
    spots = [] # The seating locations
    if numpeople == 1: # If it's only one hunt down that spot
      for int1, i in enumerate(self.economyclass): # Iterate through each row
        for int2, x in enumerate(i): # Iterate through each seat
          if x == "": # Found a seat
            x = "X" # Mark the seat
            spot = str(string.ascii_uppercase[int1 + 5] + int2) # Turn the spot into a location
            spots.append(spot) # Append the spot to the spots list
            return spots # Finish the method and return the spot
    for int1, i in enumerate(self.economyclass): # Enumerate through the rows
      for index0, x in enumerate(i): # Enumerate through the chairs
        if (10 - index0) <= numpeople: # If the chair is Too close to the wall
          pass # Passes (Prevents Overflow errors)
        elif x == "": # If the chair is empty
          available = True # Show there's a possible chair here
          for y in range(numpeople): # Check to see if the
            if i[y+index0] == "X": # Next amount of chairs necessary are free
              available = False # If they aren't, unavailable
          if available == True: # If they are
            for y in range(numpeople): # Mark that chair
              i[y+index0] = "X" # Mark it
              spot = string.ascii_uppercase[int1 + 5] + str(y+index0) # Save the spot
              spots.append(spot) # Append the spot
            return spots # Return the spot
    return 200 # If something goes wrong

  def businessclassadd(self, numpeople): # Refer to the previous
    if numpeople > 4:
      return 400
    spots = []
    if numpeople == 1:
      for int1, i in enumerate(self.businessclass):
        for int2, x in enumerate(i):
          if x == "":
            x = "X"
            spot = str(string.ascii_uppercase[int1] + int2)
            spots.append(spot)
            return spots

    for int1, i in enumerate(self.businessclass):
      for index0, x in enumerate(i):
        if (8 - index0) < numpeople:
          pass
        elif x == "":
          available = True
          for y in range(numpeople):
            if i[y+index0] == "X":
              available = False
          if available == True:
            for y in range(numpeople):
              i[y+index0] = "X"
              spot = string.ascii_uppercase[int1] + str(y+index0)
              spots.append(spot)
            return spots
    return 200
Airliner380 = plane() # Declare the plane
planetype = input("Are you flying Economy (A), Or Business (B) - A/B") # Determine how they're flying
while planetype not in "AB": # If it Doesn't fit Tell them
  planetype = input("Sorry, Try Again. \b Are you flying Economy (A), Or Business (B) - A/B ") # TELL THEM
passengeramt = int(input("And How many are Flying? (Less than 4) - ")) # Ensure it's less than 4
while int(passengeramt) > 4:
  passengeramt = int(input("A number, less than 4. How many are Flying? - "))
if planetype == "A": # If it's economy
  seats = Airliner380.economyclassadd(passengeramt) # Add Economy
else:
  seats = Airliner380.businessclassadd(passengeramt) # Else add business
response = "Your seats are" # Ready the response
for i in seats:
  response += " " + i # Add their seats
if i == 200:
  response = f"Sorry, We are unable to fit {passengeramt}, please try a smaller amount" # Incase it failed
print(response) # Tell them their seats
