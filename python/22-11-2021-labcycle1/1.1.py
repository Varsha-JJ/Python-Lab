print("Leap year between two year")
print("Enter the current year:")
curr_year = int(input())
print("Enter the final year:")
final_year = int(input())

print("Leap year between current and final years are:")
for year in range(curr_year, final_year):
   if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
      print(int(year))


