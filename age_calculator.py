from datetime import datetime

def check_birthdate(year, month, day):
	# write code here
	year = int(year)
	month = int(month)
	day = int(day)
	birth_date = datetime(year,month,day)
	if birth_date <= datetime.today():
		return True
	elif birth_date > datetime.today():
		return False


def calculate_age(year, month, day):
    # write code here
	year = int(year)
	month = int(month)
	day = int(day)
	today = datetime.today()

	if month < today.month or (month == today.month and day < today.day):
		age = today.year - year
	else:
		age = today.year - year - 1

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
