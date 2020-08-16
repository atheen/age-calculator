from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	year = int(year)
	if year < 2019 :
		return True
	elif year > 2019 :
		return False
	elif year == 2019:
		if month < 9:
			return True
		elif month > 9:
			return False
		elif month == 9:
			if day <= 4:
				return True
			elif day > 4:
				return False

def calculate_age(year, month, day):
    # write code here
	month = int(month)
	day = int(day)
	if month < 9:
		age = 2019 - int(year)
	elif month > 9:
		age = 2019 - int(year) - 1
	elif month == 9:
		if day <= 4:
			age = 2019 - int(year)
		elif day > 4:
			age = 2019 - int(year) - 1
	print("You are %d years old."%(age))

def main():
	# write main code here
	birth_year = input("Enter year of birth: ")
	birth_month = input("Enter month of birth: ")
	birth_day = input("Enter day of birth: ")
	if check_birthdate(birth_year,birth_month,birth_day) == True:
		calculate_age(birth_year,birth_month,birth_day)
	else:
		print("invalid birthdate")


if __name__ == '__main__':
	main()
