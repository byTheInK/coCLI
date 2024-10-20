import cmd
import os

class coCLI(cmd.Cmd):
#------------------------------#
    def __init__(self):
        super().__init__()
#------------------------------#
    os.system("cls")
#------------------------------#
    intro = 'coCLI is enabled. Please type "help" to look through the avaible commands.'
#------------------------------#
    prompt = "|>- "

   
    #!FUNCS
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*ls
    def do_ls(self, line):
        """Finds and prints out the files in the current directory."""
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)
    #*cd
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    def do_cd(self,directory):
        """Changes the current directory to another directory."""
        try:
            nd = os.path.join(self.current_directory,directory)
            if os.path.exists(nd) and os.path.isdir(nd):
                self.current_directory = nd
                print(f"Directory is now changed to {self.current_directory}")
            else:
                print(f"Can't find directory {directory}")
        except Exception as e:
            print(f"There is an error found:\n{e}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*cls
    def do_cr(self,line):
        """Clears the CLI."""
        os.system("cls")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*intro
    def do_it(self,line):
        """Clears the CLI and prints out the intro message."""
        os.system("cls")
        print('coCLI is enabled. Please type "help" to look through the avaible commands.')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*exit
    def do_q(self, line):
        """Exit the CLI."""
        try:
            os.system("cls")
            return True
        except Exception as e:
            print("Can't exit: \n"+e)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #!FILES
    #*create file
    def do_cf(self,filename):
        """Creates a file relative to the current directory."""
        try:
            with open(os.path.join(self.current_directory,filename),"x") as f:
                pass
        except FileExistsError:
            print(f"File {filename} already exsists.")
        except Exception as e:
            print(f"There is an error found:\n{e}")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*remove file
    def do_rf(self,filename):
        """Removes a file relative to the current directory."""
        try:
            os.remove(os.path.join(self.current_directory,filename))
        except FileNotFoundError:
            print(f"Can't find file {filename}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #!DIRECTORY
    #*directory
    def do_d(self,line):
        """Prints out the current directory."""
        print(self.current_directory)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    #*create directory
    def do_cdir(self,directoryname):
        """Creates a directory relative to the current directory."""
        try:
            os.makedirs(os.path.join(self.current_directory,directoryname))
        except FileExistsError:
            print(f"Directory {filename} already exsists.")
        except Exception as e:
            print(f"There is an error found:\n{e}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #*Change the directory to desktop
    def do_ctd(self,line):
        """Changes the current directory to desktop."""
        try:
            self.current_directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            print(f"Changed the current directory to {self.current_directory}")
        except Exception as e:
            print(f"There is an error found:\n{e}")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#        
#?RUN
if __name__ == '__main__':
    coCLI().cmdloop()