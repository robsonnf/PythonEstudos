
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Gerando uma chave aleatória de 16 bytes
key = get_random_bytes(16)

# Criptografando os dados
cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b"mensagem secreta")

# Descriptografando os dados
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print(plaintext)

# Função para verificar aptidão para doação (sem alterações)
def verificar_aptidao_doacao():
    while True:
        try:
            idade = int(input('Informe sua idade: '))
            peso = int(input('Informe seu peso: '))
            descanso = int(input('Informe quantas horas de sono teve nas últimas 24 horas: '))

            if 16 <= idade <= 69 and peso >= 50 and descanso >= 6:
                print("Olá! Você está apto a doar sangue.")
            else:
                print("Olá, você não está apto a doar sangue.")
                print("Verifique se sua idade está entre 16 e 69 anos, se pesa 50kg ou mais e se descansou pelo menos 6 horas.")
            break
        except ValueError:
            print("Por favor, insira apenas números inteiros para idade, peso e horas de sono.")

verificar_aptidao_doacao()
