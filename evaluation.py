import time, gc
import gc

# Activate garbage collector
gc.enable()
memory_start_point = gc.mem_free()

# Record the start time
start_time = time.ticks_us()

# Import the urdflib library
import urdflib as rdflib

# Record the time after importing the library
import_time_tick = time.ticks_us()

# Create a new RDF graph
graph = rdflib.Graph()

# Record the start time
# Add X triples to the graph. Here, I am adding 100 triples
x = 100
datatype = rdflib.URIRef("http://www.w3.org/2001/XMLSchema#string")
base_uri = "http://example.org/"
for i in range(x):
    # Generate unique URIs for subject, predicate, and object
    subject = rdflib.URIRef(base_uri + f"subject{i}")
    predicate = rdflib.URIRef(base_uri + f"predicate{i}")
    obj = rdflib.Literal(f"Object{i}",datatype=datatype)

    # Add the triple to the graph
    graph.add((subject, predicate, obj))

# Record the end time
end_time = time.ticks_us()

# Calculate the time taken to import the library
initial_time = time.ticks_diff(import_time_tick, start_time)
# Calculate the time taken to add triples to the graph
adding_time = time.ticks_diff(end_time, import_time_tick)

# Calculate the memory allocated
memory_end_point = gc.mem_free()
memory_allocated = memory_start_point - memory_end_point

print(f"Graph has {len(graph)} triples")
print(f"Initial time: {initial_time} us")
print(f"Adding time: {adding_time} us")
print(f"Memory allocated: {memory_allocated} bytes")
