---
file: /home/pedro/Documents/chatgpt_export/Markdown/Self-Extracting Python Script Framework.md
heading_stack: <root> -> b84c160d-01f8-4464-bdcb-ce33aed920f2 -> System -> 223bd57b-5a68-450f-8413-2c9aaa3de884 -> System -> aaa2f0a0-5c47-46c8-9517-226c34230146 -> User -> 0fec26b9-8a0c-4dfc-b842-fb7cf4697924 -> Assistant -> Problem Exploration and Design Specification -> Problem Statement -> Core Components -> Data Packing -> Data Unpacking -> Operation Interfaces -> Script Generation -> Specifications -> aaa28cbe-9139-4539-915e-cee347975b63 -> User -> 2d6e1ca0-1786-4102-b30e-5545b9b2f1e0 -> Assistant -> aaa2fcae-5154-4dac-91c6-f8c98e0dba1f -> User -> e7d6cadc-2ed5-4673-aa24-5eabdf011818 -> Assistant -> 4ab984b5-d8c1-4463-83b0-dd85ff18f35f -> Tool -> 2e7a6320-a857-4f06-9c46-2438d80bb331 -> Assistant -> 30890fc7-d405-44a9-b4b4-5755b79309c7 -> Assistant -> 8cfa77c9-ffc0-42a1-b070-72225b99093d -> Tool -> 682274cb-508e-40ea-b309-1c8ae23ed8ad -> Assistant -> aaa2c4c9-6f1b-496c-98e9-fb1ccce31bff -> User -> f58e1ce0-a2bf-4b5a-8a83-c57d7ae7b39d -> Assistant -> fb30f088-a47f-4bd3-880d-f080eedfdb46 -> Tool -> 677e81ba-f9f5-4ba1-83af-d8d440a13496 -> Assistant -> aaa2c27f-0250-48cb-add7-fd54540b0234 -> User -> f02a8a00-3031-488f-bf57-8835c4ca4d6f -> Assistant -> e866aa99-f1a7-4870-827b-8c06a0e3915a -> Tool -> 413b4363-ad69-4eb5-8d5e-667f7d020362 -> Assistant -> 793aab43-70aa-41ec-b7a6-0ab63ec8a525 -> Assistant -> e52d5cb6-2f2b-44be-b794-0588eeade6d3 -> Tool -> 766ec117-77d1-4ea6-a523-babdacae42b3 -> Assistant -> aaa2425f-c007-4084-9bf0-c2e9bbd0cc87 -> User -> b9d172ae-f754-4f2a-b1b7-52e3595b04ed -> Assistant -> aaa236ee-be72-4876-bc42-eb3cb9b3d464 -> User -> 6a5bd6e8-ae96-43ed-9d91-2d422817c5b3 -> Assistant -> 68e1fb0f-6312-49f9-adb1-0f4d0db90748 -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[6], line 39
     37 # Include whl files in packed data
     38 paths_to_pack = [str(temp_file), str(whl_dir)]
---> 39 packed_data = pack_data(paths_to_pack)
     41 # Generate script
     42 script = generate_script(operations, packed_data)

Cell In[3], line 37, in pack_data(paths)
     35 with tarfile.open(fileobj=temp_file, mode="w:gz") as tar:
     36     for path in paths:
---> 37         tar.add(path)
     38 temp_file.seek(0)
     39 return base64.b64encode(temp_file.read()).decode('utf-8')

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

FileNotFoundError: [Errno 2] No such file or directory: 'temp_demo_folder/some_file.txt'

```

[child ⬇️](#ed8a1906-014d-4b34-9966-39de6d88935c)

---

(main branch ⎇)
###### ed8a1906-014d-4b34-9966-39de6d88935c
[parent ⬆️](#68e1fb0f-6312-49f9-adb1-0f4d0db90748)
