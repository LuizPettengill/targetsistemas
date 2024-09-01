# Função 
def check_number_a(text):
    # Metodo que transforma o texto todo para lower case e conta os As
    quantity_a = text.lower().count('a')
    
    # Checa se tem A no texto
    if quantity_a> 0:
        print(f"Tem {quantity_a} As na frase.")
    else:
        print("Nao tem A nessa frase.")

# Input do usuario
text = input("Escreva uma frase: ")

# Chamando a função que faz a verificação se existem As
check_number_a(text)
