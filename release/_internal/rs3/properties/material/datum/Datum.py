import rs3.generatedFiles.MaterialDatumService_pb2_grpc as MaterialDatumService_pb2_grpc
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3.properties.material.datum.YoungsModulusDatumDependency import YoungsModulusDatumDependency
from rs3.properties.material.datum.FrictionAngleDatumDependency import FrictionAngleDatumDependency
from rs3.properties.material.datum.CohesionDatumDependency import CohesionDatumDependency
from rs3._proxyObject import _ProxyObject
from ._PropertyAccessor import PropertyAccessor
class Datum(_ProxyObject):
    """
	Examples:
		See :ref:`material_datum_example`.
    """
    def __init__(self, client : Client, materialID : str):
        super().__init__(client, materialID)
        self._stub = MaterialDatumService_pb2_grpc.MaterialDatumServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, materialID, self._stub)
        self.YoungsModulusDatumDependency = YoungsModulusDatumDependency(client, materialID, DatumDependencyIndex.YOUNGS_MODULUS)
        self.FrictionAngleDatumDependency = FrictionAngleDatumDependency(client, materialID, DatumDependencyIndex.FRICTION_ANGLE)
        self.CohesionDatumDependency = CohesionDatumDependency(client, materialID, DatumDependencyIndex.COHESION)
        self.UnloadingYoungsModulusDatumDependency = CohesionDatumDependency(client, materialID, DatumDependencyIndex.UNLOADING_YOUNGS_MODULUS)
        
    