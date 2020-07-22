"""
The following files are available in this module:
"""
import sys
from pathlib import Path

from ._sample import _SAMPLE_FILES, download_sample_data

files = download_sample_data()

file_list = []
file_dict = {}
for f in files:
    name = Path(f).name
    _key = _SAMPLE_FILES.get(name, None)
    if not _key:
        continue

    setattr(sys.modules[__name__], _key, str(f))
    file_list.append(f)
    file_dict.update({_key: f})
    # Add filename to the docs
    __doc__ += f'   - ``{_key}``\n'

__all__ = list(_SAMPLE_FILES.values()) + ['file_dict', 'file_list']
