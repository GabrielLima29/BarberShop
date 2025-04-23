import re
from messages.responses import MENSAGENS
from servises.google_calendar_api import verificar_disponibilidade, criar_evento

def handle_agendamento(message, user_data):
    if not user_data.get("nome"):
        user_data["nome"] = message.strip().title()
        return (MENSAGENS["pergunta_telefone"], user_data, False)

    if not user_data.get("telefone"):
        if re.match(r"\(?\d{2}\)?\s?9?\d{4}-?\d{4}$", message):
            user_data["telefone"] = message.strip()
            return (MENSAGENS["pergunta_profissional"], user_data, False)
        else:
            return ("Número inválido. Envie no formato (DD) 91234-5678", user_data, False)

    if not user_data.get("profissional"):
        profissional = message.lower().strip()
        if profissional in ["felipe", "matheus", "guilherme"]:
            user_data["profissional"] = profissional
            return (MENSAGENS["pergunta_data"], user_data, False)
        else:
            return ("Profissional não encontrado. Escolha entre Felipe, Matheus ou Guilherme.", user_data, False)

    if not user_data.get("data"):
        # Aceita formatos como 23/04 ou 23-04
        if re.match(r"\d{2}[/-]\d{2}", message):
            user_data["data"] = message.strip().replace("-", "/")
            return (MENSAGENS["pergunta_horario"], user_data, False)
        else:
            return ("Data inválida. Envie no formato DD/MM", user_data, False)

    if not user_data.get("horario"):
        horario = message.strip()
        if re.match(r"\d{2}:\d{2}", horario):
            # Verifica disponibilidade no Google Calendar
            disponivel = verificar_disponibilidade(user_data["profissional"], user_data["data"], horario)
            if disponivel:
                user_data["horario"] = horario
                criar_evento(user_data)  # Cria o evento no Google Calendar
                return (MENSAGENS["confirmacao"].format(**user_data), user_data, True)
            else:
                return ("Esse horário já está agendado. Por favor, escolha outro horário.", user_data, False)
        else:
            return ("Horário inválido. Envie no formato HH:MM", user_data, False)

    return ("Algo deu errado. Vamos tentar novamente?", user_data, False)
