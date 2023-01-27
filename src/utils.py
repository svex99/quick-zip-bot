from typing import Iterator
from asyncio import wait
from asyncio.tasks import FIRST_COMPLETED
from zipfile import ZipFile
from pathlib import Path

from telethon.tl.custom import Message


async def download_files(
    msgs: list[Message],
    conc_max: int = 3,
    root: Path | None = None
) -> Iterator[Path]:
    """
    Downloads the file if present for each message.

    Args:
        msgs: list of messages from where download the files.
        conc_max: max amount of files to be downloaded concurrently.
        root: root path where store file downloaded.
    
    Returns:
        Yields the path of every file that is downloaded.
    """
    root = root or Path('./')

    next_msg_index = 0
    pending = set()
    while next_msg_index < len(msgs) or pending:
        # fill the pending set with tasks until reach conc_max
        while len(pending) < conc_max and next_msg_index < len(msgs):
            try:
                m = msgs[next_msg_index]
            except IndexError:
                pass
            else:
                pending.add(m.download_media(file=root / (m.file.name or 'no_name')))
                next_msg_index += 1
        
        if pending:
            done, pending = await wait(pending, return_when=FIRST_COMPLETED)

            if done and (path := await done.pop()) is not None:
                yield Path(path)


def add_to_zip(zip: Path, file: Path) -> None:
    """
    Appends a file to a zip file.

    Args:
        zip: the zip file path.
        file: the path to the file that must be added.
    """
    flag = 'a' if zip.is_file() else 'x'
    with ZipFile(zip, flag) as zfile:
        zfile.write(file, file.name)
