# Verificador de Sequência e Unificador (`relatorio_mensagens.py` / `relatorio_mensagens.exe`)

## Objetivo
Verificar sequências numéricas em nomes de arquivos e, opcionalmente, unificar relatórios `.txt` em HTML.

## Verificação de sequência
- Usuário informa:
  - pasta;
  - número inicial;
  - número final.
- O script avalia arquivos da pasta (somente nível raiz) e identifica:
  - números faltantes no intervalo;
  - números fora do intervalo;
  - arquivos sem número inicial.

## Relatório individual
- Salva em `.txt` na pasta pai da pasta analisada:
  - `relatorio_verificacao_<nome_da_pasta>.txt`

## Unificação opcional
- Se marcada a opção na interface:
  - lê os `.txt` da pasta pai;
  - gera um HTML consolidado:
    - `<nome_da_pasta_pai> - Relatório dos Backups de Mensagens.html`
  - remove os `.txt` unificados.
- Logs da unificação em:
  - `LOGS_UNIFICADOR/unificador_report_log_*.log`

## Dependência funcional
- Usa a biblioteca `markdown` para converter conteúdo de texto para HTML no processo de unificação.
