# logger.py

"""
Configuração básica do módulo de logging para o projeto.

Esta configuração define o nível de logging para INFO e especifica o formato
padrão para as mensagens de log. Isso garante que as mensagens de log serão
registradas com um carimbo de data/hora, nível de log e a própria mensagem.

A configuração deve ser importada e utilizada nos módulos relevantes do projeto
para manter uma formatação e nível de log consistentes.

Exemplo de uso:
    from logger import logging_config
"""

import logging

# Configuração básica do módulo de logging para o projeto
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
