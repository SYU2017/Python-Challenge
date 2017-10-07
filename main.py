import os
import csv
import datetime

employee_csv = os.path.join("..", "Resources", "employee_data2.csv")

Emp_ID = []
First_Name= []
Last_Name = []
DOB = []
SSN = []
State = []
us_state_abbrev = {
          'Alabama': 'AL',
          'Alaska': 'AK',
          'Arizona': 'AZ',
          'Arkansas': 'AR',
          'California': 'CA',
          'Colorado': 'CO',
          'Connecticut': 'CT',
          'Delaware': 'DE',
          'Florida': 'FL',
          'Georgia': 'GA',
          'Hawaii': 'HI',
          'Idaho': 'ID',
          'Illinois': 'IL',
          'Indiana': 'IN',
          'Iowa': 'IA',
          'Kansas': 'KS',
          'Kentucky': 'KY',
          'Louisiana': 'LA',
          'Maine': 'ME',
          'Maryland': 'MD',
          'Massachusetts': 'MA',
          'Michigan': 'MI',
          'Minnesota': 'MN',
          'Mississippi': 'MS',
          'Missouri': 'MO',
          'Montana': 'MT',
          'Nebraska': 'NE',
          'Nevada': 'NV',
          'New Hampshire': 'NH',
          'New Jersey': 'NJ',
          'New Mexico': 'NM',
          'New York': 'NY',
          'North Carolina': 'NC',
          'North Dakota': 'ND',
          'Ohio': 'OH',
          'Oklahoma': 'OK',
          'Oregon': 'OR',
          'Pennsylvania': 'PA',
          'Rhode Island': 'RI',
          'South Carolina': 'SC',
          'South Dakota': 'SD',
          'Tennessee': 'TN',
          'Texas': 'TX',
          'Utah': 'UT',
          'Vermont': 'VT',
          'Virginia': 'VA',
          'Washington': 'WA',
          'West Virginia': 'WV',
          'Wisconsin': 'WI',
          'Wyoming': 'WY' }


with open(employee_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        Emp_ID.append(row[0])
        first = row[1].split( )[0]
        last = row[1].split( )[1]
        First_Name.append(first)
        Last_Name.append(last)
      
        newdate=row[2].datetime.strptime("2017-1-25", '%Y-%m-%d').strftime('%-m/%d/%y') 
        DOB.append(newdate)
        newSSN="*" * (len(raw[3]) - 4) + raw[3][-4:]
        SSN.append(newSSN)
        
        newstate = us_state_abbrev.get(row[4].upper(), "")

        State.append(newstate)

cleaned_csv = zip(Emp_ID, First_Name, Last_Name, DOB, SSN, State )
print(cleaned_csv)
# Set variable for output file
output_file = os.path.join("employee_final.csv")
#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write the header row
    writer.writerow(["Emp_ID", "First_Name", "Last_Name", "DOB", "SSN", "State"])
    # Write in zipped rows
    writer.writerows(cleaned_csv)
