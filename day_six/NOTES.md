Q1. What is stratified sampling?
> Strata means a group i.e homogenous. Sampling simply means selecting a subset (sample) from a larger group (usually called population). Stratified sampling means selecting a sample from these stratas. In this sampling:
1. We first divide a larger heteregonous group into smaller homogenous groups.
2. Then, we randomly sample from each strata.

**Why stratified sampling?**
> It makes sure that each groups are represented well in train, val and test set.

Q2. Is internet search a RAG?
> I think internet search cannot be termed as RAG but it comes a whole new umberall term called "context engineering" (which RAG can also be part of). Since most of the internet search is basically surfing through internet to create a context that can be used by the LLM for any downstream tasks.

Q3. Is uploading a file to the ChatGPT a RAG or not?
> Current version of ChatGPT product uses a tool called `file_search` tool.

Exposed interface
```
Tool name: file_search.msearch

Purpose: search over user-uploaded documents

Core input field: queries (list of search queries)

Constraint: 1–5 queries

Optional field: time_frame_filter

start_date

end_date

Output: relevant document text chunks used for answering
```

 So if the user uploads the file, then a proper RAG workflow is initiated. Hence, uploading the file and asking QA with ChatGPT is obviously RAG.
While it is necessary to mention that it may not always invoke the tool depending on the context of information it initially loads in its window the first time user uploads the document file.

[My short interaction with ChatGPT](https://chatgpt.com/share/6981a619-9860-8000-a7ed-4f37c85d8b30)
[Report Created by Grok on my conversation](day_six/grok_report_on_chatgpt.pdf)