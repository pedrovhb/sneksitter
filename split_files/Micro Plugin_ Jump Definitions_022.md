---
file: /home/pedro/Documents/chatgpt_export/Markdown/Micro Plugin_ Jump Definitions.md
heading_stack: <root> -> e239441e-b426-4499-8b1d-3353241cbedd -> System -> c7ec2628-081c-4452-bad7-9d9408a37dbe -> System -> aaa2959b-ba07-4598-ae83-f18f3743ceda -> User -> 55a82fb5-6597-4870-bc54-3f056fcc765d -> Assistant -> aaa28f27-4c2e-43e0-bd23-02e759e2a046 -> User -> 13728b7a-2735-4e1d-9a06-14e6d8e00587 -> Assistant -> aaa22449-e24e-47d9-8610-6cdba5cba27e -> User -> 8726a647-85de-484c-a4a8-09246e56d7d3 -> Assistant -> aaa2dc7a-7bca-4ccf-b445-8af0a21c8fe5 -> User -> Plugins -> Lua callbacks -> Accessing micro functions -> Accessing the Go standard library
---
## Accessing the Go standard library

It is possible for your lua code to access many of the functions in the Go
standard library.

Simply import the package you'd like and then you can use it. For example:

```lua
local ioutil = import("io/ioutil")
local fmt = import("fmt")
local micro = import("micro")

local data, err = ioutil.ReadFile("SomeFile.txt")

if err ~= nil then
    micro.InfoBar():Error("Error reading file: SomeFile.txt")
else
    -- Data is returned as an array of bytes
    -- Using Sprintf will convert it to a string
    local str = fmt.Sprintf("%s", data)

    -- Do something with the file you just read!
    -- ...
end
```

Here are the packages from the Go standard library that you can access.
Nearly all functions from these packages are supported. For an exact
list of which functions are supported you can look through `lua.go`
(which should be easy to understand).

```
fmt
io
io/ioutil
net
math
math/rand
os
runtime
path
filepath
strings
regexp
errors
time
archive/zip
net/http
```

For documentation for each of these functions, see the Go standard
library documentation at https://golang.org/pkg/ (for the packages
exposed to micro plugins). The Lua standard library is also available
to plugins though it is rather small.

The following functions are also available from the go-humanize package:

The `humanize` package exposes:
* `Bytes`
* `Ordinal`

