# Arquivador Recursivo (`arquiva_subpastas.py` / `arquiva_subpastas.exe`)

## Objetivo
Organizar arquivos da pasta escolhida e de todas as subpastas em estrutura `AAAA/AAAA-MM` dentro da própria raiz selecionada.

## Como funciona
- Processamento recursivo.
- Ignora pastas `ERROS` e `anos anteriores` (case-insensitive), além da pasta de log ativa.
- Ignora `.ffs_db` e `.ffs_lock`.
- Para `.eml`:
  - tenta `Date` do cabeçalho;
  - fallback para extração de `Date:` no texto bruto (casos com header quebrado);
  - fallback final para data/hora atual.
- Para outros arquivos: usa data de modificação.
- Ao final, remove pastas vazias (com proteções para não remover raiz/log/excluídas).

## Regras de nome e caminho
- Sanitização CP1252 (Windows), incluindo nomes reservados e fallback.
- Ordem: `sanitizar -> truncar -> duplicidade -> retruncar`.
- Limite de caminho completo: `249` (`259 - 10`).

## Logs e resultado
- Logs em `ERROS/archive_failures_subfolders_*.log`.
- Resumo final em janela com contagens de:
  - arquivos movidos;
  - arquivos renomeados no local;
  - pastas criadas;
  - pastas vazias removidas;
  - erros.

## Execução independente
- Funciona sem dependência obrigatória externa do sanitizador compartilhado (possui fallback local).
