---
file: /home/pedro/Documents/chatgpt_export/Markdown/Notebook Job Data Retrieval.md
heading_stack: <root> -> e6fe1ab6-f1c0-4388-a8e7-1c3d0315466e -> System -> 24b915fb-e8ff-4102-a875-7f7ea2e2a439 -> System -> aaa2b941-2299-4711-b7fd-52b2da380ed6 -> User -> 6b4fac93-b94a-4f43-82b6-a7a4868044f3 -> Assistant -> c63832c2-df1d-4483-aa9f-ab7e910c8f16 -> Tool -> generated by datamodel-codegen: -> filename:  hn_jobs.json -> timestamp: 2023-09-25T20:22:55+00:00 -> 7b502702-4ce6-40b4-a0ef-439d804f78d0 -> Assistant -> aaa2543c-cd16-4a49-a6dd-36e85c82c60d -> User -> e4e1553a-f7a4-423f-9b5e-134aa2af861c -> Assistant -> 1ca395da-d1b3-4508-8161-5abf783be70e -> Tool -> generated by datamodel-codegen: -> filename:  hn_jobs.json -> timestamp: 2023-09-25T20:22:55+00:00 -> Show a random company -> 5d3bf0ba-b6ce-43f7-a5ca-3fb27a031604 -> Assistant -> aaa20425-66a2-4835-8049-deec7f8467e5 -> User -> 8b440c17-4bdf-495b-b2ae-dc5e8dd7d533 -> Assistant -> 9109e1e2-41f1-493c-b9fa-e314ed35a8ff -> Tool -> generated by datamodel-codegen: -> filename:  hn_jobs.json -> timestamp: 2023-09-25T20:22:55+00:00 -> Show a random company -> 4e987c7e-6f39-476e-ad69-a6cf0713e1ed -> Assistant -> aaa27db9-6747-43da-8090-16c8aa422c6e -> User -> b15cc185-bd79-4692-9c5e-7a893c810569 -> Assistant -> 97ca0ab7-bc48-4897-9931-1d973fd70e02 -> Tool -> generated by datamodel-codegen: -> filename:  hn_jobs.json -> timestamp: 2023-09-25T20:22:55+00:00 -> Show a random company -> 5eff3979-8823-494c-9df9-cb5f88db426e -> Assistant -> 150d31f9-c649-4cb9-a257-f43b09a2e0b8 -> Tool -> Information Related to Job Openings -> 43f9b0f0-a070-41d9-9d64-5204f759d079 -> Assistant -> aaa28917-1835-4887-87e5-a45617870c70 -> User -> debbc83c-7055-4385-96af-f7224ba79aef -> Assistant -> 4eda622a-65b1-480f-9651-9bbbf2b5f8a2 -> Tool -> generated by datamodel-codegen: -> filename:  hn_jobs.json -> timestamp: 2023-09-25T20:22:55+00:00 -> Show a random company -> 68de6d01-cbe5-4879-9966-232d424cb1ba -> Assistant -> Libraries and Dependencies -> Data Models -> Data Loading and Exploration -> Implications for Job Information -> aaa25948-9b55-407b-957a-0bd78c7c540a -> User -> 5c5f38a7-c338-4e86-9ad0-6802bcb95b45 -> Assistant -> 7dab6743-33b2-4682-a9b9-148fa4cf7529 -> Tool -> 213f21a3-e385-4ce8-b87a-0a17b0a06f4b -> Assistant -> 32706a9d-6721-4cbc-bc3f-401f478fac8c -> Tool -> a844271b-84f9-4d04-bfa7-eb1540338fb4 -> Assistant -> aaa2c604-f280-4681-9bbc-4b718a353389 -> User -> 3be926cb-907a-4311-a93b-da809579b8c4 -> Assistant -> bdf7c1ad-3e40-4499-b7c0-6113692f75d2 -> Tool -> 35e5c04d-06af-4210-83ae-7a3503ac6831 -> Assistant -> 504028f8-46e1-4510-a5a1-b509a3045521 -> Tool -> Convert the list of companies to a DataFrame for easier manipulation -> Extract the jobs into a separate DataFrame -> 65bdc7c5-fdd3-45a1-ac5a-1b957c3be079 -> Assistant -> 1bf0b844-19b6-4e51-b1e6-a4028b0ca2b0 -> Tool -> Correcting the code to properly extract job details -> 1b9dc564-ea5e-4ce9-a7c1-08d8783b9c4f -> Assistant -> ff4ad0de-f7f7-4af7-bebe-88c0e0969e13 -> Tool -> Visualizing the distribution of job types -> ce225427-6dd5-45e8-93fc-4c6a00f9b4e2 -> Assistant -> 07fc4d6c-4bd3-41b7-b1ba-e8bff7bb95da -> Tool -> Visualizing the distribution of engineering types -> 3a66291e-684a-42b2-bc06-51ffd56a6471 -> Assistant -> 779f9a25-28d5-43dd-9d39-b96154af83f5 -> Tool -> Visualizing the distribution of remote jobs -> 0685561f-9032-4f0a-b1ef-810e5be163c4 -> Assistant -> 785ae135-509e-4c4c-b313-166afa4302d4 -> Tool -> Exploring skills required for jobs -> 8d962fe0-f383-463b-95ee-adadc76ea143 -> Assistant -> 56c45a59-85aa-42b4-91c0-f4757fa7452c -> Tool -> Correcting the code to properly count skills -> 65d12032-031d-4d05-9c46-c2ae4d86a98a -> Assistant -> 6ff17374-c250-4bf7-be9e-a38df8cc837b -> Tool -> Summary of Job Data Exploration -> ad1c335d-f5eb-4d15-a6f3-e1bb50b03fcc -> Assistant -> aaa21995-1639-4eaf-8f7c-4cf3ea649a0d -> User -> 28964f16-9349-4d00-b4e0-73846145d152 -> Assistant -> 82a2f75b-1e20-4b0d-a42d-ccc6f1a931d8 -> Tool -> Filter jobs that are remote, don't require a visa, and list Python as a desired skill
---
# Filter jobs that are remote, don't require a visa, and list Python as a desired skill
filtered_jobs = jobs_df[(jobs_df['remote'] == True) & (jobs_df['visa'] == False) & (jobs_df['skills'].apply(lambda x: any(skill['name'] == 'Python' for skill in x)))]