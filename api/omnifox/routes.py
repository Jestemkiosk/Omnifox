from omnifox import api
import omnifox.models as models

api.add_resource(models.Foxes, '/foxes/')
api.add_resource(models.Fox, '/foxes/<int:id>')
api.add_resource(models.Cities, '/cities/')
api.add_resource(models.City, '/cities/<int:id>')
api.add_resource(models.HomePage, '/')