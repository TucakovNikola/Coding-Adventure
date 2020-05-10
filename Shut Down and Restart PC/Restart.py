# Python Program - Restart Computer

import os;
check = input("Want to restart your computer ? (y/n): ");
if check == 'n':
    exit();
elif check == 'y':
    os.system("shutdown /r /t 1");