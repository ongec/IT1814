def is_valid_nric( s ):
    valid = False
    # implement your validation here
    if(len(s) == 9): # 7 digits, 2 alpha
        # Starts with S or T
        if (s[0].upper() == 'S' or s[0].upper() == 'T' ):
            # Must be 7 digits
            if ( s[1:8].isdigit() ):
                # Ends with alphabet
                if (s[-1].isalpha()):
                    valid = True
    return valid
# main program calling function is_valid_nric
# It just display the boolean result returned from function
print( is_valid_nric( "t2323213t" ) ) #this should be valid
print( is_valid_nric( "s12323232" ) ) #this is invalid
print( is_valid_nric( "S" ) ) #this is invalid
print( is_valid_nric( "S12345678T" ) ) #this is invalid
