import rs3.generatedFiles.MaterialDataService_pb2_grpc as MaterialDataService_pb2_grpc
import rs3.generatedFiles.CommonMessages_pb2 as CommonMessages_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3._proxyObject import _ProxyObject
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3.properties.material.initialConditions.InitialConditions import InitialConditions
from rs3.properties.material.constitutiveModel.ConstitutiveModel import ConstitutiveModel
from rs3.properties.material.hydraulic.Hydraulic import Hydraulic
from rs3.properties.material.datum.Datum import Datum
from rs3.properties.material.stageFactors.StageFactors import StageFactors
from rs3.ColorPicker import ColorPicker

class MaterialProperty(_ProxyObject):
    """
    Define material properties.
    
    Attributes:
        Standard (Standard): Reference object for modifying property.
        Geosynthetic (Geosynthetic): Reference object for modifying property.
        ReinforcedConcrete (ReinforcedConcrete): Reference object for modifying property.
    
    Examples:
    - :ref:`material_initial_conditions_example`.
    - :ref:`material_constitutive_models_example`.
    - :ref:`material_hydraulic_example`.
    - :ref:`material_datum_example`.
    - :ref:`material_stage_factors_example`.
    """
    def __init__(self, client : Client, materialID : str):
        super().__init__(client, materialID)
        self._materialDataService = MaterialDataService_pb2_grpc.MaterialDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, materialID, self._materialDataService)
        self.InitialConditions = InitialConditions(client, materialID)
        self.ConstitutiveModel = ConstitutiveModel(client, materialID)
        self.Hydraulic = Hydraulic(client, materialID)
        self.Datum = Datum(client, materialID)
        self.StageFactors = StageFactors(client, materialID)

    def getMaterialName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")
    def setMaterialName(self, name):
        self._propertyAccessor.setStringValue("Name", name)
    def setMaterialColor(self, *args):
        """
        Sets the RGBA color for the object.

        Raises:
            ValueError: If inputs are invalid or out of range.
            
        Notes:
            Accepted formats:
                - setColor(red, green, blue)
                - setColor(red, green, blue, alpha)
                - setColor("#RRGGBB")
                - setColor("#RRGGBBAA")
                - setColor(ColorType.Rose)
                - setColor(0xE1E4FF)  # Integer COLORREF

        """
        color_bytes = ColorPicker._setColorValidation(*args)
        request = CommonMessages_pb2.SetColorRequest(objectId=self._objectId, value=color_bytes)
        self._client.callFunction(self._materialDataService.SetColorProperty, request)
    def getMaterialColor(self) -> tuple[int, int, int, int]:
        """
        Retrieves the RGBA color of the object.

        Returns:
            tuple[int, int, int, int]: A tuple of four integers representing the red, green, blue, and alpha components of the object's color, each in the range [0, 255].
        """
        request = CommonMessages_pb2.GetColorRequest(objectId=self._objectId)
        response : CommonMessages_pb2.GetColorResponse = self._client.callFunction(self._materialDataService.GetColorProperty, request)
        red, green, blue, alpha = response.value
        return red, green, blue, alpha