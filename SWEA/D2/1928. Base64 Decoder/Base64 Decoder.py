code = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

for test_case in range(1,int(input())+1):
    words = input()
    binary_decoding = ''
    original = ''
    for word in words:
        binary = int(bin(code.index(word))[2:])
        binary_decoding += '{0:06d}'.format(binary)                 
    for idx in range(0,len(binary_decoding), 8):                     
        word = binary_decoding[idx:idx+8]
        original += chr(int(word, 2))                          
    print(f'#{test_case} {original}')