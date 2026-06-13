with open("setup.py", "r") as f:
  c = f.read()

print("Original content:")
print(c)

c = (c
     .replace(
       # https://github.com/Morton-Li/PyTorch-MacOS-Builder/blob/main/patches/0000-project.patch
"""            install_name_tool_args = [
                "-rpath",
                rpath,
                "@loader_path",
            ]""",
"""            install_name_tool_args = ["-delete_rpath", rpath] if "@loader_path" in rpaths else ["-rpath", rpath, "@loader_path"]"""
     )
)

with open("setup.py", "w") as f:
  f.write(c)

with open("setup.py", "r") as f:
  c = f.read()

print("Modified content:")
print(c)
