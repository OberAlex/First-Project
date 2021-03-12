import ctypes

user_handle = ctypes.WinDLL("User32.dll") # Handle to User32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") # Handle to Kernel32.dll

hWnd = None # Not Used
lpText = "Hello World!" # Message to be Displayed
lpCaption = "Howdy y'all" # Box Title
uType = 0x00000001 # Ok and Cancel Buttons Displayed

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType) # Catch Response

error = k_handle.GetLastError() # Handle Error
if error != 0: # Something failed, Notifies User + OS
    print ("Error Code: {0}".format(error))
    exit(1)

if response == 1: # Ok Button Clicked
    print ("User Clicked OK!")
elif response == 2: # Cancel/'X' Button Clicked
    print ("User Clicked CANCEL!")