# Comparador de Pastas (`pastas_diff.py` / `pastas_diff.exe`)

## Objetivo
Comparar duas pastas (incluindo subpastas) e gerar relatório com arquivos exclusivos de cada lado.

## Como funciona
- Usuário seleciona duas pastas pela interface.
- O script lista arquivos recursivamente por caminho relativo.
- Ignora arquivos `.ffs_db`.
- Calcula:
  - exclusivos da pasta 1;
  - exclusivos da pasta 2;
  - total em comum (por caminho relativo).

## Saída
- Relatório de texto salvo na pasta 1:
  - `comparacao_pastas_YYYYMMDDHHMMSS.txt`
- Log de erros em:
  - `ERROS/comparison_failures_YYYYMMDDHHMMSS.log` (na pasta 1)

## Importante
- A comparação é por presença/ausência de caminho relativo.
- Não compara conteúdo binário/hash dos arquivos.
