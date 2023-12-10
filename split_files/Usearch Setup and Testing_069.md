---
file: /home/pedro/Documents/chatgpt_export/Markdown/Usearch Setup and Testing.md
heading_stack: <root> -> 736a6f35-0c3a-4def-8e5f-fb433283b0a3 -> System -> 7e1fc11a-385d-4641-83a5-24bcd0f772a6 -> System -> aaa28f28-7a3d-4adc-9c31-2e24b825ee2c -> User -> 431e417f-ba17-4c71-8651-4bb4fc005b8a -> Assistant -> 5efa9536-227a-4097-a943-8a062fa36ebb -> Tool -> 0125b662-4281-4b16-a7df-c31bce9c8ddd -> Assistant -> bbb603db-a333-4ce8-90a2-a060fe0913fe -> Tool -> e359e771-2ded-442d-84dd-9197c84f3a10 -> Assistant -> 52917e86-ff86-4af7-b631-331103ecd0ba -> Tool -> faa2d1e3-8ba1-40f7-bb9b-0529d8b66d9b -> Assistant -> eedb56d6-43ee-4b2a-bab7-b0a66cd5e743 -> Tool -> ede47510-19d2-4507-9e28-e101779dfc56 -> Assistant -> d36982cb-1dff-408e-a3e2-7ebbd9651f28 -> Tool -> 80c4522b-cbf5-44a7-a234-be8818417cee -> Assistant -> f9a4c4b4-dd9b-4aa5-a44d-8261813f74eb -> Tool -> 3d31e99b-d204-492b-bb21-a15ae70e39e5 -> Assistant -> ffe7ec2c-9ab9-41fd-af79-b5dbd8ab21d2 -> Tool -> 2d62042c-555a-4768-ad75-ac8471355ad9 -> Assistant -> aaa2efa5-1015-45f4-a14e-2ac9de41f9d3 -> User -> 27e9ad5a-5943-4b9a-8d53-57be00420983 -> Assistant -> efdfb750-f062-49f0-a748-0aaef6133343 -> Tool -> e64111fc-6337-49bf-9f28-90254d2d75a8 -> Assistant -> d9e1ada1-bceb-4e5a-adc2-f07012d9ddb2 -> Tool -> 270ee728-6db3-4efc-8743-9a1a75e88d1f -> Assistant -> eb022945-6bb7-497e-9288-7da0524271db -> Tool -> 07220b62-5840-461e-8dd2-094eb7b9ea9b -> Assistant -> 6af2f9ba-7e0c-41aa-bedb-a036a7ab2661 -> Tool -> 2b495532-8842-4d73-a1cd-7760c923cc4b -> Assistant -> aaa24e6b-073d-4378-aaa3-3b15770b7e04 -> User -> 4eb099d5-5320-4026-946d-3a316d081126 -> Assistant -> a5404c36-a23d-4d08-9288-5f367fa2af06 -> Tool -> Sample sentences with some similar and some different meanings -> Generate embeddings for the sample sentences -> Initialize a usearch index for the embeddings -> Add embeddings to the index -> Verify the index -> 1263b678-1c92-4fc2-a12f-55c3ec158473 -> Assistant
---
# Assistant

{
  "file_id": "bd307b66-5e95-434a-9ff2-d2599b457e0c",
  "cell_type": "code",
  "source": [
    "# Function to search for similar sentences",
    "def search_similar_sentences(query_sentence, index, model, sample_sentences, top_n=5):",
    "    query_embedding = model.encode([query_sentence])[0]",
    "    matches = index.search(query_embedding, top_n)",
    "    similar_sentences = [(sample_sentences[match.key], match.distance) for match in matches]",
    "    return similar_sentences",
    "",
    "# Test the function with a query",
    "query = 'I love Python programming'",
    "similar_sentences = search_similar_sentences(query, sentence_index, model, sample_sentences)",
    "similar_sentences"
  ],
  "and_run": true
}

[child ⬇️](#04cdd239-af78-40f6-b6fd-ab0e6e12f49d)

---

(main branch ⎇)
###### 04cdd239-af78-40f6-b6fd-ab0e6e12f49d
[parent ⬆️](#1263b678-1c92-4fc2-a12f-55c3ec158473)
