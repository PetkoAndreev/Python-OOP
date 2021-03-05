from category import Category
from document import Document
from storage import Storage
from topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
# print(storage.categories)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
'''
Output
Category 1: work
Topic 1: daily tasks in C:\work_documents
Document 1: finilize project; category 1, topic 1, tags: urgent, work
Document 1: finilize project; category 1, topic 1, tags: urgent, work
'''
