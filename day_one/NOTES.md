### What is token?
> Tokens are the smallest unit of text that LLM processes. It is not always true that the smallest unit would be a word and it depends on the type of tokenizer used. For instance for a character level tokenizer the smallest unit would be characters (a, b, c, d etc).

### Why tokens?
> 

**Characters are too granular**: If LLM reads letter-by-letter, it would take forever to "understand" a paragraph. 

**Words are too infinite**: There are millions of words, plus slang, typos, and new terms (like "rizz"). If every word was a unique token, the model's "dictionary" (vocabulary) would be too massive to manage.

**The "Goldilocks" Zone**: Sub-word tokenization allows the model to understand that "smart," "smarter," and "smartest" all share the root "smart." This helps it handle words it has never seen before by breaking them into familiar pieces.

In conclusion, tokenization is used for balancing efficiency and vocabulary size.

**How do they work?**

There are three main steps:

1. Tokenization: 
>The raw text is fed into a Tokenizer. This is a fixed algorithm (like Byte Pair Encoding or BPE) that slices the string into the most efficient pieces based on a pre-defined vocabulary
2. Numerical Mapping:
> Computers can't calculate "apple" + "orange." Every token is assigned a specific ID number.\
Example: > "Hello" $\rightarrow$ 15496" world" $\rightarrow$ 995
3. Vectorization:
> Each token id is then converted into an embedding. This is a high-dimensional vector (a long list of numbers) that represents the "meaning" of the token.If we imagine this in a simplified 3D space, the vector for "King" would be physically close to the vector for "Queen," and "Apple" would be far away near "Fruit."$$V_{king} - V_{man} + V_{woman} \approx V_{queen}$$


**Q. Why output token cost is expensive then input token cost?** 
> The LLMs are heavily inspired from the transformer architecture. The LLMs when they take input as tokens they can process it parallely and there is also technique called KV cache which allows the LLMs to store the attention values and hence the resource used is efficient. But while generating output tokens they must do it sequentially/. Also let's say LLM is generating paragraph of 100 words then for predicting the 87th word it must process previous 1st word to 86th word. Hence generating output token has lots of overhead tasks and uses the resources extensively.