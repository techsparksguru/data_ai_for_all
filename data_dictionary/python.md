# Why Python
Why not Python ? We could totally use any other language like Java, Ruby, haskell, Scala etc, but the question would remain if we use those :) Why that ? Python has the largest number of libraries , ecosystem, support for IDEs and active development that makes it attactive for data analysis, science, stats etc. Surely, it is possible to do in Java for e.g. , but we probably have to jump through hoops. In Big Data, Java based frameworks/libraries/tools rule for e.g. hadoop ecosystem runs on JVM's, wrappers are built using Java code fully (Apache Spark), however if the interface to interact with the servers is many - python , scala being the top easiest ones

# Is Python Compiled or Interpreted ?
I wish it was an easy answer ! In good ol' days - probably it was, when there were probably a handful of languages/runtimes like Basic, Cobol, c, c++, java, but no longer. The terms compilers and interpreters are not mutually exclusive, because some of python can be compiled and some interpreted based on execution time. In short, Python is compiled (look at .pyc files that get created, it is bytecode), however the user doesn't explicitly invoke compiler (like java where it has to be compiled before executed). The python interpreter decides "when" to compile. The user's job is only to write python code and execute through one of the many python interpreters.   
ByteCode is actually another layer that a virtual machine executes and converts to actual machine code (the one that CPU & registers understand). In that sense it is similar to JVM (which again is executed by java's vm). Btw, we aint talking about the VMs at the operating system level aka. hypervisors. That is another topic

# Python Interpreters
The most common one that many use is CPython or cython, but otherwise there are many 

- Cpython (implemented and runs on C platform)
- Jython (implemented and runs on jvm)
- Iron Python (implemented and runs on .net framework)
- PyPy
- PythonNet
- Stackless Python

The concept is very similar to Ruby World - cruby/mri ruby, jruby etc.

# Zen of Python

The Zen of Python is a collection of 19 guiding principles penned by Tim Peters in 1999. It was included as entry number 20 in the language’s official Python Enhancement Proposals.

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren’t special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one — and preferably only one — obvious way to do it.
- Although that way may not be obvious at first unless you’re Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it’s a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea — let’s do more of those!
- there is no rule