def windows_interaction():
    import sys

    if "windows" not in sys.platform:
        raise RuntimeError('Function can only run on windows systems')
    print('Doing windows things')

# try:
#     windows_interaction()
# except:
#     pass
    
try:
    windows_interaction()
except:
    print("The windows function wasn't executed")

# In order to see exactly what went wrong, you’d need to catch the error that the function raised.
    
try:
    windows_interaction()
except RuntimeError as error:
    print(error)
    print("The windows function wasn't executed")