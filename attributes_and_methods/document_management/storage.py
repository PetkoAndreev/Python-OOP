class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        # __repr__() – returns a string representation of each document on separate lines
        result = ''
        for document in self.documents:
            result += f"{document.__repr__()}\n"
        return result

    def get_category_inst(self, category_id):
        category = [category for category in self.categories if category.id == category_id][0]
        return category

    def get_topic_inst(self, topic_id):
        topic = [topic for topic in self.topics if topic.id == topic_id][0]
        return topic

    def get_document_inst(self, document_id):
        document = [document for document in self.documents if document.id == document_id][0]
        return document

    def add_category(self, category):
        # category = [category for category in self.categories]
        # add_category(category:Category) – add the category if it does not exist
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        # add_topic(topic:Topic) – add the topic if it does not exist
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        # add_document(document:Document) – add the document if it does not exist
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        # edit_category(category_id: int, new_name:str) – edit the name of the category with the provided id
        category = self.get_category_inst(category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        # edit_topic(topic_id: int, new_topic: str, new_storage_folder: str) – edit the topic with the given id
        topic = self.get_topic_inst(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        # edit_document(document_id: int, new_file_name: str) – edit the document with the given id
        document = self.get_document_inst(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        # delete_category(category_id) – delete the category with the provided id
        category = self.get_category_inst(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        # delete_topic(topic_id) – delete the topic with the provided id
        topic = self.get_topic_inst(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        # delete_document(document_id) – delete the document with the provided id
        document = self.get_document_inst(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        # get_document(document_id) – return the document with the provided id
        document = self.get_document_inst(document_id)
        return document.__repr__()
