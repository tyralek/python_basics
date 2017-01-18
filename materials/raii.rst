.. raw:: pdf

   PageBreak oneColumn

Resource acquisition is initialization (RAII)
=============================================

WIKI:
RAII is a programming idiom[2] used in several object-oriented languages.
The technique was developed for exception-safe resource management.
In RAII, holding a resource is a class invariant, and is tied to object lifetime: resource allocation (acquisition) is done during object creation (specifically initialization), by the constructor, while resource deallocation (release) is done during object destruction (specifically finalization), by the destructor. Thus the resource is guaranteed to be held between when initialization finishes and finalization starts (holding the resources is a class invariant), and to be held only when the object is alive. Thus if there are no object leaks, there are no resource leaks.


http://effbot.org/zone/python-with-statement.htm
https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

