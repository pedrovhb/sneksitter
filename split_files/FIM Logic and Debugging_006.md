---
file: /home/pedro/Documents/chatgpt_export/Markdown/FIM Logic and Debugging.md
heading_stack: <root> -> ccfb9a26-4159-40fe-b34e-021fbc2c3255 -> System -> ec3e3103-d827-4adc-88e3-b58200f32ea1 -> System -> aaa24904-7ec6-4e44-875c-31e21b7e874c -> User
---
# User

Please check out this code and the resulting code generation:

import os
import textwrap

from rich import get_console
from rich.live import Live
from rich.syntax import Syntax

os.environ["LLAMA_CPP_LIB"] = (
    os.environ.get("LLAMA_CPP_LIB")
    or "/nix/store/xbyfr7gnzm5z3wig7wvy5g62igwvnizp-llama.cpp/lib/libllama.so"
)
llama_model = (
    os.environ.get("LLAMA_MODEL")
    or "/home/pedro/dockerx/llama_attempt/llama.cpp/models/codellama-13b-instruct.Q4_K_M.gguf"
)
import llama_cpp


def build_fim_prompt(prompt_before: str, prompt_after: str) -> str:
    """Builds a special prompt for the Fill-in-the-Middle task.

    As per the paper, the prompt is built as follows:
        <PRE> <prompt_before> <SUF> <prompt_after> <MID> <... (generated text)> <EOT>
    """
    fim_prefix = "<PRE>"
    fim_middle = "<MID>"
    fim_suffix = "<SUF>"
    # fim_eot = "<EOT>"  # Not used in this example
    prompt_before, prompt_after = prompt_before.strip(), prompt_after.strip()
    return f"{fim_prefix} {prompt_before} {fim_suffix} {prompt_after} {fim_middle}".strip()


def as_fim_prompt(prompt: str, dedent: bool = False) -> str:
    """Converts a regular prompt to a Fill-in-the-Middle prompt by splitting at the location of the <MID> token.

    Example:
        >>> as_fim_prompt("This is a test of the <MID> system.")
        '<PRE> This is a test of the <SUF> system. <MID>'
    """
    if dedent:
        prompt = textwrap.dedent(prompt)
    return build_fim_prompt(*prompt.split("<MID>"))


def main() -> None:
    llm = llama_cpp.Llama(
        model_path=llama_model,
        n_gpu_layers=50,
        logits_all=False,
        verbose=False,
        n_batch=128,
    )

    prompt = """
    [INST]Write a type-annotated function which merges any number of asynchronous iterators, yielding values from each as soon as they are available, and finishing when all iterators are exhausted.[/INST]
    ```
    <MID>
    
        async def _result_iterator() -> AsyncIterator[T]:
            while True:
                item = await _queue.get()
                if item is _sentinel:
                    num_finished += 1
                    if num_finished == num_iterators:
                        return
                else:
                    yield item
                    
        return _result_iterator()
    ```
    [INST]Test the merge function.[/INST]
    ```
    async def arange(start: int, stop: int, step: int = 1, delay: float=0.1) -> AsyncIterator[int]:
        for i in range(start, stop, step):
            await asyncio.sleep(delay)
            yield i
        
    async def main() -> None:
        values = []
        aranges = (
            arange(0, 10, 1, delay=0.2),
            arange(10, 20, 2, delay=0.35),
            arange(100, 103, 3, delay=0.5),
        )
        async for i in merge(*aranges):
            print(i)
            values.append(i)
        
        print(values)
            
    asyncio.run(main())
    ```
    """

    con = get_console()
    fim_prompt = as_fim_prompt(prompt, dedent=True)
    prefix, suffix = textwrap.dedent(prompt).split("<MID>")
    generated_text = []

    syntax = Syntax(prefix + suffix, lexer="python", theme="monokai", line_numbers=True)
    with Live(renderable=syntax, console=con, auto_refresh=False, transient=True) as live:
        for token in llm(
            prompt=fim_prompt,
            stream=True,
            temperature=0,
            max_tokens=1024,
        ):
            generated_text.append(token["choices"][0]["text"])
            syntax.code = prefix + "".join(generated_text) + suffix
            live.update(syntax, refresh=True)

    syntax.line_numbers = False
    con.print(syntax)  # Print the final result without line numbers


if __name__ == "__main__":
    main()

---

Output result:

[INST]Write a type-annotated function which merges any number of asynchronous iterators, yielding values from each as
```

import asyncio
from typing import AsyncIterator, Generic, TypeVar

T = TypeVar('T')

async def merge(*iterators: AsyncIterator[T]) -> AsyncIterator[T]:
    num_iterators = len(iterators)
    _sentinel = object()
    _queue = asyncio.Queue()
    num_finished = 0

    async def _enqueue_iterator(iterator: AsyncIterator[T]) -> None:
        try:
            while True:
                item = await iterator.__anext__()
                await _queue.put(item)
        except StopAsyncIteration:
            await _queue.put(_sentinel)

    for iterator in iterators:


    async def _result_iterator() -> AsyncIterator[T]:
        while True:
            item = await _queue.get()
            if item is _sentinel:
                num_finished += 1
                if num_finished == num_iterators:
                    return
            else:
                yield item

    return _result_iterator()
```
[INST]Test the merge function.[/INST]
```
async def arange(start: int, stop: int, step: int = 1, delay: float=0.1) -> AsyncIterator[int]:
    for i in range(start, stop, step):
        await asyncio.sleep(delay)
        yield i

async def main() -> None:
    values = []
    aranges = (
        arange(0, 10, 1, delay=0.2),
        arange(10, 20, 2, delay=0.35),
        arange(100, 103, 3, delay=0.5),
    )
    async for i in merge(*aranges):
        print(i)
        values.append(i)

    print(values)

asyncio.run(main())
```

---

We can see the produced code is actually quite close to nailing it, but it stops short of one line to complete the function. Are there any logic issues in the FIM calculation that explain this?

[child ⬇️](#3e42be5a-97b3-4ca4-9124-2ca3d4c32e56)

---

(main branch ⎇)
###### 3e42be5a-97b3-4ca4-9124-2ca3d4c32e56
[parent ⬆️](#aaa24904-7ec6-4e44-875c-31e21b7e874c)
