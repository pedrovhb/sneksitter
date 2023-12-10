---
file: /home/pedro/Documents/chatgpt_export/Markdown/Python Library `Textual` Main Concepts.md
heading_stack: <root> -> 5f9f7096-bb2a-4704-aca4-c9546814e0eb -> System -> df2de6ab-21ee-4e3f-b909-f71f777a24ea -> System -> aaa27974-0b91-4f43-9df7-ce0becad2ca1 -> User -> d02ff3d0-30f7-4850-a678-71286ddcfdc0 -> Assistant -> 06cd88dc-5bff-4a6f-8946-50e2a437c6ca -> Tool -> bbb4f456-4257-4ba0-8840-4f069aad6191 -> Assistant -> 1e6a5e45-4d2b-4580-b5d7-e5a3df2697bc -> Tool -> 33893889-6709-4b19-b299-9e344dddd296 -> Assistant -> 0948fa3d-6ea6-458b-9d53-a401f23ba83d -> Tool
---
# Tool

```python
【21†Textual†github.com】 is a Python package used to create cross-platform Text User Interfaces (TUI). This may sound like you’ll be creating a user interface with ASCII-art, but that is not the case.

Textual is quite advanced and allows you to add widgets to your terminal applications, including buttons, context switchers, scroll bars, checkboxes, inputs and more.

## Getting Started

The first thing you need to do is install Textual. If you only want to run Textual applications, then the following pip comand is all you need:

    python3 -m pip install textual

However, if you want to write your own Textual applications, you should run this command instead:

    python3 -m pip install "textual[dev]"

That funny little [dev] part will install some extra dependencies that make developing Textual applications easier.

## Run the Textual Demo

The Textual package comes with a demo. You’ll find the demo is a great way to see what types of things you can do with Textual.

Here’s how you can run the demo:

    python3 -m textual

When you run the command above in your terminal, you should see something like the following appears:

[Image: Textual Demo App]

You can explore Textual in the demo and see the following features:

  * Widgets
  * Accelerators (i.e. CTRL+C)
  * CSS styling
  * and more

## Creating Your Own Simple Application

While the demo is a great place to start to get a feel for what you can do with Textual, it’s always better to dive into the docs and start writing some real code.

You will understand how things work much quicker if you write the code yourself and then start changing the code piece by piece. By going through this iterative process, you’ll learn how to build a little at a time and you’ll have a series of small failures and successes, which is a great way to build up your confidence as you learn.

The first step to take when creating a Textual application is to import Textual and subclass the App() class. When you subclass App(), you create a Textual application. The App() class contains all the little bits and bobs you need to create your very own terminal application.

To start off, create a new Python file in your favorite text editor or IDE and name it hello_textual.py.

Next, enter the following code into your new file:

    from textual.app import App

    class HelloWorld(App):
        ...

    if __name__ == "__main__":
        app = HelloWorld()
        app.run()

When you go to run your terminal application, you should run it in a terminal. Some IDEs have a terminal built-in, such as VS Code and PyCharm. Textual may or may not look correct in those terminals though.

Whenever possible, it is recommended that you run Textual applications in your external terminal. Your applications will look and behave better there most of the time. On Mac, it is recommended that you use iTerm rather than the built-in terminal as the built-in Terminal application hasn’t been updated in quite some time.

To run your new terminal application, you will need to run the following command:

    python3 hello_textual.py

When you run this command, you will see the following:

[Image: Hello Textual]

Oops! That’s kind of like creating a blank black box! That’s probably not what you want after all.

To exit a Textual application, press CTRL+C. When you do, you will exit the application and return to the normal terminal.

That was exciting, but the user interface was very plain. You can fix that up a bit by adding a label in the next section!

## Adding a Label

Now that you are back to your original terminal, go back to your Python editor and create a new file. This time you will name it hello_textual2.py.

Enter the following code into your new Python file:

    from textual.app import App, ComposeResult
    from textual.widgets import Label

    class HelloWorld(App):

        def compose(self) -> ComposeResult:
            yield Label("Hello Textual")

    if __name__ == "__main__":
        app = HelloWorld()
        app.run()

Your HelloWorld() class was empty before. Now you added a compose() method. The compose() method is where you normally setup your widgets.

A widget is a user interface element, such as a label, a text box, or a button. In this example, you add a Label() with the text “Hello World” in it.

Try running your new code in your terminal and you should see something like this:

[Image: Hello Textual with label]

Well, that looks a little better than the original. But it would be nice to have a way to close your application without using CTRL+C.

One common way to close an application is with a Close button. You’ll learn how to add one of those next!

## Adding a Close Button

When you create a user interface, you want to communicate with the user about how they can close your application. A terminal application already has a way to close the terminal itself by way of its exit button.

However, you usually want a way to close your Textual application without closing the terminal itself. You have been using CTRL+C for this.

But there’s a better way! You can add a Button widget and connect an event handler to it to close the function.
```

[child ⬇️](#e60dd7e1-9292-46ef-acbe-1c514feb690e)

---

(main branch ⎇)
###### e60dd7e1-9292-46ef-acbe-1c514feb690e
[parent ⬆️](#0948fa3d-6ea6-458b-9d53-a401f23ba83d)
