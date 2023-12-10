# Tool

```python
---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
Cell In[7], line 18
     16 # Rendering the graph to a new PNG file
     17 dot_file_path = '/mnt/data/python_syntax_tree_hierarchical'
---> 18 dot.render(dot_file_path)
     20 # Check the new dimensions
     21 with Image.open(dot_file_path + '.png') as img:

File ~/.local/lib/python3.8/site-packages/graphviz/files.py:238, in File.render(self, filename, directory, view, cleanup, format, renderer, formatter, quiet, quiet_view)
    235 if format is None:
    236     format = self._format
--> 238 rendered = backend.render(self._engine, format, filepath,
    239                           renderer=renderer, formatter=formatter,
    240                           quiet=quiet)
    242 if cleanup:
    243     log.debug('delete %r', filepath)

File ~/.local/lib/python3.8/site-packages/graphviz/backend.py:235, in render(***failed resolving arguments***)
    232 else:
    233     cwd = None
--> 235 run(cmd, capture_output=True, cwd=cwd, check=True, quiet=quiet)
    236 return rendered

File ~/.local/lib/python3.8/site-packages/graphviz/backend.py:177, in run(cmd, input, capture_output, check, encoding, quiet, **kwargs)
    174     else:
    175         raise
--> 177 out, err = proc.communicate(input)
    179 if not quiet and err:
    180     err_encoding = sys.stderr.encoding or sys.getdefaultencoding()

File /usr/lib/python3.8/subprocess.py:1028, in Popen.communicate(self, input, timeout)
   1025     endtime = None
   1027 try:
-> 1028     stdout, stderr = self._communicate(input, endtime, timeout)
   1029 except KeyboardInterrupt:
   1030     # https://bugs.python.org/issue25942
   1031     # See the detailed comment in .wait().
   1032     if timeout is not None:

File /usr/lib/python3.8/subprocess.py:1868, in Popen._communicate(self, input, endtime, orig_timeout)
   1861     self._check_timeout(endtime, orig_timeout,
   1862                         stdout, stderr,
   1863                         skip_check_and_raise=True)
   1864     raise RuntimeError(  # Impossible :)
   1865         '_check_timeout(..., skip_check_and_raise=True) '
   1866         'failed to raise TimeoutExpired.')
-> 1868 ready = selector.select(timeout)
   1869 self._check_timeout(endtime, orig_timeout, stdout, stderr)
   1871 # XXX Rewrite these to use non-blocking I/O on the file
   1872 # objects; they are no longer using C stdio!

File /usr/lib/python3.8/selectors.py:415, in _PollLikeSelector.select(self, timeout)
    413 ready = []
    414 try:
--> 415     fd_event_list = self._selector.poll(timeout)
    416 except InterruptedError:
    417     return ready

KeyboardInterrupt: 

WARNING: Automatic interrupt triggered after 60.0 seconds.
```

[child ⬇️](#aaa2e2a0-b4eb-4a3c-9f31-f32a381933ca)

---

(main branch ⎇)
###### aaa2e2a0-b4eb-4a3c-9f31-f32a381933ca
[parent ⬆️](#d0c92034-93f9-4197-8cdc-4d69c7e62459)
