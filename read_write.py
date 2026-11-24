from pathlib import Path
from thefuzz import fuzz

def read_file(file):
    words = []
    try:
        with open(file, "r", encoding="utf-8") as file:
                for line in file:
                    clean_line = line.rstrip("\r\n").lstrip()
                    if(clean_line.find("//") != -1):
                        clean_line = clean_line.split("//", 1)[0]
                    if(clean_line != ''):
                        words.append(clean_line)
    except FileNotFoundError:
        
        notit = []
        
        while (find_close(file, notit)) != 0:
            closest = find_close(file, notit)
            choice = input(f"Did you mean {closest}. ").lower()
            while choice not in ['y','n','yes','no']:
                print("Not valid choice try again")
                
            if(choice == 'y' or choice == 'yes'):
                words = read_file(closest)
                break
            else:
                notit.append(closest)
        else:
            print("No more files found")
            return
            
    except PermissionError:
        print(f"Error: Permission denied to read {file}.")
        return
        
    except OSError as e:
        print(f"File error occurred: {e}")
        return

    return words

def write_file(file, text):
    file_path = Path.cwd() / file
    if file_path.is_file():
        try:
            with open(file, "a", encoding="utf-8") as file:
                file.write(text)
                
        except PermissionError:
            print(f"Error: Permission denied to write to {file}")
        except OSError as e:
            print(f"File error occurred: {e}")    
    else:
        try:
            with open(file, "w", encoding="utf-8") as file:
                file.write(text)
        except PermissionError:
            print(f"Error: Permission denied to write to {file}")
        except OSError as e:
            print(f"File error occurred: {e}")    

def find_close(file_name, *args):
    directory = Path.cwd()
    closest = "Error: no files found"
    match = 0

    #finding all files that might be relavant
    files = [f for f in directory.glob("*.sv") if f.is_file()]
    files.extend(f for f in directory.glob("*.v") if f.is_file())
    
    for check_file in files:

        if match < fuzz.ratio(str(file_name), str(check_file.name)) and str(check_file.name) not in args[0]:
            match = fuzz.ratio(str(file_name), str(check_file.name))
            closest = check_file.name

    if match == 0:
        return 0
        
    return closest

def main():
    find_close("test.sv")
        
if __name__ == "__main__":
    main()