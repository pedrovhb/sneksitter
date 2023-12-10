---
file: /home/pedro/Documents/chatgpt_export/Markdown/Scraping Tree-Sitter Parsers Failed.md
heading_stack: <root> -> d983c898-d843-48b2-8d19-e6358c6b3117 -> System -> e17b45cd-afd8-40ff-9f17-efd45736b653 -> System -> aaa20636-5e4b-4441-bb5f-bf9eba90dce2 -> User -> 432ed60e-ec95-40ea-b496-fd523a6dea8d -> Assistant -> 46b32ca1-24f5-4323-8f5d-f353801b264c -> Tool -> 5d6e7cb4-e20c-4759-95a6-070b010d5169 -> Assistant -> aeb33008-033e-4c51-9795-353210680c11 -> Tool -> 72a817b1-2783-48d4-bf78-8f9daa221f44 -> Assistant -> c73162e6-83db-48ae-8c00-9fd50a81c5af -> Tool -> 7da4ef10-11a0-4f4f-8aec-d157fe8b9927 -> Assistant -> 348e0146-9bb9-495d-b8c4-bde20485181c -> Tool -> 4f1f0651-482e-4cab-a55d-39df9816a94f -> Assistant -> 110fa627-9882-4cc6-8366-bb4269a99851 -> Tool -> d639a724-6245-4c34-ae81-2a1a7a238b1a -> Assistant -> 4cf1eff7-4257-4611-9cf2-67a51ee45ace -> Tool -> 5eb515b5-5e93-4d99-834e-48d5bdd44983 -> Assistant -> 511015e7-9298-47ab-9ff5-7b4680d8c3b2 -> Tool -> 6723818c-93de-443d-a2f6-d6bfd8afa36c -> Assistant -> da42d6fe-6dce-43fc-b5f8-62fb0b35c208 -> Tool -> Since asyncio.run() cannot be used in a running event loop in Jupyter, let's use an alternative approach. -> 54a98b97-4922-4d68-8ae4-e9584ea09e6b -> Assistant -> 87411147-3dd5-4582-8c6a-add4383fa5bb -> Tool -> Using a workaround to run the coroutine in Jupyter's event loop -> 3b2bc534-700d-47ba-aaf4-250dc661f51c -> Assistant -> f28cbdcb-4a95-48b7-aaec-cda14ed29d51 -> Tool -> Using a different approach to run the coroutine -> b7444827-1589-40ed-9b7d-d354f4017eb0 -> Assistant -> aaa2689e-1607-47a1-a47d-7e6ad32fb153 -> User -> d450e6ea-f0dd-4313-94f0-827fa9f7657d -> Assistant -> 465f6944-627a-48d3-bfae-0dcb6d2aebf9 -> Tool -> Debugging by printing the HTML content to identify the correct selectors -> 4c1726e1-b488-410f-867e-06d454a86542 -> Assistant -> aaa23726-4c08-490a-8f7c-e3d61f566227 -> User -> 50a3fc8b-afb9-4d7f-9edd-08d4a412e714 -> Assistant -> 756f1981-acbf-4346-82eb-03d3242d8e40 -> Tool -> Fetching the full HTML content for debugging -> Trying to find the correct CSS selector for the list of parsers -> eda2332a-e66f-48a0-a9e3-69bef1422749 -> Assistant -> 69ec6047-394f-4c35-8602-b9c197c0e2fd -> Tool -> 21e855ac-29bc-459d-97d6-68b68fc3c153 -> Assistant -> 19441444-1394-4817-826b-99ca25512fe7 -> Assistant -> a9cb60a9-71dc-45c2-91d3-fdc65f710ea1 -> Tool -> Debugging by printing a smaller snippet of the HTML content to identify the correct selectors
---
# Debugging by printing a smaller snippet of the HTML content to identify the correct selectors
print(full_html_content[5000:5500])  # Printing a smaller snippet from the middle of the HTML content
== Output ==
<li><a href="https://github.com/returntocorp/ocaml-tree-sitter-core">OCaml</a></li>                                    
                                                                                      <li><a href="https://metacpan.org/
pod/Text::Treesitter">Perl</a></li>                                                                                     
                                     <li><a href="https://github.com/tree-sitter/py-tree-sitter">Python</a></li>        
                                                                                                                  <li><a
 href="https://github.com/tree-sitter/ruby-tree-sitter">Ruby</a></li>                                                   
                                                                       <li><a href="https://github.com/calicoday/ruby-tr
ee-sitter-ffi">Ruby</a></li>                                                                                            
                              <li><a href="https://github.com/tree-sitter/tree-sitter/tree/master/lib/binding_rust">Rust
</a></li>                                                                                                               
           <li


[child ⬇️](#bb8f0eeb-ab2c-4069-8ac1-1b9a1f148b0a)

---

(main branch ⎇)
###### bb8f0eeb-ab2c-4069-8ac1-1b9a1f148b0a
[parent ⬆️](#a9cb60a9-71dc-45c2-91d3-fdc65f710ea1)
