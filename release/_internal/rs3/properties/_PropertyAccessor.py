import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
import rs3.generatedFiles.MaterialHydraulicModelService_pb2 as MaterialHydraulicModelService_pb2
import rs3.generatedFiles.MaterialHydraulicModelService_pb2_grpc as MaterialHydraulicModelService_pb2_grpc

class PropertyAccessor:
    def __init__(self, client : Client, objectId : str, stub):
        self.objectId = objectId
        self._client = client
        self._stub = stub
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = CommonMessages_pb2.GetPropertyRequest(objectId=self.objectId, propertyName=propertyName)
        response : CommonMessages_pb2.GetPropertyResponse = self._client.callFunction(self._stub.GetProperty, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = CommonMessages_pb2.SetPropertyRequest(objectId=self.objectId, 
                                                        propertyName=propertyName,
                                                        value=value)
        self._client.callFunction(self._stub.SetProperty, request)

    def getDoubleProperty(self, propertyName : str) -> float:
        return self._getProperty(propertyName).doubleValue

    def setDoubleProperty(self, propertyName : str, value : float):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(doubleValue=value))

    def getFloatProperty(self, propertyName : str) -> float:
        return self._getProperty(propertyName).floatValue
    
    def setFloatProperty(self, propertyName : str, value : float):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(floatValue=value))

    def getIntProperty(self, propertyName : str) -> int:
        return self._getProperty(propertyName).intValue
    
    def setIntProperty(self, propertyName : str, value : int):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(intValue=value))

    def getLongProperty(self, propertyName : str) -> int:
        return self._getProperty(propertyName).longValue
    
    def setLongProperty(self, propertyName : str, value : int):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(longValue=value))

    def getUintProperty(self, propertyName: str) -> int:
        return self._getProperty(propertyName).uintValue

    def setUintProperty(self, propertyName: str, value: int):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(uintValue=value))

    def getUlongProperty(self, propertyName: str) -> int:
        return self._getProperty(propertyName).ulongValue

    def setUlongProperty(self, propertyName: str, value: int):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(ulongValue=value))

    def getBoolValue(self, propertyName: str) -> bool:
        return self._getProperty(propertyName).boolValue

    def setBoolValue(self, propertyName: str, value: bool):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(boolValue=value))

    def getStringValue(self, propertyName: str) -> str:
        return self._getProperty(propertyName).stringValue

    def setStringValue(self, propertyName: str, value: str):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(stringValue=value))

    def getBytesValue(self, propertyName: str) -> bytes:
        return self._getProperty(propertyName).bytesValue

    def setBytesValue(self, propertyName: str, value: bytes):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(bytesValue=value))
        
    def getEnumValue(self, propertyName: str, enumType):
        return enumType(self._getProperty(propertyName).enumValue)
    
    def setEnumValue(self, propertyName: str, value: str):
        self._setProperty(propertyName, CommonMessages_pb2.PropertyValue(enumValue=value))
        
    def getVector3DValue(self, propertyName: str) -> tuple[float, float, float]:
        response = self._getProperty(propertyName).vector3DValue
        return (response.x, response.y, response.z)
    
    def setVector3DValue(self, propertyName: str, value: tuple[float, float, float]):
        request = CommonMessages_pb2.PropertyValue(vector3DValue=CommonMessages_pb2.Vector3D(x=value[0], y=value[1], z=value[2]))
        self._setProperty(propertyName, request)    
    
    def getPoint3DValue(self, propertyName: str) -> tuple[float, float, float]:
        response = self._getProperty(propertyName).point3DValue
        return (response.x, response.y, response.z)
    
    def setPoint3DValue(self, propertyName: str, value: tuple[float, float, float]):
        request = CommonMessages_pb2.PropertyValue(point3DValue=CommonMessages_pb2.Point3D(x=value[0], y=value[1], z=value[2]))
        self._setProperty(propertyName, request)
        
class CustomHydraulicModelPropertyAccessor(PropertyAccessor):
    def __init__(self, client : Client, objectId : str, projectId : str):
        self._stub = MaterialHydraulicModelService_pb2_grpc.MaterialHydraulicModelServiceStub(client.channel)
        super().__init__(client, objectId, self._stub)
        self._projectId = projectId        
        
    def _getProperty(self, propertyName : str) -> CommonMessages_pb2.PropertyValue:
        request = MaterialHydraulicModelService_pb2.GetCustomHydraulicModelPropertyRequest(objectId=self.objectId, projectId=self._projectId, propertyName=propertyName)
        response : MaterialHydraulicModelService_pb2.GetCustomHydraulicModelPropertyResponse = self._client.callFunction(self._stub.GetCustomHydraulicModelProperty, request)
        return response.value
    
    def _setProperty(self, propertyName : str, value : CommonMessages_pb2.PropertyValue):
        request = MaterialHydraulicModelService_pb2.SetCustomHydraulicModelPropertyRequest(objectId=self.objectId, projectId=self._projectId, propertyName=propertyName, value=value)
        self._client.callFunction(self._stub.SetCustomHydraulicModelProperty, request)
