from pathlib import Path

p = Path("example.txt")
p.write_text("Hello world!")

print(p.read_text())
print("Exists: ", p.exists())

absolute_path = p.absolute()

print("absolute_path :> ", absolute_path)

relative_path = absolute_path.relative_to(absolute_path)

print("relative_path :> ", relative_path)