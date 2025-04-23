from servises.whatsapp_api   import receive_message, send_message
from client_data import get_user_data, update_user_data
from messages.system import handle_agendamento
from config import WELCOME_MESSAGE

def main():
    while True:
        numero, mensagem = receive_message()  # Simula recebimento de mensagem
        user_data = get_user_data(numero)

        resposta, user_data, finalizado = handle_agendamento(mensagem, user_data)

        update_user_data(numero, user_data)
        send_message(numero, resposta)

        if finalizado:
            print(f"Agendamento concluído para {numero}")


