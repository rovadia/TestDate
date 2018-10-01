# testdate.py
# Part II: Regular Expressions 
import sys
import re

def main():
	print("testdate.py by Roei Ovadia and Jon Attia")
	if (len(sys.argv)==1):
		print("Usage: testdate.py file ...")
	else:	
		for i in sys.argv[1:]:
			#We'll loop through the files in the sys args. I just simplified it to one file below to make sure it works for one file before implementing multi-files. 
			f = open(i, 'r')
			strings = re.findall(r'(\d\d/\d\d/\d\d\d\d)|(\d\d/\d/\d\d\d\d)|(\d/\d\d/\d\d\d\d)|(\d/\d/\d\d\d\d)|(\d\d/\d\d/\d\d)|(\d\d/\d/\d\d)|(\d/\d\d/\d\d)|(\d/\d/\d\d)|(\d\d-\d\d-\d\d\d\d)|(\d\d-\d-\d\d\d\d)|(\d-\d\d-\d\d\d\d)|(\d-\d-\d\d\d\d)|(\d\d[.]\d\d[.]\d\d\d\d)|(\d\d[.]\d[.]\d\d\d\d)|(\d[.]\d\d[.]\d\d\d\d)|(\d[.]\d[.]\d\d\d\d)|(\d\d[.] \d\d[.] \d\d\d\d)|(\d\d[.] \d[.] \d\d\d\d)|(\d[.] \d\d[.] \d\d\d\d)|(\d[.] \d[.] \d\d\d\d)|(\d\d\d\d-\d\d-\d\d)|(\d\d\d\d-\d\d-\d)|(\d\d\d\d-\d-\d\d)|(\d\d\d\d-\d-\d)', f.read())
			#re.findall basically is the one function that encompasses multiple.. like compile/match/search,
			# without the need to read each file line by line, but each file in it's entirety.
			valid_dates = []
			#Save the valid dates to a list
			#print(strings)	
			for k in strings:
				for j in k:
					if len(j)>0:
						valid_dates.append(j)
			
			final_dates = []
			for k in valid_dates:
				valid=True
				if "/" in k: #every formatted date with a slash
					data=k.split('/') #split by slash
					month=int(data[0]) #month
					day=int(data[1]) #day
					year=int(data[2]) #year
				elif "." in k: #every formatted date with dot
					data=k.split('.') #split by dot
					day=int(data[0])
					month=int(data[1])
					year=int(data[2])
				elif "-" in k: #formatted with dash
					if len(data[0])>2:
						year=int(data[0])
						month=int(data[1])
						day=int(data[2])
					else:
						month=int(data[0])
						day=int(data[1])
						year=int(data[2])
				
				if month>12: 
					valid=False
				if day>31:
					valid=False
				if month==4 or month==6 or month==9 or month==11: #months with 30 days
					if day>30:
						valid=False
				if month==2: #february
					if day>29:
						valid=False
					if year % 4 !=0: #if not a leap year
						if day>28:
							valid=False
				if (len(str(year))>2):
					if year>2018 or year<1919:
						valid=False
				if valid==True: #printing the valid dates
					if len(str(year))>2: #4 digit years
						output=str(year)
					else:
						if (year>18):
							output="19"
						else:
							output="20"		
						output+=str(year)	
					output+='/'
					if (month<10):
						output+='0'
					output+=str(month)
					output+='/'
					if (day<10):
						output+='0'
					output+=str(day)
					final_dates.append(output)
			
			if (not final_dates):
				print(str(i) + " does not contain dates.")
			else :
				final_string=""
				for x in final_dates:
					final_string+=x
					final_string+=" "
				print(str(i) + " contains dates: " + str(final_string))
	


main()	
