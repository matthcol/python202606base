# module csvutils
from pathlib import Path
import re

import pandas as pd

# Héritage:
# - class CsvConversionError hérite de la classe Exception
# - 1 object CsvConversionError est aussi une Exception (principe de substitution)
class CsvConversionError(Exception):
    pass

def convert(
        file_in: str | Path,
        delimiter_in: str,
        delimiter_out: str,
        overwrite: bool = False,
        suffix: str | None = None,
        **kwargs_in
) -> Path:
    """ TODO: mode d'emploi de la fonction

    Parameters:
    - file_in:
    - delimiter_in:
    - delimiter_out: 
    - overwrite:
    - suffix:
    - kwargs_in: extra params to read the input file

    Returns output file path

    Raises CsvConversionError if output file already exists and overwrite is deactivated
    """
    path_in = file_in if isinstance(file_in, Path) else Path(file_in)
    if suffix is None:
        path_out = path_in
    else:
        filename = path_in.name
        m = re.fullmatch(r"(.*)(\.[^.]*)", filename)
        if m is None:
            # no extension
            new_filename = filename + suffix
        else:
            base, ext = m.groups()
            new_filename = base + suffix + ext
        path_out = path_in.parent / new_filename
    if not overwrite and path_out.exists():
        # raise FileExistsError("output file already exists and overwrite is forbidden")
        raise CsvConversionError("output file already exists and overwrite is forbidden")


    data = pd.read_csv(path_in, delimiter=delimiter_in, **kwargs_in)
    data.to_csv(path_out, sep=delimiter_out)
    return path_out