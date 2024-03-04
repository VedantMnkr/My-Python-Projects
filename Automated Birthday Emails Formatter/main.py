import automate_email

def main():
    names = []
    automate_email.extract_names("Input/Names/invited_names.txt", names)          
    automate_email.write_email(names)

if __name__ == "__main__":
    main()