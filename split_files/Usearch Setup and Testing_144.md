---
file: /home/pedro/Documents/chatgpt_export/Markdown/Usearch Setup and Testing.md
heading_stack: <root> -> 736a6f35-0c3a-4def-8e5f-fb433283b0a3 -> System -> 7e1fc11a-385d-4641-83a5-24bcd0f772a6 -> System -> aaa28f28-7a3d-4adc-9c31-2e24b825ee2c -> User -> 431e417f-ba17-4c71-8651-4bb4fc005b8a -> Assistant -> 5efa9536-227a-4097-a943-8a062fa36ebb -> Tool -> 0125b662-4281-4b16-a7df-c31bce9c8ddd -> Assistant -> bbb603db-a333-4ce8-90a2-a060fe0913fe -> Tool -> e359e771-2ded-442d-84dd-9197c84f3a10 -> Assistant -> 52917e86-ff86-4af7-b631-331103ecd0ba -> Tool -> faa2d1e3-8ba1-40f7-bb9b-0529d8b66d9b -> Assistant -> eedb56d6-43ee-4b2a-bab7-b0a66cd5e743 -> Tool -> ede47510-19d2-4507-9e28-e101779dfc56 -> Assistant -> d36982cb-1dff-408e-a3e2-7ebbd9651f28 -> Tool -> 80c4522b-cbf5-44a7-a234-be8818417cee -> Assistant -> f9a4c4b4-dd9b-4aa5-a44d-8261813f74eb -> Tool -> 3d31e99b-d204-492b-bb21-a15ae70e39e5 -> Assistant -> ffe7ec2c-9ab9-41fd-af79-b5dbd8ab21d2 -> Tool -> 2d62042c-555a-4768-ad75-ac8471355ad9 -> Assistant -> aaa2efa5-1015-45f4-a14e-2ac9de41f9d3 -> User -> 27e9ad5a-5943-4b9a-8d53-57be00420983 -> Assistant -> efdfb750-f062-49f0-a748-0aaef6133343 -> Tool -> e64111fc-6337-49bf-9f28-90254d2d75a8 -> Assistant -> d9e1ada1-bceb-4e5a-adc2-f07012d9ddb2 -> Tool -> 270ee728-6db3-4efc-8743-9a1a75e88d1f -> Assistant -> eb022945-6bb7-497e-9288-7da0524271db -> Tool -> 07220b62-5840-461e-8dd2-094eb7b9ea9b -> Assistant -> 6af2f9ba-7e0c-41aa-bedb-a036a7ab2661 -> Tool -> 2b495532-8842-4d73-a1cd-7760c923cc4b -> Assistant -> aaa24e6b-073d-4378-aaa3-3b15770b7e04 -> User -> 4eb099d5-5320-4026-946d-3a316d081126 -> Assistant -> a5404c36-a23d-4d08-9288-5f367fa2af06 -> Tool -> Sample sentences with some similar and some different meanings -> Generate embeddings for the sample sentences -> Initialize a usearch index for the embeddings -> Add embeddings to the index -> Verify the index -> 1263b678-1c92-4fc2-a12f-55c3ec158473 -> Assistant -> 04cdd239-af78-40f6-b6fd-ab0e6e12f49d -> Tool -> Function to search for similar sentences -> Test the function with a query -> 59921e28-a359-43a8-9774-f7aed1c23927 -> Assistant -> aaa2ae00-752f-43a8-b40c-eb5a28503319 -> User -> c815a18a-ff6b-4013-9d73-1974a7e7f5e0 -> Assistant -> Features of a Robust Semantic Search Library -> Core Features -> Metadata Handling -> Interface -> Miscellaneous/Utility Functions -> Abstractions -> User-Friendly Design -> aaa258af-22d7-48e5-afd0-8ab0b857e61c -> User -> 98be4f3e-f01d-49f8-876d-b88c7ae4defb -> Assistant -> CLI Tool Design: SemanticSearchCLI -> Core Features -> Metadata Handling -> Interface -> Miscellaneous/Utility Functions -> Abstractions -> Example Commands -> User-Friendly Design -> aaa219da-7adc-4fd8-9b9f-9f6167516c14 -> User -> 5112851c-7493-4339-a32c-d61ad55e4011 -> Assistant -> aaa26df5-1515-4b4f-b95a-4981c8e682da -> User -> db12bec8-82eb-402b-b389-1ef7bf3ab8ec -> Assistant -> 849f50c2-a40a-4bdd-a6cb-8283af8d1c24 -> Tool -> Installing required packages for logging and rich output -> e3a8f39c-b202-4722-86b9-9e0f2f6095aa -> Assistant -> 42fe0006-c96d-4deb-9050-de02eb3dbc0b -> Tool -> Importing required modules -> 88aed8db-412b-4c77-a068-cd5c61d367c5 -> Assistant -> 6253c7ae-0579-4a2a-907b-48f9e3f4616e -> Tool -> Setting up the logger -> db69a04c-1077-4883-904b-bdba4fee2d82 -> Assistant -> e216c828-2c4e-4988-beb5-d9ddf161a9fc -> Tool -> Implementing the SentenceIndexer class in the 'indexer' module -> 3a4e0da9-c9d2-441c-a388-c31dac156af4 -> Assistant -> d7651b08-61b9-47ed-9738-a2852a618308 -> Tool -> Testing the SentenceIndexer class -> 786c1933-783c-4329-8b9f-d5e41fd90492 -> Assistant -> c2265b5e-2baf-4372-ac47-45d1fca6f383 -> Tool -> Implementing the index_sentences method in SentenceIndexer -> 85a78b4e-d7e0-412a-9e60-b03d75645982 -> Assistant -> 428bdcc5-ba3a-4284-89e1-1df7c2d3bd63 -> Tool -> Correcting the syntax error by adding the method inside the class definition -> 2f3ea362-9927-4d73-b591-7f3ba5c77fcb -> Assistant -> 028ce8df-8a7d-4b98-a45a-7021681bcb52 -> Tool -> Testing the index_sentences method
---
# Testing the index_sentences method
sample_sentences = ['Hello world', 'Semantic search is cool', 'I love Python']
sample_tags = [{'lang': 'en'}, {'lang': 'en'}, {'lang': 'en'}]
indexer.index_sentences(sample_sentences, sample_tags)
== Output ==
```
{ 'ename': 'AttributeError',
  'evalue': "'SentenceIndexer' object has no attribute 'index_sentences'"}
```



[child ⬇️](#88418d33-1f5b-4ad5-9093-d985d1e03d93)

---

(main branch ⎇)
###### 88418d33-1f5b-4ad5-9093-d985d1e03d93
[parent ⬆️](#028ce8df-8a7d-4b98-a45a-7021681bcb52)
