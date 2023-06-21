def palindrome (s) : 
    
    return s [::-1] == s 



while True: 
    
    s = input( "Bведите слово: " ) 
    
    print( f" {s} является палиндромом" if 
        palindrome (s) else f" {s} не является палиндромом" )
    
    if s == 'break.' :
        break