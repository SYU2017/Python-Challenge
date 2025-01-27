# python-challenge
# Assignment - Py Me Up, Charlie

# Option 1: PyBank
   *In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given   two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue.
   *Your task is to create a Python script that analyzes the records to calculate each of the following:

       The total number of months included in the dataset
       The total amount of revenue gained over the entire period
       The average change in revenue between months over the entire period
       The greatest increase in revenue (date and amount) over the entire period
       The greatest decrease in revenue (date and amount) over the entire period
       
       
 # Option 2: PyPoll
   *In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
   *You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
   *Your final script must be able to handle any such similarly-structured dataset in the future. In addition, your final script should both print the analysis to the terminal and export a text file with the results.

     The total number of votes cast
     A complete list of candidates who received votes
     The percentage of votes each candidate won
     The total number of votes each candidate won
     The winner of the election based on popular vote.
     
# Option 3: PyBoss
   * In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

   *Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format.
   *Insummary, the required conversions are as follows:
        
        The Name column should be split into separate First Name and Last Name columns.
        The DOB data should be re-written into DD/MM/YYYY format.
        The SSN data should be re-written such that the first five numbers are hidden from view.
        The State data should be re-written as simple two-letter abbreviations.
          
                  
# Option 4: PyParagraph
   * In this challenge, you get to play the role of chief linguist at a local learning academy. As chief linguist, you are responsible for assessing the complexity of various passages of writing, ranging from the sophomoric Twilight novel to the nauseatingly high-minded research article. Having read so many passages, you've since come up with a fairly simple set of metrics for assessing complexity.

   *Your task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:

    Import a text file filled with a paragraph of your choosing.
     Assess the passage for each of the following:
     Approximate word count
     Approximate sentence count
     Approximate letter count (per word)
     Average sentence length (in words)
     
* Special Hint: this code snippet is helpful when determining sentence length (look into regular expressions if interested in learning more):
import re
re.split("(?&lt;=[.!?]) +", paragraph)

   
