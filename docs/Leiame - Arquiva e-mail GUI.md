# Arquivador GUI de Pasta Única (`arquiva_email_gui.py` / `arquiva_email_gui.exe`)

## Objetivo
Organizar arquivos de uma pasta escolhida pelo usuário em subpastas `AAAA/AAAA-MM`.

## Como funciona
- Processa apenas arquivos do nível raiz da pasta selecionada.
- Ignora `.ffs_db` e `.ffs_lock`.
- Para `.eml`:
  - usa cabeçalho `Date`;
  - se o parser falhar, tenta `Date:` no conteúdo bruto do arquivo;
  - se não conseguir data válida, usa data/hora atual.
- Para outros arquivos: usa data de modificação.

## Regras de nome e caminho
- Sanitização em CP1252 (Windows), com:
  - remoção de `msg ` no início;
  - remoção/substituição de caracteres inválidos;
  - tratamento de nomes reservados do Windows;
  - fallback `arquivo_renomeado`.
- Ordem: `sanitizar -> truncar -> duplicidade -> retruncar`.
- Limite de caminho completo: `249` caracteres (`259 - 10`).

## Logs e resumo
- Logs em `ERROS/archive_failures_*.log` dentro da pasta processada.
- Exibe resumo final em janela com auto-fechamento.

## Execução independente
- Funciona sozinho.
- A função de sanitização já está embutida no próprio script.
