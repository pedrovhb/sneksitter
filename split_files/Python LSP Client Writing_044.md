---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python LSP Client Writing.md
heading_stack: <root> -> fb86b0e7-bf62-4975-be52-afe44c28e2ea -> System -> 93a72920-b6b0-4849-ae9f-6a6bac06bf87 -> System -> aaa23743-d4b8-479a-9cf4-b7e357d2d973 -> User -> 3a85587d-63d2-4e15-a912-383beeee1f3b -> Assistant -> 2cbd10f3-6642-4021-9e90-a67e05827bf9 -> Tool -> 22a86aba-e3b8-4805-a841-9752070c999b -> Assistant -> Language Server Protocol (LSP) -> Features -> Workflow -> Writing a Python Client for LSP -> Example Libraries -> Example Code Outline -> aaa2528e-4c1f-4ad0-991b-16ed764da716 -> User -> 4a334677-9d0e-4635-afaa-e2795893b1a9 -> Assistant -> c3734514-9dae-4be3-8123-c1558578e838 -> Tool -> 0f6f37b3-6ec2-43a7-b76f-bae08d4ce51c -> Assistant -> 580895c4-5981-4f16-a55d-41ba1ab8af1e -> Assistant -> 6e38ed5a-91cb-43b9-986c-658dcecf8cf0 -> Tool -> 9fff6a60-716a-4a71-ba99-d15523367a56 -> Assistant -> aaa252ee-32d8-49fa-aa5b-565c1180a6e6 -> User -> ba806386-ffe6-41cf-bd96-214301f8b3d6 -> Assistant -> ffe0c567-a0f6-42e1-b0dd-ef6442fd4e14 -> Tool -> aaa28b11-8a59-4317-b066-13d7134b3907 -> User -> 76860d41-3d67-4ece-8738-74647d574dca -> Assistant -> 32ca632e-0f15-4dda-8d27-f3ef3e83beff -> Tool
---
# Tool

```python
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
Cell In[5], line 40
     37     return response_json
     39 # Run the asyncio function and display the LSP server response
---> 40 await lsp_server_communication()

Cell In[5], line 6, in lsp_server_communication()
      4 async def lsp_server_communication():
      5     # Launch python-lsp-server as a subprocess
----> 6     process = await asyncio.create_subprocess_exec(
      7         'python-lsp-server',
      8         stdin=asyncio.subprocess.PIPE,
      9         stdout=asyncio.subprocess.PIPE,
     10         stderr=asyncio.subprocess.PIPE
     11     )
     13     # Send an initialization request to the LSP server
     14     initialize_params = {
     15         "jsonrpc": "2.0",
     16         "id": 1,
   (...)
     23         }
     24     }

File /usr/lib/python3.8/asyncio/subprocess.py:236, in create_subprocess_exec(program, stdin, stdout, stderr, loop, limit, *args, **kwds)
    229     warnings.warn("The loop argument is deprecated since Python 3.8 "
    230                   "and scheduled for removal in Python 3.10.",
    231                   DeprecationWarning,
    232                   stacklevel=2
    233     )
    234 protocol_factory = lambda: SubprocessStreamProtocol(limit=limit,
    235                                                     loop=loop)
--> 236 transport, protocol = await loop.subprocess_exec(
    237     protocol_factory,
    238     program, *args,
    239     stdin=stdin, stdout=stdout,
    240     stderr=stderr, **kwds)
    241 return Process(transport, protocol, loop)

File /usr/lib/python3.8/asyncio/base_events.py:1630, in BaseEventLoop.subprocess_exec(self, protocol_factory, program, stdin, stdout, stderr, universal_newlines, shell, bufsize, encoding, errors, text, *args, **kwargs)
   1628     debug_log = f'execute program {program!r}'
   1629     self._log_subprocess(debug_log, stdin, stdout, stderr)
-> 1630 transport = await self._make_subprocess_transport(
   1631     protocol, popen_args, False, stdin, stdout, stderr,
   1632     bufsize, **kwargs)
   1633 if self._debug and debug_log is not None:
   1634     logger.info('%s: %r', debug_log, transport)

File /usr/lib/python3.8/asyncio/unix_events.py:197, in _UnixSelectorEventLoop._make_subprocess_transport(self, protocol, args, shell, stdin, stdout, stderr, bufsize, extra, **kwargs)
    194     raise RuntimeError("asyncio.get_child_watcher() is not activated, "
    195                        "subprocess support is not installed.")
    196 waiter = self.create_future()
--> 197 transp = _UnixSubprocessTransport(self, protocol, args, shell,
    198                                   stdin, stdout, stderr, bufsize,
    199                                   waiter=waiter, extra=extra,
    200                                   **kwargs)
    202 watcher.add_child_handler(transp.get_pid(),
    203                           self._child_watcher_callback, transp)
    204 try:

File /usr/lib/python3.8/asyncio/base_subprocess.py:36, in BaseSubprocessTransport.__init__(self, loop, protocol, args, shell, stdin, stdout, stderr, bufsize, waiter, extra, **kwargs)
     34 # Create the child process: set the _proc attribute
     35 try:
---> 36     self._start(args=args, shell=shell, stdin=stdin, stdout=stdout,
     37                 stderr=stderr, bufsize=bufsize, **kwargs)
     38 except:
     39     self.close()

File /usr/lib/python3.8/asyncio/unix_events.py:789, in _UnixSubprocessTransport._start(self, args, shell, stdin, stdout, stderr, bufsize, **kwargs)
    787     stdin, stdin_w = socket.socketpair()
    788 try:
--> 789     self._proc = subprocess.Popen(
    790         args, shell=shell, stdin=stdin, stdout=stdout, stderr=stderr,
    791         universal_newlines=False, bufsize=bufsize, **kwargs)
    792     if stdin_w is not None:
    793         stdin.close()

File /usr/lib/python3.8/subprocess.py:858, in Popen.__init__(self, args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags, restore_signals, start_new_session, pass_fds, encoding, errors, text)
    854         if self.text_mode:
    855             self.stderr = io.TextIOWrapper(self.stderr,
    856                     encoding=encoding, errors=errors)
--> 858     self._execute_child(args, executable, preexec_fn, close_fds,
    859                         pass_fds, cwd, env,
    860                         startupinfo, creationflags, shell,
    861                         p2cread, p2cwrite,
    862                         c2pread, c2pwrite,
    863                         errread, errwrite,
    864                         restore_signals, start_new_session)
    865 except:
    866     # Cleanup if the child failed starting.
    867     for f in filter(None, (self.stdin, self.stdout, self.stderr)):

File /usr/lib/python3.8/subprocess.py:1704, in Popen._execute_child(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, restore_signals, start_new_session)
   1702     if errno_num != 0:
   1703         err_msg = os.strerror(errno_num)
-> 1704     raise child_exception_type(errno_num, err_msg, err_filename)
   1705 raise child_exception_type(err_msg)

FileNotFoundError: [Errno 2] No such file or directory: 'python-lsp-server'

```

[child ⬇️](#abfa122e-b2f6-4c37-832e-66748bf19c62)

---

(main branch ⎇)
###### abfa122e-b2f6-4c37-832e-66748bf19c62
[parent ⬆️](#32ca632e-0f15-4dda-8d27-f3ef3e83beff)
