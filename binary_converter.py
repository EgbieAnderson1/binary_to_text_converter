###############################################################################
# Binary To Text and a Text to Binary converter
# Started on sun 27  13:12:18 hrs
# Finished on Tuesday 14:56:18 hrs
# Updated on Wed 30 April 2014 15:00 hrs
# Language python 2.7
# created by Egbie Anderson
 
# A simple program in which text is entered by the user. Depending on the users choice
# within the menu the text is either converted to binary or into to text
#
# This program works by reading and writing files from and to a hard drive
# The program was written in python in 2.7x and therefore will not work in python 3.x series
#
# Licence < free>
# Operating System <any>
# All rights 2014
# Copy right <None>
###############################################################################
 
# built in python modules
import os
import sys
import webbrowser
from time import sleep
from platform import system
 
########################################################################
# Operating System class
########################################################################
class OperatingSystem(object):
    '''Responsible for all things that has to with the operating system'''
   
    def get_operating_system(self):
        '''returns the user operating system'''
        return system()
 
    def get_current_path(self):
        '''return the current file path'''
        return os.getcwd()
 
    def join_path(self, file_name):
        '''takes a file name and concatenate it with the current directory path'''
        return (os.path.join(self.get_current_path(), file_name))
 
    def command(self, command, file_path):
        '''performs a specific command on the operating system'''
        os.system('%s %s' %(command, file_path))
 
########################################################################
# InputOutput class
########################################################################
class InputOutput(object):
    """The class is responsible for anything that involves retreiving or storing information
   to a hard drive
   """
    def load(self, file_path):
        '''load(str) -> return(str)
 
       Takes a file or a file path and loads it into memory
       '''
        try:
            self.file = open(file_path, "r")
        except IOError:
            print "[!] File not found, closing program"
            exit(0)
        else:
            self.out_file = self.file.readlines()
            self.file.close()
            return self.out_file
           
    def create_text_file(self, filename, info_to_be_written, mode = 'w'):
        """creates a text file or a clipboard and then writes information to that file"""
 
        self.files = open(filename, mode)
        self.files.write(info_to_be_written)
        self.files.write("\n")
        self.files.close()
 
########################################################################
# Converter class
########################################################################
class Converter(object):
    '''responsible for converting data from one thing to another'''
 
    # private function
    def _add_padding(self, bin_str, padding=8):
        '''add_padding(int) -> return(int)
 
       Takes a binary string and checks if the length of that
       the string is 8. If True the binary string is returned and
       if False the binary string is padded with 0 until the length
       is 8. This ensures the method is working with bytes.
 
       >>> _add_padding(10)
       00000010
 
       >>> _add_padding(11110000)
       11110000
       '''
        # return the str if str is of length eight
        if len(bin_str) == padding:
            return bin_str
 
        # add padding if the string does not meet the right specification
        while len(bin_str) < padding:
            bin_str = "0" + bin_str
         
        return bin_str
 
    def convert_to_binary(self, message):
        '''convert_to_binary(void) -> return(str)
 
       Takes a string and returns it binary representation
 
       >>> convert_to_binary("Shannon Morse)
       '01010011011010000110000101101110011011100110111
       101101110001000000100110101101111011100100111001101100101'
 
       >>> convert_to_binary(PadreJ)
       '010100000110000101100100011100100110010101001010'
       '''
 
        self.binary_str = ""
        self.binary_string = ""
 
        # changes the letters in the string into its ascii value representation
        for char in message:
            self.number = ord(str(char))
 
            # turns an integer into a binary string
            while self.number > 0:
               
                self.binary_string = str(self.number % 2) + self.binary_string
                self.number = self.number//2
 
            self.binary_str += self._add_padding(self.binary_string) # checks the padding and stores it in a new string
            self.binary_string = ""                #  reset the binary string to an empty string and begin anew
 
        return self.binary_str
 
    def convert_binary_to_integer(self, binary):
        '''convert_binary_to_integer(str) -> return(str)
       Takes a binary string and converts it into an integer
       returns: an Integer
 
       >>> convert_binary_to_integer('01100001')
       97
       >>> convert_binary_to_integer('01100001')
       119
       
       '''
        self.decimal = []
        self.binary_position = 0
 
        # starts from the right of the binary string. If the binary string at that position is a
        # 1. Then the index in which the 1 occurs is raised to the power of 2
        for pos in xrange(len(binary) -1, 0, -1):
           
             if binary[pos] == '1':
                 self.decimal.append(2 ** self.binary_position)      # raise the index by the power of 2
             self.binary_position += 1
               
        return (sum(self.decimal))
           
    def convert_binary_to_string(self, binary_str):
        '''convert_binary_to_string(str) -> return(str)
 
       Takes a binary string and returns a sentence that all the character
       and letters that can be found on the ascii table
 
       str1 = '010000110110111101100100011010010110111001100111001100010011000000110001'
       str2 = '01010011011010000110000101101110011011100110111101101110'
       str3 = '01000100011000010110110001100101'
       str4 =  '010100000110000101100100011100100110010101001010'
       
       >>> convert_binary_to_string(str1)
       'Coding101'
       
       >>> convert_binary_to_string(str2)
       Shannon
       
       >>> convert_binary_to_string(str3)
       Dale
       
       >>> convert_binary_to_string(str4)
       'PadreJ'
       
       '''
        self.start = 0
        self.end  = 8
        self.text = ""
 
        # Takes a binary string and splits it into bytes. Each byte is then converted to
        # its integer counter part. Next the integer is then converted into a character
        # that can be found within an ascii table.
        for block in range(len(binary_str)/8) :
 
            self.byte = binary_str[self.start: self.end]                          # the first byte of the number
            self.start, self.end = self.end, self.end + 8
       
            # a method call to convert the byte into an integer
            self.integer = self.convert_binary_to_integer(self.byte)
 
            # use the ascii table to convert the integer to its ascii couterpart
            self.text += chr(self.integer)
 
        return self.text
   
########################################################################
# Friendly user inteface class
########################################################################            
class Interface(OperatingSystem):
    '''The class is the inteface class. It hides all the complexes of the classes and
   provides the user with an easy way of converting binary to text or text to binary via a
   friendly text menu. It also inherits from the OperatingSystem class'''
   
    def inform_user(self):
        '''inform the user of what about to happen'''
 
        print "[*] Please wait preparing writing pad for user.."
        sleep(0.05)
        print "[*] Please wait open writing pad for user in new window... "
        sleep(0.05)
       
    def check_and_open(self, file_path):
        '''check_and_open(str) -> return(None)
 
       Depending on what operating system the user is using
       a specific command is used to open the default editor
       on the user computer
       '''
       
        if self.get_operating_system() == "Linux":
                   
            self.command('xdg-open', self.join_path(file_path))
            raw_input("[*] Press Enter to continue ")
     
        elif self.get_operating_system() == "Windows":
           
            self.command('notepad', self.join_path(file_path))
            raw_input("[*] Press Enter to continue ")
 
        else:
            self.output = webbrowser.open(self.join_path(file_path))
            raw_input("[*] Press Enter to continue ")
           
    def menu(self):
        '''menu(void) -> return(int)'''
       
        print '''
 
       [+] A simple program in which text is entered by the user. It is then
       [+] converted to binary or from binary to text if your option was 2
       
       =======================================
 
           [1] Convert Text to Binary
           [2] Convert  Binary to Text
           [3] Exit
 
       =======================================
       '''
 
        self.choice = int(raw_input("[*] Enter your choice : "))
           
        if self.choice == 1:
            self.inform_user()
            self.check_and_open("text_file.txt")
            return 1
 
        elif self.choice == 2:
 
            self.inform_user()
            print "[*] Enter the binary you would like to convert to text "
            self.check_and_open("binary_file.txt")
            return 2
 
        elif self.choice == 3:
            print "[*] Exiting menu and closing program"
            sleep(0.2)
            print "[*] Goodbye, see you soon!!"
            #sys.exit(0)
        else:
            print "[!] your choice must be either 1,2,3, exiting program!!!"
           
               
# the main program
def main():
     
      choice =  user_interface.menu()  # return the user choice from the text menu
     
      if choice == 1:
          txt_file = data.load("text_file.txt")[9:]
 
         # convert to binary and display to user
          for f in txt_file:
              binary = convert.convert_to_binary(f)
              data.create_text_file("binary_file.txt",  binary, "a")
 
          print "\n[*] Conversion successful."
          sleep(0.3)
          print "[*] A copy of file binary_file.txt is in your current working directory..."
          sleep(0.3)
          print "[*[ Displaying binary file in new window please wait..."
          sleep(0.3)
          user_interface.check_and_open("binary_file.txt")
 
      elif choice == 2:
 
         binary_txt_file = data.load("binary_file.txt")[4:]
 
         # Turns the binary string list into a string removes any spaces and any newlines and converts it back
         # to a string. This ensures that even if the user enters the binary with spaces such as 01010 0001 000
         # the outcome will still be the same
         binary_txt_file = [''.join((''.join(''.join(binary_txt_file).split(' '))).split('\n'))]
       
         # convert to text and display to user
         for f in binary_txt_file:
     
             string = convert.convert_binary_to_string(f)
             data.create_text_file("binary_to_string.txt",  string.strip("\n"), "a")
 
         print "\n[*] Succesful converted binary to text."
         sleep(0.3)
         print "[*] A copy of file binary_to_string.txt is in your current working directory..."
         sleep(0.3)
         print "[*] Preparing binary_to_string.txt  file to display to user..."
         sleep(0.3)
         print "[*] Opening file to user in new window..."
         user_interface.check_and_open("binary_to_string.txt")
       
# if the program is run and not imported the following things are initialised and created
if  __name__ == "__main__":
 
    user_interface = Interface()
    data = InputOutput()
    convert = Converter()
   
    # create text file
    data.create_text_file("text_file.txt", ("#"*80))
    data.create_text_file("text_file.txt", ("[*] Hello user enter the text you want to turn to binary"), "a")
    data.create_text_file("text_file.txt", ("[*] Just below the second hash line"), "a")
    data.create_text_file("text_file.txt", ("[*] Or copy and paste any text into the editor"), "a")
    data.create_text_file("text_file.txt", ("[*] When entering your text whether pasting or entering by hand make sure there"), "a")
    data.create_text_file("text_file.txt", ("[*] is at least one new line between your text and the last hash line."), "a")
    data.create_text_file("text_file.txt", ("[*] or your text will not show up in the converted binary file."), "a")
    data.create_text_file("text_file.txt", ("[*] Save the file and close"), "a")
    data.create_text_file("text_file.txt", ("#"*80),"a")
    data.create_text_file("text_file.txt", "\n", "a")
   
    # create binary file
    data.create_text_file("binary_file.txt", ("#"*80))
    data.create_text_file("binary_file.txt", "[*] Your text in binary form\n", "a")
    data.create_text_file("binary_file.txt", ("#"*80), "a")
    data.create_text_file("binary_file.txt", "\n", "a")
 
    # create binary_to_string file
    data.create_text_file("binary_to_string.txt", ("#"*80))
    data.create_text_file("binary_to_string.txt", "[*] converted binary to text format\n", "a")
    data.create_text_file("binary_to_string.txt", ("#"*80), "a")
    data.create_text_file("binary_to_string.txt", "\n", "a")
 
    main()
