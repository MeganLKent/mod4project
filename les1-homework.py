def palindrome (s) : 
    
    return s [::-1] == s 



while True: 
    
    s = input( "Bведите слово: " ) 
    
    print( "True" if palindrome (s) else "False" )
    
    if s == 'break.' :
        break
