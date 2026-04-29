from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

SOLUCOES_TI = {
    "lentidao": "Para lentidão ou travamentos, recomendo abrir o Gerenciador de Tarefas (Ctrl+Shift+Esc), verificar qual programa está consumindo mais CPU ou RAM e finalizá-lo. Reiniciar a máquina também limpa o cache.",
    "internet": "Problemas de conexão (Wi-Fi ou Rede) geralmente se resolvem reiniciando o roteador. Aguarde 30 segundos com ele desligado. Se não voltar, tente limpar o DNS abrindo o CMD e digitando 'ipconfig /flushdns'.",
    "tela azul": "A temida Tela Azul da Morte! Isso costuma ser problema de memória RAM ou drivers desatualizados. Recomendo atualizar os drivers de vídeo e rodar o Diagnóstico de Memória do Windows.",
    "virus": "Se suspeita de vírus, desconecte a máquina da internet imediatamente para evitar que ele se espalhe. Em seguida, rode uma verificação completa no Windows Defender ou no seu antivírus de preferência.",
    "impressora": "Cancele todos os documentos na fila de impressão, desligue a impressora, tire da tomada por 10 segundos, ligue novamente e tente imprimir uma página de teste."
}

class ActionResolverProblema(Action):
    def name(self) -> Text:
        return "action_resolver_problema"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        problema = tracker.get_slot("problema")

        if not problema:
            dispatcher.utter_message(text="Poderia me dar mais detalhes sobre o que está acontecendo com o equipamento? Tente usar palavras-chave como: wifi, internet, tela azul, impressora, vírus ou lento.")
            return []

        problema_lower = problema.lower()
        
        if problema_lower in ["wifi", "wi-fi", "rede", "conexão", "internet", "caiu"]:
            chave_busca = "internet"
        elif problema_lower in ["lentidão", "lento", "travando", "congelando", "pc lento"]:
            chave_busca = "lentidao"
        elif problema_lower in ["tela azul", "blue screen"]:
            chave_busca = "tela azul"
        elif problema_lower in ["vírus", "virus", "malware"]:
            chave_busca = "virus"
        elif problema_lower in ["impressora", "imprimir", "impressão"]:
            chave_busca = "impressora"
        else:
            chave_busca = problema_lower

        solucao = SOLUCOES_TI.get(chave_busca)

        if solucao:
            dispatcher.utter_message(text=f"Entendido. Aqui está a recomendação técnica: \n\n**{solucao}**")
        else:
            dispatcher.utter_message(text=f"Ainda não tenho um procedimento padrão no meu sistema para o sintoma '{problema}'. Recomendo abrir um chamado para a equipe de nível 2 analisar fisicamente.")

        return []