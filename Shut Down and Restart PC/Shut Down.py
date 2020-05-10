# Python Program - Shutdown Computer
	
import os;
check = input("Want to shutdown your computer ? (y/n): \n");
if check == 'n':
    exit();
elif check == 'y':
    os.system("shutdown /s /t 1");