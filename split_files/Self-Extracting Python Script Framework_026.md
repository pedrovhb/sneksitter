---
file: /home/pedro/Documents/chatgpt_export/Markdown/Self-Extracting Python Script Framework.md
heading_stack: <root> -> b84c160d-01f8-4464-bdcb-ce33aed920f2 -> System -> 223bd57b-5a68-450f-8413-2c9aaa3de884 -> System -> aaa2f0a0-5c47-46c8-9517-226c34230146 -> User -> 0fec26b9-8a0c-4dfc-b842-fb7cf4697924 -> Assistant -> Problem Exploration and Design Specification -> Problem Statement -> Core Components -> Data Packing -> Data Unpacking -> Operation Interfaces -> Script Generation -> Specifications -> aaa28cbe-9139-4539-915e-cee347975b63 -> User -> 2d6e1ca0-1786-4102-b30e-5545b9b2f1e0 -> Assistant -> aaa2fcae-5154-4dac-91c6-f8c98e0dba1f -> User -> e7d6cadc-2ed5-4673-aa24-5eabdf011818 -> Assistant -> 4ab984b5-d8c1-4463-83b0-dd85ff18f35f -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[1], line 82
     80 paths = ["some_file.txt", "some_folder"]
     81 operations = [InstallLibraries(["numpy", "pandas"])]
---> 82 packed_data = pack_data(paths)
     83 script = generate_script(operations, packed_data)
     84 print(script)

Cell In[1], line 48, in pack_data(paths)
     46 with tarfile.open(fileobj=temp_file, mode="w:gz") as tar:
     47     for path in paths:
---> 48         tar.add(path)
     49 temp_file.seek(0)
     50 return base64.b64encode(temp_file.read()).decode('utf-8')

File /usr/lib/python3.8/tarfile.py:1955, in TarFile.add(self, name, arcname, recursive, filter)
   1952 self._dbg(1, name)
   1954 # Create a TarInfo object from the file.
-> 1955 tarinfo = self.gettarinfo(name, arcname)
   1957 if tarinfo is None:
   1958     self._dbg(1, "tarfile: Unsupported type %r" % name)

File /usr/lib/python3.8/tarfile.py:1834, in TarFile.gettarinfo(self, name, arcname, fileobj)
   1832 if fileobj is None:
   1833     if not self.dereference:
-> 1834         statres = os.lstat(name)
   1835     else:
   1836         statres = os.stat(name)

FileNotFoundError: [Errno 2] No such file or directory: 'some_file.txt'

```

[child ⬇️](#2e7a6320-a857-4f06-9c46-2438d80bb331)

---

(main branch ⎇)
###### 2e7a6320-a857-4f06-9c46-2438d80bb331
[parent ⬆️](#4ab984b5-d8c1-4463-83b0-dd85ff18f35f)
