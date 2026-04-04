"""Utilitarios compartilhados entre os scripts de backup de mensagens."""

from pathlib import Path
import re
from typing import Optional, Sequence, Union


PathLike = Union[str, Path]


def sanitize_filename(
    filename: str,
    fallback: str = "arquivo_renomeado",
    remove_msg_prefix: bool = True,
    normalize_leading_number: bool = True,
) -> str:
    """Normaliza um nome de arquivo para uso seguro no Windows.

    A funcao remove caracteres invalidos, corrige nomes reservados e aplica
    fallback quando o nome resultante fica vazio.

    Args:
        filename: Nome original do arquivo.
        fallback: Nome minimo a usar quando o resultado fica vazio.
        remove_msg_prefix: Remove prefixo ``msg `` (case-insensitive).
        normalize_leading_number: Normaliza numeros iniciais removendo zeros a esquerda.

    Returns:
        Nome sanitizado pronto para uso no sistema de arquivos.
    """
    sanitized = filename.strip()
    sanitized = sanitized.encode("cp1252", errors="ignore").decode("cp1252")
    if remove_msg_prefix:
        sanitized = re.sub(r"^msg\s+", "", sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", sanitized)
    sanitized = re.sub(r"[\x00-\x1f]", "", sanitized)
    sanitized = sanitized.strip().rstrip(" .")

    if normalize_leading_number:
        match = re.match(r"^(\d+)(.*)", sanitized)
        if match:
            number_str, rest_of_name = match.groups()
            try:
                sanitized = str(int(number_str)) + rest_of_name
            except ValueError:
                if len(number_str) > 1 and number_str.startswith("0"):
                    sanitized = number_str.lstrip("0") + rest_of_name
                else:
                    sanitized = number_str + rest_of_name

    if not sanitized:
        sanitized = fallback

    if sanitized.startswith("."):
        sanitized = f"{fallback}{sanitized}"

    suffixes = "".join(Path(sanitized).suffixes)
    base = sanitized[:-len(suffixes)] if suffixes else sanitized
    if not base:
        base = fallback
        sanitized = f"{base}{suffixes}" if suffixes else base

    windows_reserved_names = {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    }
    if base.upper() in windows_reserved_names:
        sanitized = f"{base}_{suffixes}" if suffixes else f"{base}_"

    sanitized = sanitized.rstrip(" .")
    return sanitized or fallback


def extract_header_value_from_raw_eml(
    eml_path: PathLike,
    header_name: str,
    encodings: Sequence[str] = ("utf-8", "latin-1"),
) -> Optional[str]:
    """Extrai um valor de cabecalho diretamente do texto bruto de um arquivo EML.

    Esse fallback e util quando o parser padrao de e-mail falha em arquivos
    com peculiaridades como BOM no meio dos headers.

    Args:
        eml_path: Caminho do arquivo ``.eml``.
        header_name: Nome do header desejado (ex.: ``Date``, ``Subject``).
        encodings: Lista de encodings tentados durante a leitura.

    Returns:
        Valor do header sem o nome/chave, ou ``None`` se nao encontrado.
    """
    eml_path_obj = Path(eml_path)
    header_prefix = f"{header_name.lower()}:"

    for encoding in encodings:
        try:
            with eml_path_obj.open("r", encoding=encoding, errors="ignore") as file_obj:
                for line in file_obj:
                    stripped_line = line.strip("\r\n")
                    if stripped_line == "":
                        break
                    normalized_line = stripped_line.lstrip("\ufeff")
                    if normalized_line.lower().startswith(header_prefix):
                        return normalized_line.split(":", 1)[1].strip()
        except Exception:
            continue
    return None


def is_ffs_aux_file(filename: str) -> bool:
    """Indica se um arquivo e auxiliar do FreeFileSync e deve ser ignorado.

    Args:
        filename: Nome do arquivo a verificar.

    Returns:
        ``True`` para ``.ffs_db`` e ``.ffs_lock``; caso contrario, ``False``.
    """
    normalized_name = filename.lower()
    return normalized_name.endswith(".ffs_db") or normalized_name.endswith(".ffs_lock")
