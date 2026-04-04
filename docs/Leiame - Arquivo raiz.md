# Centralizador de Arquivos na Raiz (`arquiva_raiz.py` / `arquiva_raiz.exe`)

## Objetivo
Mover arquivos das subpastas para a pasta raiz selecionada e padronizar os nomes.

## Como funciona
- Varre recursivamente a árvore da pasta raiz.
- Ignora pastas `ERROS` e `anos anteriores` (case-insensitive), além da pasta de log ativa.
- Para cada arquivo:
  - sanitiza nome;
  - aplica truncamento por limite de caminho;
  - resolve duplicidade com timestamp;
  - move para a raiz (ou renomeia se já estiver na raiz).
- Ao final, remove pastas vazias.

## Regras de nome e caminho
- Sanitização CP1252 com:
  - remoção de prefixo `msg `;
  - remoção de caracteres inválidos;
  - proteção contra nomes reservados do Windows;
  - fallback `arquivo_renomeado`.
- Ordem: `sanitizar -> truncar -> duplicidade -> retruncar`.
- Limite de caminho completo: `249` caracteres (`EFFECTIVE_MAX_PATH=259`, `SAFE_PATH_MARGIN=10`).

## Logs
- Pasta: `ERROS` na raiz selecionada.
- Arquivo: `process_root_log_YYYYMMDDHHMMSS.log`.
- Registra sanitizações, truncamentos, conflitos e erros de operação.

## Execução independente
- O script funciona sozinho e já traz a função de sanitização embutida.
