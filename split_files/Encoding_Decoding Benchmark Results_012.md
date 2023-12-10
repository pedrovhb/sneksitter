---
file: /home/pedro/Documents/chatgpt_export/Markdown/Encoding_Decoding Benchmark Results.md
heading_stack: <root> -> 45bfa0f9-0280-4536-84fe-9f5a2b886748 -> System -> 6e6dc52e-87cd-443f-8455-8f3b2627c1a5 -> System -> aaa2d7d6-5705-4351-a4b5-6ac5b9bb328d -> User -> 2fb2df16-e3b9-43e8-b679-167cac98874e -> Assistant -> 99cabd56-53c1-4d29-95a7-64a236319ddf -> Tool -> 6e23f93f-78cb-4931-95c5-1a03ade96cc2 -> Assistant
---
# Assistant

```python
# Plotting the benchmark results for visualization
plt.figure(figsize=(12, 8))
plt.barh(df_benchmark_results['Function'], df_benchmark_results['Time (s)'], color='teal')
plt.xlabel('Time (s)')
plt.ylabel('Function')
plt.title('Benchmarking Encoding/Decoding Functions')
plt.grid(True)

# Annotate the bars with the actual time values
for i, v in enumerate(df_benchmark_results['Time (s)']):
    plt.text(v + 0.001, i, f"{v:.5f}", va='center', color='black')

plt.show()
```

[child ⬇️](#6417ee72-c53a-491c-b535-4ee25c0edae1)

---

(main branch ⎇)
###### 6417ee72-c53a-491c-b535-4ee25c0edae1
[parent ⬆️](#6e23f93f-78cb-4931-95c5-1a03ade96cc2)
