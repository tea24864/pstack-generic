"""Append one POSIX-locked, spreadsheet-safe decision row (stdlib)."""
from datetime import datetime, timezone
from pathlib import Path
import fcntl
import os
import stat
import sys

HEADER = 'ts\tphase\tdecision\twhy\tevidence\tresult\n'


def clean(value):
    value = ''.join(' ' if ch in '\t\r\n\v\f\x85\u2028\u2029' else ch for ch in value)
    return "'" + value if value.lstrip().startswith(('=', '+', '-', '@')) else value


def append(path, cells):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW | os.O_NONBLOCK
    fd = os.open(path, flags, 0o600)
    with os.fdopen(fd, 'r+', encoding='utf-8', newline='') as stream:
        if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
            raise ValueError('log target must be a regular file')
        fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        stream.seek(0)
        first = stream.readline()
        if first and first != HEADER:
            raise ValueError('existing log header does not match the decision schema')
        stream.seek(0, os.SEEK_END)
        size = stream.tell()
        if size:
            stream.seek(size - 1)
            if stream.read(1) != '\n':
                raise ValueError('existing log has an incomplete last row')
            stream.seek(0, os.SEEK_END)
        stamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        row = '\t'.join([stamp, *(clean(x) for x in cells)]) + '\n'
        stream.write(('' if first else HEADER) + row)
        stream.flush()
        os.fsync(stream.fileno())


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 6:
        print('usage: log.sh <logfile> <phase> <decision> <why> <evidence> <result>', file=sys.stderr)
        return 2
    try:
        append(args[0], args[1:])
    except (OSError, ValueError, UnicodeError) as exc:
        print('log append failed: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
