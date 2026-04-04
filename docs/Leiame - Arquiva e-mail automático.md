# Arquivador Automático (`arquiva_email.py` / `arquiva_email.exe`)

## Objetivo
Organizar arquivos de uma pasta de monitoramento em subpastas `AAAA/AAAA-MM`, usando data do e-mail (`.eml`) ou data de modificação (demais arquivos).

## Entrada da pasta monitorada
- Prioridade 1: argumento de linha de comando (ao chamar o `.exe`).
  - Exemplo: `arquiva_email.exe "C:\MinhaPasta\Mensagens"`
- Prioridade 2: se nenhum argumento for informado, o programa abre uma caixa de mensagem e solicita a seleção da pasta em um diálogo.
- Se o argumento for inválido, exibe erro e encerra.
- Se o usuário cancelar a seleção, exibe aviso e encerra.

## Como funciona
- Processa apenas arquivos da pasta raiz configurada (não percorre subpastas).
- Ignora arquivos `.ffs_db` e `.ffs_lock`.
- Para `.eml`:
  - tenta ler cabeçalho `Date`;
  - se o parser não enxergar o cabeçalho (ex.: BOM no meio do arquivo), tenta extrair `Date:` do texto bruto;
  - se ainda falhar, usa `datetime.now()`.
- Para outros arquivos: usa `st_mtime` (data de modificação).

## Regras de nome e caminho
- Sanitização (Windows/CP1252):
  - remove prefixo `msg ` no início;
  - remove caracteres inválidos de nome (`<>:"/\\|?*`);
  - remove controles, ponto/espaço no fim;
  - evita nomes reservados (`CON`, `PRN`, `AUX`, `NUL`, `COM1..COM9`, `LPT1..LPT9`);
  - aplica fallback `arquivo_renomeado` quando necessário.
- Ordem aplicada: `sanitizar -> truncar -> resolver duplicidade -> retruncar`.
- Limite de caminho completo: `EFFECTIVE_MAX_PATH (259) - SAFE_PATH_MARGIN (10) = 249`.

## Logs
- Pasta: `ERROS` dentro da raiz de arquivamento.
- Arquivo: `archive_failures_YYYYMMDDHHMMSS.log`.
- Registra erros de leitura, data, criação de pasta, conflito irresolúvel e falha de movimentação.

## Execução independente
- O script roda sozinho.
- A função de sanitização já está embutida no próprio script.

## Observação de compatibilidade
- O script continua com `WATCH_FOLDER_PATH_STR` no código, mas o fluxo principal agora prioriza argumento/seleção por diálogo.
