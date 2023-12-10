---
file: /home/pedro/Documents/chatgpt_export/Markdown/C# to Nim translation.md
heading_stack: <root> -> c62d72d9-69d2-43a4-b2b8-661a1133e5ea -> System -> 5a0b0a56-d40a-4cbd-b9cd-723b26f630d1 -> System -> aaa29c1a-79ad-4c94-b557-f135da09a3d7 -> User -> d005864f-c7a0-487f-9627-1ff49abcab93 -> Assistant -> aaa2f9df-dd43-4caf-a6bc-ca77cac9e1c5 -> User -> a12fb9a7-62bb-46e0-a9a8-7fc51c7009da -> Assistant
---
# Assistant

```python
# Implementing the full Pruning Radix Trie in Nim
nim_code = '''
import strutils, tables, sequtils, times, streams, os, algorithms

type
  Node = object
    termFrequencyCount: int64
    termFrequencyCountChildMax: int64
    children: seq[(string, ref Node)]

  PruningRadixTrie = object
    termCount: int64
    termCountLoaded: int64
    trie: Node

proc initNode(termFrequencyCount: int64): Node =
  Node(termFrequencyCount: termFrequencyCount, children: @[])

proc initTrie(): PruningRadixTrie =
  PruningRadixTrie(trie: initNode(0))

proc updateMaxCounts(nodeList: var seq[ref Node], termFrequencyCount: int64) =
  for node in nodeList:
    if termFrequencyCount > node.termFrequencyCountChildMax:
      node.termFrequencyCountChildMax = termFrequencyCount

proc addTerm(trie: var PruningRadixTrie, curr: var Node, term: string, termFrequencyCount: int64, id: int, level: int, nodeList: var seq[ref Node]) =
  try:
    nodeList.add(addr curr)
    var common = 0

    if curr.children != nil:
      for j in 0..<curr.children.len:
        let (key, node) = curr.children[j]
        for i in 0..<min(term.len, key.len):
          if term[i] == key[i]:
            common = i + 1
          else:
            break

        if common > 0:
          if common == term.len and common == key.len:
            if node.termFrequencyCount == 0:
              trie.termCount += 1
            node.termFrequencyCount += termFrequencyCount
            updateMaxCounts(nodeList, node.termFrequencyCount)

          elif common == term.len:
            var child = initNode(termFrequencyCount)
            child.children = @[(key[common..^1], node)]
            child.termFrequencyCountChildMax = max(node.termFrequencyCountChildMax, node.termFrequencyCount)
            updateMaxCounts(nodeList, termFrequencyCount)
            curr.children[j] = (term[0..common-1], addr child)
            curr.children.sort do(a, b: (string, ref Node)) -> int:
              b[1].termFrequencyCountChildMax - a[1].termFrequencyCountChildMax
            trie.termCount += 1

          elif common == key.len:
            addTerm(trie, node[], term[common..^1], termFrequencyCount, id, level + 1, nodeList)

          else:
            var child = initNode(0)
            child.children = @[(key[common..^1], node), (term[common..^1], addr initNode(termFrequencyCount))]
            child.termFrequencyCountChildMax = max(node.termFrequencyCountChildMax, max(termFrequencyCount, node.termFrequencyCount))
            updateMaxCounts(nodeList, termFrequencyCount)
            curr.children[j] = (term[0..common-1], addr child)
            curr.children.sort do(a, b: (string, ref Node)) -> int:
              b[1].termFrequencyCountChildMax - a[1].termFrequencyCountChildMax
            trie.termCount += 1
          return

    if curr.children == nil:
      curr.children = @[(term, addr initNode(termFrequencyCount))]
    else:
      curr.children.add (term, addr initNode(termFrequencyCount))
      curr.children.sort do(a, b: (string, ref Node)) -> int:
        b[1].termFrequencyCountChildMax - a[1].termFrequencyCountChildMax

    trie.termCount += 1
    updateMaxCounts(nodeList, termFrequencyCount)

  except Exception as e:
    echo "Exception: ", e.msg

# ... Implement other methods
'''

# Saving the Nim code to a file for the user to download
with open("/mnt/data/PruningRadixTrie.nim", "w") as f:
    f.write(nim_code)

"/mnt/data/PruningRadixTrie.nim"
```

[child ⬇️](#69aab37f-d4ee-41f7-a789-7eca71c005cf)

---

(main branch ⎇)
###### 69aab37f-d4ee-41f7-a789-7eca71c005cf
[parent ⬆️](#a12fb9a7-62bb-46e0-a9a8-7fc51c7009da)
