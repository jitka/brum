import tarfile
import io

stream = io.open("archive.tar.gz", mode="rb")
stream = io.open("example/example.txt", mode="rb")
stream = io.open("example.zip", mode="rb")
#stream = io.open("archive.tar", mode="rb")
tarf = tarfile.open(fileobj=stream, mode="r")

records = []
for member in tarf.getmembers():
    extracted_member = tarf.extractfile(member)
    if extracted_member:
        records.append(
            {
                "identifier": member.name,
                "payload": extracted_member.read().decode(encoding="utf-8"),
            }
        )

print(records)
