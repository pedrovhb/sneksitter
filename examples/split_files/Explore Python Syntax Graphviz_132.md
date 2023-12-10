# Assistant

It appears that the `MemoryError` persists despite implementing memoization to avoid infinite loops. The issue might be related to the complexity of the SQLite grammar and how the `next_state` and `lookahead_iterator` methods interact with it. These methods are likely producing a large number of possible next states and lookahead symbols, causing the function to generate excessive data.

One way to narrow down the issue is to limit the range of lookahead symbols processed. Another approach is to add more debugging information to identify where the algorithm is consuming excessive memory.

I'll start by adding debugging outputs to better understand the flow and identify potential bottlenecks.

[child ⬇️](#e0bc9c91-f128-40a3-a23a-45a02c493dae)

---

(main branch ⎇)
###### e0bc9c91-f128-40a3-a23a-45a02c493dae
[parent ⬆️](#38d93ec2-136c-4778-8f38-fa2d23724b22)
