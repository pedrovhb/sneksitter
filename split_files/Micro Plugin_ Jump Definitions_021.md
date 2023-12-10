---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions
---
## Accessing micro functions

Some of micro's internal information is exposed in the form of packages which
can be imported by Lua plugins. A package can be imported in Lua and a value
within it can be accessed using the following syntax:

```lua
local micro = import("micro")
micro.Log("Hello")
```

The packages and functions are listed below (in Go type signatures):

* `micro`
    - `TermMessage(msg interface{}...)`: temporarily close micro and print a
       message

    - `TermError(filename string, lineNum int, err string)`: temporarily close
       micro and print an error formatted as `filename, lineNum: err`.

    - `InfoBar()`: return the infobar BufPane object.

    - `Log(msg interface{}...)`: write a message to `log.txt` (requires
       `-debug` flag, or binary built with `build-dbg`).

    - `SetStatusInfoFn(fn string)`: register the given lua function as
       accessible from the statusline formatting options.

    - `CurPane() *BufPane`: returns the current BufPane, or nil if the
       current pane is not a BufPane.

    - `CurTab() *Tab`: returns the current tab.
* `micro/config`
	- `MakeCommand(name string, action func(bp *BufPane, args[]string),
                   completer buffer.Completer)`:
       create a command with the given name, and lua callback function when
       the command is run. A completer may also be given to specify how
       autocompletion should work with the custom command.

	- `FileComplete`: autocomplete using files in the current directory
	- `HelpComplete`: autocomplete using names of help documents
	- `OptionComplete`: autocomplete using names of options
	- `OptionValueComplete`: autocomplete using names of options, and valid
       values afterwards
	- `NoComplete`: no autocompletion suggestions

	- `TryBindKey(k, v string, overwrite bool) (bool, error)`: bind the key
       `k` to the string `v` in the `bindings.json` file.  If `overwrite` is
       true, this will overwrite any existing binding to key `k`. Returns true
       if the binding was made, and a possible error (for example writing to
       `bindings.json` can cause an error).

	- `Reload()`: reload configuration files.

	- `AddRuntimeFileFromMemory(filetype RTFiletype, filename, data string)`:
       add a runtime file to the `filetype` runtime filetype, with name
       `filename` and data `data`.

	- `AddRuntimeFilesFromDirectory(plugin string, filetype RTFiletype,
                                    directory, pattern string)`:
       add runtime files for the given plugin with the given RTFiletype from
       a directory within the plugin root. Only adds files that match the
       pattern using Go's `filepath.Match`

	- `AddRuntimeFile(plugin string, filetype RTFiletype, filepath string)`:
       add a given file inside the plugin root directory as a runtime file
       to the given RTFiletype category.

	- `ListRuntimeFiles(fileType RTFiletype) []string`: returns a list of
       names of runtime files of the given type.

	- `ReadRuntimeFile(fileType RTFiletype, name string) string`: returns the
       contents of a given runtime file.

	- `NewRTFiletype() int`: creates a new RTFiletype, and returns its value.

	- `RTColorscheme`: runtime files for colorschemes.
	- `RTSyntax`: runtime files for syntax files.
	- `RTHelp`: runtime files for help documents.
	- `RTPlugin`: runtime files for plugin source code.

	- `RegisterCommonOption(pl string, name string, defaultvalue interface{})`:
       registers a new option with for the given plugin. The name of the
       option will be `pl.name`, and will have the given default value. Since
       this registers a common option, the option will be modifiable on a
       per-buffer basis, while also having a global value (in the
       GlobalSettings map).

	- `RegisterGlobalOption(pl string, name string, defaultvalue interface{})`:
       same as `RegisterCommonOption` but the option cannot be modified
       locally to each buffer.

	- `GetGlobalOption(name string) interface{}`: returns the value of a
       given plugin in the `GlobalSettings` map.

	- `SetGlobalOption(option, value string) error`: sets an option to a
       given value. Same as using the `> set` command. This will parse the
       value to the actual value type.

	- `SetGlobalOptionNative(option string, value interface{}) error`: sets
       an option to a given value, where the type of value is the actual
       type of the value internally.
* `micro/shell`
	- `ExecCommand(name string, arg ...string) (string, error)`: runs an
       executable with the given arguments, and pipes the output (stderr
       and stdout) of the executable to an internal buffer, which is
       returned as a string, along with a possible error.

	- `RunCommand(input string) (string, error)`: same as `ExecCommand`,
       except this uses micro's argument parser to parse the arguments from
       the input. For example `cat 'hello world.txt' file.txt`, will pass
       two arguments in the `ExecCommand` argument list (quoting arguments
       will preserve spaces).

	- `RunBackgroundShell(input string) (func() string, error)`: returns a
       function that will run the given shell command and return its output.

	- `RunInteractiveShell(input string, wait bool, getOutput bool)
                          (string, error)`:
       temporarily closes micro and runs the given command in the terminal.
       If `wait` is true, micro will wait for the user to press enter before
       returning to text editing. If `getOutput` is true, micro redirect
       stdout from the command to the returned string.

	- `JobStart(cmd string, onStdout, onStderr,
                onExit func(string, []interface{}), userargs ...interface{})
                *exec.Cmd`:
       Starts a background job by running the shell on the given command
       (using `sh -c`). Three callbacks can be provided which will be called
       when the command generates stdout, stderr, or exits. The userargs will
       be passed to the callbacks, along with the output as the first
       argument of the callback.

	- `JobSpawn(cmd string, cmdArgs []string, onStdout, onStderr,
                onExit func(string, []interface{}), userargs ...interface{})
                *exec.Cmd`:
       same as `JobStart`, except doesn't run the command through the shell
       and instead takes as inputs the list of arguments.

	- `JobStop(cmd *exec.Cmd)`: kills a job.
	- `JobSend(cmd *exec.Cmd, data string)`: sends some data to a job's stdin.

	- `RunTermEmulator(h *BufPane, input string, wait bool, getOutput bool,
                       callback func(out string, userargs []interface{}),
                       userargs []interface{}) error`:
       starts a terminal emulator from a given BufPane with the input command.
       If `wait` is true it will wait for the user to exit by pressing enter
       once the executable has terminated and if `getOutput` is true it will
       redirect the stdout of the process to a pipe which will be passed to
       the callback which is a function that takes a string and a list of
       optional user arguments. This function returns an error on systems
       where the terminal emulator is not supported.

	- `TermEmuSupported`: true on systems where the terminal emulator is
       supported and false otherwise. Supported systems:
        * Linux
        * MacOS
        * Dragonfly
        * OpenBSD
        * FreeBSD

* `micro/buffer`
    - `NewMessage(owner string, msg string, start, end, Loc, kind MsgType)
                  *Message`:
       creates a new message with an owner over a range given by the start
       and end locations.

    - `NewMessageAtLine(owner string, msg string, line int, kindMsgType)
                        *Message`:
       creates a new message with owner, type and message at a given line.

    - `MTInfo`: info message.
    - `MTWarning`: warning message.
    - `MTError` error message.

    - `Loc(x, y int) Loc`: creates a new location struct.
    - `SLoc(line, row int) display.SLoc`: creates a new scrolling location struct.

    - `BTDefault`: default buffer type.
    - `BTLog`: log buffer type.
    - `BTRaw`: raw buffer type.
    - `BTInfo`: info buffer type.

    - `NewBuffer(text, path string) *Buffer`: creates a new buffer with the
       given text at a certain path.

    - `NewBufferFromFile(path string) (*Buffer, error)`: creates a new
       buffer by reading from disk at the given path.

    - `ByteOffset(pos Loc, buf *Buffer) int`: returns the byte index of the
       given position in a buffer.

    - `Log(s string)`: writes a string to the log buffer.
    - `LogBuf() *Buffer`: returns the log buffer.
* `micro/util`
    - `RuneAt(str string, idx int) string`: returns the utf8 rune at a
       given index within a string.
    - `GetLeadingWhitespace(s string) string`: returns the leading
       whitespace of a string.
    - `IsWordChar(s string) bool`: returns true if the first rune in a
       string is a word character.
    - `String(b []byte) string`: converts a byte array to a string.
    - `RuneStr(r rune) string`: converts a rune to a string.
    - `Unzip(src, dest string) error`: unzips a file to given folder.
    - `HttpRequest(method string, url string, headers []string) (http.Response, error)`: makes a http request.

This may seem like a small list of available functions but some of the objects
returned by the functions have many methods. The Lua plugin may access any
public methods of an object returned by any of the functions above.
Unfortunately it is not possible to list all the available functions on this
page. Please go to the internal documentation at
https://pkg.go.dev/github.com/zyedidia/micro/v2/internal to see the full list
of available methods. Note that only methods of types that are available to
plugins via the functions above can be called from a plugin. For an even more
detailed reference see the source code on Github.

For example, with a BufPane object called `bp`, you could call the `Save`
function in Lua with `bp:Save()`.

Note that Lua uses the `:` syntax to call a function rather than Go's `.`
syntax.

```go
micro.InfoBar().Message()
```

turns to

```lua
micro.InfoBar():Message()
```

