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