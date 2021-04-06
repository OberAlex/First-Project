import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll", use_last_error=True) # Handle to Kernel32.dll, Avoids threading conflict

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF) # All possible access rights for a process object

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False # Does not inherit handle
dwProcessId = int(input("Enter a PID: ")) # Prompts user to enter a Process ID (ID of process to be opened)

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId) # Opens an existing local process object

error = k_handle.GetLastError() # Retrieves the thread's last Error Code.
if error != 0: # Something failed, Notifies User + OS
    print("Error Code: {0}".format(error)) 
    exit(1)

# Check to see if we have a valid Handle
if response <= 0:
    print("Handle was not created")
else:
    print("Handle was created")