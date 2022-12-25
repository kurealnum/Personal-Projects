import time, hashlib, random
start_time = time.time()


#Creating the hashed "password" 
encodedstr = "Pass".encode()
hashedstr = hashlib.sha256(encodedstr).hexdigest()

alph_counter_var = -1 

while True:

    #Setting the alphabet counter variable each time we loop around
    alph_counter_var = alph_counter_var+1

    #Checking if the alphabet counter has gone past 26 and if it has, set it to 0 again. Remember that lists start counting by 0
    if alph_counter_var >= 26:
        alph_counter_var == 0
    else:
        continue

    #The alphabet list to loop through
    alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    semi_ran_password_guess = [random.choice(alph_list) for i in range(3)]
    
    testhash = "Pass".encode()

    # Saving this here in case I need to check the hashes of the variables and strings again
    # print(f'The lowercase hash: {hashlib.sha256(testhash.lower()).hexdigest()} .The uppercase hash: {hashlib.sha256(testhash.upper()).hexdigest()} 
    # The normal, unchanged hash: {hashlib.sha256(testhash).hexdigest()} .The hashed string: {hashedstr} ')

    #  The hash of the the lowercase string                The hash of the uppercase string                            The hash of the bare, default string
    if hashlib.sha256(testhash.lower()).hexdigest() == hashedstr or hashlib.sha256(testhash.upper()).hexdigest() == hashedstr or hashlib.sha256(testhash).hexdigest() == hashedstr:
        print(f'The password is {testhash.decode()}')
        break
    else:
        continue

#Print how long the process took to run
print("Process finished --- %s seconds ---" % (time.time() - start_time))
