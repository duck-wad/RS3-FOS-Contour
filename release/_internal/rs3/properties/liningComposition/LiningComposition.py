import rs3.generatedFiles.CompositeLinerDataService_pb2_grpc as CompositeLinerDataService_pb2_grpc
import rs3.generatedFiles.CompositeLinerDataService_pb2 as CompositeLinerDataService_pb2
from rs3._client import Client
from rs3.properties.PropertyEnums import *
from rs3.properties._PropertyAccessor import PropertyAccessor
from rs3._proxyObject import _ProxyObject
from dataclasses import dataclass, field

@dataclass
class CompositeLinerLayer:
    linerName: str = ""
    hasUpperJoint: bool = False
    hasLowerJoint: bool = False
    installationStage: int = 0
    isRemoved: bool = False
    removalStage: int = -1
    upperJointName: str = field(default="")
    lowerJointName: str = field(default="")

    def __post_init__(self):
        self.upperJointName = None if not self.hasUpperJoint else ""
        self.lowerJointName = None if not self.hasLowerJoint else ""
        
    def setLinerByName(self, name):
        self.linerName = name

    def setUpperJoint(self, hasUpperJoint: bool, upperJointName: str = ""):
        self.hasUpperJoint = hasUpperJoint
        self.upperJointName = upperJointName if hasUpperJoint else None

    def setLowerJoint(self, hasLowerJoint: bool, lowerJointName: str = ""):
        self.hasLowerJoint = hasLowerJoint
        self.lowerJointName = lowerJointName if hasLowerJoint else None

    def setInstallationStage(self, installationStage: int):
        self.installationStage = installationStage
    
    def setRemovalStage(self, isRemoved: bool, removalStage: int):
        self.isRemoved = isRemoved
        self.removalStage = removalStage

    def to_tuple(self):
        return (
            self.linerName,
            self.hasUpperJoint,
            self.upperJointName,
            self.hasLowerJoint,
            self.lowerJointName,
            self.installationStage,
            self.isRemoved,
            self.removalStage
        )


class LiningCompositionProperty(_ProxyObject):
    """
    Define the liners and joint interfaces that belong to a lining.
    
    Examples:
        See :ref:`composite_liner_example`.
        
    """
    def __init__(self, client : Client, liningCompositionID : str):
        super().__init__(client, liningCompositionID)
        self._liningCompositionDataService = CompositeLinerDataService_pb2_grpc.CompositeLinerDataServiceStub(self._client.channel)
        self._propertyAccessor = PropertyAccessor(client, liningCompositionID, self._liningCompositionDataService)

    def getCompositeName(self) -> str:
        return self._propertyAccessor.getStringValue("Name")

    def setCompositeName(self, name : str):
        self._propertyAccessor.setStringValue("Name", name)

    def getLayerComposition(self) -> list[CompositeLinerLayer]:
        """
        Retrieves the current composite liner configuration for the object.

        Returns:
            list of CompositeLinerLayer: Each CompositeLinerLayer represents one lining composition layer in the composite liner structure.

            The CompositeLinerLayer contains the following fields:
            
            - linerName (str): Name of the liner.
            - hasUpperJoint (bool): Whether an upper joint is present.
            - upperJointName (str): Name of the upper joint if hasUpperJoint is True. Otherwise, it shows as None.
            - hasLowerJoint (bool): Whether a lower joint is present.
            - lowerJointName (str): Name of the lower joint if hasLowerJoint is True. Otherwise, it shows as None.
            - installationStage (int): The construction stage at which the liner is installed.
            - isRemoved (bool): Whether the liner is removed.
            - removalStage (int): The construction stage at which the liner is removed; should be -1 if never get removed.

        """
        request = CompositeLinerDataService_pb2.GetCompositeLinerRequest(liningId=self._objectId)
        response : CompositeLinerDataService_pb2.GetCompositeLinerResponse = self._client.callFunction(self._liningCompositionDataService.GetCompositeLiner, request)

        layers = []
        for composite in response.compositeLiner:
            layer = CompositeLinerLayer()
            layer.setLinerByName(composite.linerName)
            layer.setUpperJoint(composite.hasUpperJoint, composite.upperJointName if composite.upperJointName != "" else None)
            layer.setLowerJoint(composite.hasLowerJoint, composite.lowerJointName if composite.lowerJointName != "" else None)
            layer.setInstallationStage(composite.installationStage)
            layer.setRemovalStage(composite.isRemoved, composite.removalStage)
            layers.append(layer)

        return layers

    def setLayerComposition(self, value: list[CompositeLinerLayer]):
        """
        Sets or updates the composite liner configuration for the object.

        Args:
            value: A list of CompositeLinerLayer, each CompositeLinerLayer representing a set of liner and interface element(s) in sequence. Each item must contain:
            - linerName (str): Name of the liner.
            - hasUpperJoint (bool): True if an upper joint exists.
            - upperJointName (str): Name of the upper joint (must be a valid and unique joint name in the current RS3 project if hasUpperJoint is True). Otherwise, the value should be "None".
            - hasLowerJoint (bool): True if a lower joint exists.
            - lowerJointName (str): Name of the lower joint (must be a valid and unique joint name in the current RS3 project if hasLowerJoint is True). Otherwise, the value should be "None".
            - installationStage (int): Stage at which the liner is installed.
            - isRemoved (bool): Whether the liner is removed.
            - removalStage (int): Stage at which the liner is removed; must be -1 if isRemoved is False.

        Notes:
            - If `hasUpperJoint` or `hasLowerJoint` is True, the corresponding joint name must be a valid and uniquely defined joint in RS3.
            - If `isRemoved` is False, `removalStage` must be -1.
            - The first liner in the list is considered the primary liner; its `installationStage` cannot be changed.
            - No two adjacent items in the list may both be joints (i.e., no two consecutive InterfaceData elements).
            - A predecessor liner cannot be removed while any successor liner is still active (installed and not yet removed).
            
        """
        processed_value = []
        for item in value:
            processed_value.append(item.to_tuple())

        request = CompositeLinerDataService_pb2.SetCompositeLinerRequest(
                liningId=self._objectId,
                compositeLiner=[
                    CompositeLinerDataService_pb2.CompositeLiner(
                        linerName=linerName,
                        hasUpperJoint=hasUpperJoint,
                        upperJointName=upperJointName,
                        hasLowerJoint=hasLowerJoint,
                        lowerJointName=lowerJointName,
                        installationStage=installationStage,
                        isRemoved=isRemoved,
                        removalStage=removalStage
                    )
                    for (
                        linerName,
                        hasUpperJoint,
                        upperJointName,
                        hasLowerJoint,
                        lowerJointName,
                        installationStage,
                        isRemoved,
                        removalStage
                    ) in processed_value
                ]
            )

        self._client.callFunction(self._liningCompositionDataService.SetCompositeLiner, request)

    def getLayerCompositionTuple(self) -> list[tuple[str, bool, str, bool, str, int, bool, int]]:
        """
        Retrieves the current composite liner configuration for the object.

        Returns:
            list of tuples: Each tuple represents one layer or joint in the composite liner structure.
            
            The tuple contains the following fields:
                - linerName (str): Name of the liner.
                - hasUpperJoint (bool): Whether an upper joint is present.
                - upperJointName (str): Name of the upper joint if hasUpperJoint is True. Otherwise, it shows as None.
                - hasLowerJoint (bool): Whether a lower joint is present.
                - lowerJointName (str): Name of the lower joint if hasLowerJoint is True. Otherwise, it shows as None.
                - installationStage (int): The construction stage at which the liner is installed.
                - isRemoved (bool): Whether the liner is removed.
                - removalStage (int): The construction stage at which the liner is removed; should be -1 if never get removed.
                
        """
        request = CompositeLinerDataService_pb2.GetCompositeLinerRequest(liningId=self._objectId)
        response : CompositeLinerDataService_pb2.GetCompositeLinerResponse = self._client.callFunction(self._liningCompositionDataService.GetCompositeLiner, request)

        return [(composite.linerName, 
                 composite.hasUpperJoint, 
                 composite.upperJointName if composite.upperJointName != "" else None, 
                 composite.hasLowerJoint, 
                 composite.lowerJointName if composite.lowerJointName != "" else None, 
                 composite.installationStage, 
                 composite.isRemoved, 
                 composite.removalStage) for composite in response.compositeLiner]

    def setLayerCompositionTuple(self, value: list[tuple[str, bool, str, bool, str, int, bool, int]]):
        """
        Sets or updates the composite liner configuration for the object.

        Args:
            value: A list of tuples, each tuple representing a set of one liner and interface element(s) in sequence.
            
            Each tuple must contain:
                - linerName (str): Name of the liner.
                - hasUpperJoint (bool): True if an upper joint exists.
                - upperJointName (str): Name of the upper joint (must be a valid and unique joint name in the current RS3 project if hasUpperJoint is True). Otherwise, the value should be "None".
                - hasLowerJoint (bool): True if a lower joint exists.
                - lowerJointName (str): Name of the lower joint (must be a valid and unique joint name in the current RS3 project if hasLowerJoint is True). Otherwise, the value should be "None".
                - installationStage (int): Stage at which the liner is installed.
                - isRemoved (bool): Whether the liner is removed.
                - removalStage (int): Stage at which the liner is removed; must be -1 if isRemoved is False.

        Notes:
            - If `hasUpperJoint` or `hasLowerJoint` is True, the corresponding joint name must be a valid and uniquely defined joint in RS3.
            - If `isRemoved` is False, `removalStage` must be -1.
            - The first liner in the list is considered the primary liner; its `installationStage` cannot be changed.
            - No two adjacent items in the list may both be joints (i.e., no two consecutive InterfaceData elements).
            - A predecessor liner cannot be removed while any successor liner is still active (installed and not yet removed).
            
        """
        request = CompositeLinerDataService_pb2.SetCompositeLinerRequest(
                liningId=self._objectId,
                compositeLiner=[
                    CompositeLinerDataService_pb2.CompositeLiner(
                        linerName=linerName,
                        hasUpperJoint=hasUpperJoint,
                        upperJointName=upperJointName,
                        hasLowerJoint=hasLowerJoint,
                        lowerJointName=lowerJointName,
                        installationStage=installationStage,
                        isRemoved=isRemoved,
                        removalStage=removalStage
                    )
                    for (
                        linerName,
                        hasUpperJoint,
                        upperJointName,
                        hasLowerJoint,
                        lowerJointName,
                        installationStage,
                        isRemoved,
                        removalStage
                    ) in value
                ]
            )

        self._client.callFunction(self._liningCompositionDataService.SetCompositeLiner, request)
