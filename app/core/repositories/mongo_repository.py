from typing import Union

import bson
from beanie import Document, PydanticObjectId, WriteRules

from app.core.repositories.base_repository import BaseRepository


class MongoRepository(BaseRepository):
    collection: Document = None

    async def create(self, entity: Document, rules: WriteRules = WriteRules.WRITE):
        """
               Create a new document in the collection.

               Args:
                   entity (Document): The document to create.

               Returns:
                   The created document.
               """
        obj = await entity.save(link_rule=rules)
        return obj

    async def findall(self, limit: int = 1000, offset: int = None) -> list[Document]:
        """
               Find all documents in the collection.

               Args:
                   limit (int): The maximum number of documents to return.
                   offset (int): The number of documents to skip.

               Returns:
                   List of documents found.
               """
        objects = await self.collection.all(limit=limit, skip=offset).to_list()
        return objects

    async def find_by_id(self, id_: PydanticObjectId):
        """
                Find a document by its ID.

                Args:
                    id_ (PydanticObjectId): The ID of the document to find.

                Returns:
                    The found document or None if not found.
                """
        obj = await self.collection.get(id_)
        if obj:
            return obj

    async def update(self, id_: PydanticObjectId, data: dict) -> Union[bool, Document]:
        """
                Update a document in the collection by its ID.

                Args:
                    id_ (PydanticObjectId): The ID of the document to update.
                    update (dict): The update to apply.

                Returns:
                    The updated document.
                """
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {field: value for field, value in des_body.items()}}
        obj = await self.collection.get(id_)
        if obj:
            await obj.update(update_query)
            return obj
        return False

    async def delete_by_id(self, id_: PydanticObjectId) -> bool:
        """
               Delete a document in the collection by its ID.

               Args:
                   id_ (PydanticObjectId): The ID of the document to delete.

               Returns:
                   The deleted document.
               """
        obj = await self.collection.get(id_)
        if obj:
            await obj.delete()
            return True
        return False
