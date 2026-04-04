# Renomeador de E-mails (`renomear_eml.py` / `renomear_eml.exe`)

## Objetivo
Renomear arquivos `.eml` da pasta selecionada com base em data, assunto e remetente, mantendo consistência de nomes e evitando conflitos.

## Escopo
- Processa apenas `.eml` no nível raiz da pasta selecionada.
- Não processa subpastas.

## Regra de nome final
- Formato base:
  - `YYYY MM DD HHMM - Assunto - Remetente.eml`
- Se houver conflito, adiciona sufixo alfabético:
  - `a..z`, depois `aa..zz`.

## Origem da data
- Prioridade:
  1. Cabeçalho `Date` do e-mail.
  2. Fallback no corpo (padrão após `Mensagem=`).
  3. Data de modificação do arquivo.
  4. Data/hora atual.
- Quando o parser de cabeçalho falha (ex.: arquivo com BOM interno), tenta recuperar `Date`, `Subject` e `From` do texto bruto do `.eml`.

## Regras de nome e caminho
- Sanitização em CP1252 (preserva acentos compatíveis com Windows).
- Ordem aplicada no nome final:
  - `sanitizar -> truncar por path completo -> duplicidade -> retruncar`.
- Limite de caminho completo:
  - `249` (`EFFECTIVE_MAX_PATH=259`, `SAFE_PATH_MARGIN=10`).
- Mesma regra é usada ao mover arquivos problemáticos para `Problemas`.

## Tratamento de erros
- Arquivos com falha grave de leitura/processamento são movidos para subpasta `Problemas`.
- Logs em `LOGS_RENOMEAR_EML/renomear_eml_log_*.log`.
- Resumo final mostra:
  - renomeados;
  - movidos para `Problemas`;
  - ignorados;
  - total de erros.

## Importante
- Este script não usa mais pasta `Duplicatas`; conflitos são resolvidos por sufixo no próprio nome.
- A função de sanitização já está embutida no próprio script.
