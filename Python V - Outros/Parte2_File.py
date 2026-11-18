# open - filename and mode (r,a,w,x)
# r: opens a file just for reading, error if the file does not exist 
# a: opens a file for appending, creates the file if it does not exist
# w: opens a file for writing, creates the file if it does not exist
# x: creates the specified file, returns an error if the file exists

#with open - don't have to call close() function
with open("Parte2_File.txt", mode='a') as meu_arquivo:
    texto = meu_arquivo.write("Hoje ce pode me esquecer\nEh carnaval no Brasil\n")
    
with open("Parte2_File.txt", mode='r') as meu_arquivo:
    texto = meu_arquivo.read()
    print(texto)

#Bom para arquivos muito grandes    
print("Linhas")    
with open("Parte2_File.txt") as meu_arquivo:
    for linha in meu_arquivo:
        print(linha)
