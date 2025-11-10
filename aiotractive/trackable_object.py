from .data_object import DataObject


class TrackableObject(DataObject):
    async def details(self):
        return await self._api.request(f"trackable_object/{self._id}")

    async def health_overview(self):
        """Get health overview of the pet."""
        return await self._api.request(f"pet/{self._id}/health/overview", aps_api=True)
