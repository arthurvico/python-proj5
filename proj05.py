##############################################################################
#       CSE 231 Project #5
#       In this project, I will be given a file from which I will extract
#       information and calculate growth rates and maximums
#       1) The main function will contain everything
#       2) I will use the open_file function to open a valid file
#       3) Print_headers to print the headers of the file
#       4) calc_delta to calculate the delta of my lines
#       5) format_display_line to display my results in a certian format
#       6) I will use all these functions and their return values
#       to create my program
##############################################################################

def open_file():
    '''This function will be used to open a given file and make sure that it is a valid file'''
    #create a try and except logic to get a correct file
    while True:
        try:
            #try to open the file here
            file_name = input("Enter a file name: ")
            file_open = open(file_name, "r")
            return file_open
        except:
            #if error, try again
            print("Error. Please try again.")
    
def print_headers():
    '''This function will print the headers when outputing our results'''
    #Format the headers in the correct order
    print("{:>43s}".format("Maximum Population Change by Continent"))
    print("")
    print("{:<26s}{:>9s}{:>10s}".format("Continent","Years","Delta"))
    

def calc_delta(line,col):
    '''This function will take a line of population for different continents and
    different year brackets and calculate the growth rate between each 50 year bracket'''
    #Set an offset value to use later
    a = 0
    #Multiple if statements to get correct offset. Offset will be used to get the different values from the line
    if col == 1:
        a = 0
    if col == 2:
        a = 6
    if col == 3:
        a = 12
    if col == 4:
        a = 18
    if col == 5:
        a = 24
    if col == 6:
        a = 30
    #Get your 2 numbers from the line, with the offsets
    number_1 = float(line[17+a:21+a])
    number_2 = float(line[23+a:27+a])
    #Calculate your delta
    delta = (number_2-number_1)/number_1
    #Return value is the delta
    return delta


def format_display_line(continent,years,delta):
    '''This will format the end result. As in it will take our calculated outputs
    and print them in a way that is formated correctly'''
    #Calculate the lower year from the higher year to get a correct format output
    years_lower = years-50
    years_lower_str = str(years_lower)
    years = str(years)
    years_bracket = years_lower_str+"-"+years
    continent = str(continent)
    #Calculate the max delta in percentage
    delta_perc = (delta*100)
    #Round the percentage value to 0 decimals and also make it an int to get rid of .0
    delta_int = int(round(delta_perc,0))
    #Make the delta value a str for printing
    delta = str(delta_int)
    delta = (delta+"%")
    #format the display line so that everything displays correctly
    print("{:<26s}{:>9s}{:>10s}".format(continent,years_bracket,delta))
    display = "{:<26s}{:>9s}{:>10s}".format(continent,years_bracket,delta)
    return display
    
    

def main():
    '''This is the heart of the code. Every function will be used in here with
    each other and this function will be called to display the whole code'''
    #use the open_file function
    file_open = open_file()
    #create a for loop to get rid of the first two lines
    for i in range(2):
        #strip the header
        header = file_open.readline().strip()
    #use the print_header function to print my headers
    print_headers()
    #Create a for loop to calculate the delta of each line
    delta_abs_max = 0
    for line in file_open:
        #strip the line (This is for easier printing towards the end)
        line_stripped = line.strip()
        #Initialize a delta_max value
        delta = 0
        continent = line_stripped[0:15]
        #Create a for loop to get every single column value tested
        for col in range(1,7):
            #Call the calc_delta function to calculate my delta value
            delta_all = calc_delta(line,col)
            #Create an if statement to get a max delta value
            if delta_all > delta:
                #set an equality if the if statement is satisfied
                delta = delta_all
                #Calculate the highest year that the max happened
                years = 1750 +(col*50)
                #Create an if statement to get the absolute max of every given interval
                if delta > delta_abs_max:
                    #Set an euqality if the if statement is satisfied
                    delta_abs_max = delta
                    #Calculate the max year where the absolute max happened
                    years_abs_max = 1750+(col*50)
                    max_continents = line[1:16]
        #Create a for loop to get the continents of each line
        #for i in range (6):
            #Here we extract the characters where the continent is imbeded
            continent = line_stripped[0:13]
        #Call the format_display_line function to print everything correctly
        display = format_display_line(continent,years,delta)
        #Print an empty line
    #Print the maximum of all continents line
    print("\nMaximum of all continents:")
    #Change the absolute max to a percentage
    delta_abs_max_perc = (delta_abs_max*100)
    #Round the percentage value to no decimal and change it to an integer to get rid of the .0
    delta_abs_int = int(round(delta_abs_max_perc,0))
    #Change the value to a string for printing
    delta_abs = str(delta_abs_int)
    #Calculate the lower year of the absolute max
    years_abs_min = years_abs_max-50
    #change that value and the max year to a string for printing
    years_abs_max_str = str(years_abs_max)
    years_abs_min_str = str(years_abs_min)
    #Create a string for the year bracket for the absolute max
    years_abs_all = years_abs_min_str+"-"+years_abs_max_str
    #Format the printing for the highest of all continents
    print("{:<26}{:>9s}{:>10s}".format(max_continents,years_abs_all,delta_abs+"%"))
    file_open.close()
        
if __name__ == "__main__":
    main()