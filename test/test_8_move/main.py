import shutil

base = "./test/test_8_move"

archive = shutil.make_archive(f"{base}/backup", "zip", f"{base}/Temp")

print(archive)

shutil.unpack_archive(archive, f"{base}/new_folder")