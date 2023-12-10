---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Interrupted_ Try Again.md
heading_stack: <root> -> c8410881-41b4-4fe7-9997-92dc1d24904c -> System -> 4395d5a3-0365-45fa-bad2-c05d2ba6f9f0 -> System -> aaa2f36e-2656-4d15-8e85-adbb682c3eb5 -> User -> 1c420225-b9d1-43a0-9c4e-66ec44187760 -> Assistant -> 58b9dd79-42c6-43b6-aea7-2f8a9f0d7068 -> Tool
---
# Tool

```python
INFO:root:Temporary directory created: /tmp/tmp65k8cr2a
INFO:root:Extracted archive to /tmp/tmp65k8cr2a
INFO:root:Installing toolz, tree_sitter_languages, pydantic, wrapt, intervaltree, sortedcontainers, records, attrs, bitarray, rope, astor, astunparse, datasette, sqlite-utils, rich, jmespath, problog and its dependencies
[33mWARNING: Ignoring invalid distribution - (/home/sandbox/.local/lib/python3.8/site-packages)[0m[33m
[0m[33mWARNING: Ignoring invalid distribution - (/home/sandbox/.local/lib/python3.8/site-packages)[0m[33m
[0m[33mDEPRECATION: textract 1.6.4 has a non-standard dependency specifier extract-msg<=0.29.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of textract or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
[0m[31mERROR: Operation cancelled by user[0m[31m
[0m---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[1], line 3
      1 # Moving the setup file to the current working directory and importing it
      2 get_ipython().system('mv /mnt/data/setup_env.py .')
----> 3 import setup_env

File ~/setup_env.py:30
     27 package_names = ('toolz', 'tree_sitter_languages', 'pydantic', 'wrapt', 'intervaltree', 'sortedcontainers', 'records', 'attrs', 'bitarray', 'rope', 'astor', 'astunparse', 'datasette', 'sqlite-utils', 'rich', 'jmespath', 'problog')
     28 logging.info(f"Installing {', '.join(package_names)} and its dependencies")
---> 30 subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "--no-cache-dir", "-U", "--no-index", "--force-reinstall", "--find-links=" + tmp_path, *package_names])
     31 logging.info(f"Installed {', '.join(package_names)} and its dependencies")
     33 sys.path.append(tmp_path)

File /usr/lib/python3.8/subprocess.py:495, in run(input, capture_output, timeout, check, *popenargs, **kwargs)
    493 with Popen(*popenargs, **kwargs) as process:
    494     try:
--> 495         stdout, stderr = process.communicate(input, timeout=timeout)
    496     except TimeoutExpired as exc:
    497         process.kill()

File /usr/lib/python3.8/subprocess.py:1020, in Popen.communicate(self, input, timeout)
   1018         stderr = self.stderr.read()
   1019         self.stderr.close()
-> 1020     self.wait()
   1021 else:
   1022     if timeout is not None:

File /usr/lib/python3.8/subprocess.py:1083, in Popen.wait(self, timeout)
   1081     endtime = _time() + timeout
   1082 try:
-> 1083     return self._wait(timeout=timeout)
   1084 except KeyboardInterrupt:
   1085     # https://bugs.python.org/issue25942
   1086     # The first keyboard interrupt waits briefly for the child to
   1087     # exit under the common assumption that it also received the ^C
   1088     # generated SIGINT and will exit rapidly.
   1089     if timeout is not None:

File /usr/lib/python3.8/subprocess.py:1806, in Popen._wait(self, timeout)
   1804 if self.returncode is not None:
   1805     break  # Another thread waited.
-> 1806 (pid, sts) = self._try_wait(0)
   1807 # Check the pid and loop as waitpid has been known to
   1808 # return 0 even without WNOHANG in odd situations.
   1809 # http://bugs.python.org/issue14396.
   1810 if pid == self.pid:

File /usr/lib/python3.8/subprocess.py:1764, in Popen._try_wait(self, wait_flags)
   1762 """All callers to this function MUST hold self._waitpid_lock."""
   1763 try:
-> 1764     (pid, sts) = os.waitpid(self.pid, wait_flags)
   1765 except ChildProcessError:
   1766     # This happens if SIGCLD is set to be ignored or waiting
   1767     # for child processes has otherwise been disabled for our
   1768     # process.  This child is dead, we can't get the status.
   1769     pid = self.pid

KeyboardInterrupt: 

WARNING: Automatic interrupt triggered after 60.0 seconds.
```

[child ⬇️](#101d1b2a-a550-46ac-bd03-00de0adbcca9)

---

(main branch ⎇)
###### 101d1b2a-a550-46ac-bd03-00de0adbcca9
[parent ⬆️](#58b9dd79-42c6-43b6-aea7-2f8a9f0d7068)
