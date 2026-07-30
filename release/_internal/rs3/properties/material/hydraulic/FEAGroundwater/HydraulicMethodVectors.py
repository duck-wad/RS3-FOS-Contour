from rs3.CommonEnums import *
from rs3._client import Client
from rs3._proxyObject import _ProxyObject
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
import rs3.generatedFiles.MaterialHydraulicDataService_pb2_grpc as MaterialHydraulicDataService_pb2_grpc
import rs3.generatedFiles.MaterialHydraulicDataService_pb2 as MaterialHydraulicDataService_pb2
class HydraulicMethodVectors(_ProxyObject):
    def __init__(self, client: Client, id: str):
        super().__init__(client, id)
        self._stub = MaterialHydraulicDataService_pb2_grpc.MaterialHydraulicDataServiceStub(client.channel)
              
    def setK1DirectionType(self, value : LinearDirectionType):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DirectionType", value=CommonMessages_pb2.PropertyValue(enumValue=value.value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK1DirectionType(self) -> LinearDirectionType:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DirectionType")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return LinearDirectionType(response.value.enumValue)
    
    def setK1Trend(self, value : float):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DegTrend", value=CommonMessages_pb2.PropertyValue(doubleValue=value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK1Trend(self) -> float:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DegTrend")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return response.value.doubleValue
    
    def setK1Plunge(self, value : float):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DegPlunge", value=CommonMessages_pb2.PropertyValue(doubleValue=value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK1Plunge(self) -> float:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="DegPlunge")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return response.value.doubleValue
    
    def setK1Vector(self, value : tuple[float, float, float]):
        """
        Set (x, y, z) of the K1 vector.
        """
        vector = CommonMessages_pb2.Vector3D(x=value[0], y=value[1], z=value[2])
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="Vector", value=CommonMessages_pb2.PropertyValue(vector3DValue=vector))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK1Vector(self) -> tuple[float, float, float]:
        """
        Get (x, y, z) of the K1 vector.
        """
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K1Orientation", propertyName="Vector")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return (response.value.vector3DValue.x, response.value.vector3DValue.y, response.value.vector3DValue.z)
    
    def setK2DirectionType(self, value : LinearDirectionType):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DirectionType", value=CommonMessages_pb2.PropertyValue(enumValue=value.value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK2DirectionType(self) -> LinearDirectionType:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DirectionType")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return LinearDirectionType(response.value.enumValue)
    
    def setK2Trend(self, value : float):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DegTrend", value=CommonMessages_pb2.PropertyValue(doubleValue=value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK2Trend(self) -> float:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DegTrend")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return response.value.doubleValue
    
    def setK2Plunge(self, value : float):
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DegPlunge", value=CommonMessages_pb2.PropertyValue(doubleValue=value))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK2Plunge(self) -> float:
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="DegPlunge")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return response.value.doubleValue
    
    def setK2Vector(self, value : tuple[float, float, float]):
        """
        Set (x, y, z) of the K2 vector.
        """
        vector = CommonMessages_pb2.Vector3D(x=value[0], y=value[1], z=value[2])
        request = MaterialHydraulicDataService_pb2.SetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="Vector", value=CommonMessages_pb2.PropertyValue(vector3DValue=vector))
        self._client.callFunction(self._stub.SetLinearDirection, request)

    def getK2Vector(self) -> tuple[float, float, float]:
        """
        Get (x, y, z) of the K2 vector.
        """
        request = MaterialHydraulicDataService_pb2.GetLinearDirectionRequest(objectId=self._objectId, upperPropertyName="K2Orientation", propertyName="Vector")
        response : MaterialHydraulicDataService_pb2.GetLinearDirectionResponse = self._client.callFunction(self._stub.GetLinearDirection, request)
        return (response.value.vector3DValue.x, response.value.vector3DValue.y, response.value.vector3DValue.z)
    