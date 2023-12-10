---
file: /home/pedro/Documents/chatgpt_export/Markdown/Setup Environment_ Timeout Issue.md
heading_stack: <root> -> f7835fe7-1d38-4bba-b690-0a7e45027bb8 -> System -> a74211a6-4100-4343-a7d2-1cdc7eb28288 -> System -> aaa26c76-0115-455e-a7e5-48072e737bc7 -> User -> 7cf98d2b-ea66-427c-a31e-42f2adbbd70b -> Assistant -> 5750445e-cd88-45c5-9622-3152967bee5a -> Tool
---
# Tool

```python
INFO:root:Temporary directory created: /tmp/tmpzxc5xyhr
INFO:root:Extracted archive to /tmp/tmpzxc5xyhr
INFO:root:Installing toolz, tree_sitter_languages, pydantic, wrapt, intervaltree, sortedcontainers, records, attrs, bitarray, rope, astor, astunparse, datasette, sqlite-utils, rich, jmespath and its dependencies
[33mWARNING: Ignoring invalid distribution - (/home/sandbox/.local/lib/python3.8/site-packages)[0m[33m
[0m[33mWARNING: Ignoring invalid distribution - (/home/sandbox/.local/lib/python3.8/site-packages)[0m[33m
[0m[33mDEPRECATION: textract 1.6.4 has a non-standard dependency specifier extract-msg<=0.29.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of textract or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063[0m[33m
[0m[31mERROR: Operation cancelled by user[0m[31m
[0m---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[1], line 3
      1 # Moving the setup_env.py file to the current working directory and importing it.
      2 get_ipython().system('mv /mnt/data/setup_env.py .')
----> 3 import setup_env

File ~/setup_env.py:30
     27 package_names = ('toolz', 'tree_sitter_languages', 'pydantic', 'wrapt', 'intervaltree', 'sortedcontainers', 'records', 'attrs', 'bitarray', 'rope', 'astor', 'astunparse', 'datasette', 'sqlite-utils', 'rich', 'jmespath')
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

[child ⬇️](#7e5aea34-ad80-4cd7-9984-0da00a5e0b10)

---

(main branch ⎇)
###### 7e5aea34-ad80-4cd7-9984-0da00a5e0b10
[parent ⬆️](#5750445e-cd88-45c5-9622-3152967bee5a)
