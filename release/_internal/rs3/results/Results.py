import rs3.generatedFiles.ResultsQueryService_pb2 as ResultsQueryService
import rs3.generatedFiles.ResultsQueryService_pb2_grpc as ResultsQueryServiceGrpc
from rs3._proxyObject import _ProxyObject
from rs3._client import Client
from typing import Optional
from rs3.results.SolidResults import SolidResults
from rs3.results.BeamResults import BeamResults
from rs3.results.PileForepoleResults import PileForepoleResults
from rs3.results.ResultEnums import SolidsDataType
from rs3.results.CompositeLinerResults import CompositeLinerResults
from rs3.results.JointResults import JointResults
from rs3.results.BoltResults import BoltResults

class NodeInformation:
    def __init__(self, grpcNodeInfo):
        self._grpcNodeInfo = grpcNodeInfo

    @property
    def nodeID(self):
        return self._grpcNodeInfo.nodeID

    @property
    def location(self) -> tuple[float, float, float]:
        loc = self._grpcNodeInfo.location
        return (loc.x, loc.y, loc.z)


class ElementInformation:
    def __init__(self, grpcElementInfo):
        self._grpcElementInfo = grpcElementInfo

    @property
    def elementID(self):
        return self._grpcElementInfo.elementID

    @property
    def nodeIDs(self):
        return self._grpcElementInfo.nodeIDs


class PileForepoleElementInformation:
    def __init__(self, grpcPileForepoleElementInfo):
        self._grpcPileForepoleElementInfo = grpcPileForepoleElementInfo

    @property
    def beamElementID(self):
        return self._grpcPileForepoleElementInfo.beamElementID

    @property
    def interfaceElementID(self):
        return self._grpcPileForepoleElementInfo.interfaceElementID

    @property
    def nodeIDs(self):
        return self._grpcPileForepoleElementInfo.nodeIDs


class SRFValue:
    def __init__(self, grpcSRFValue):
        self._grpcSRFValue = grpcSRFValue

    @property
    def SRF(self):
        return self._grpcSRFValue.srf

    @property
    def MaxTotalDisplacement(self):
        return self._grpcSRFValue.maxTotalDisplacement
    
    @property
    def Converged(self):
        return self._grpcSRFValue.converged


class Results(_ProxyObject):
    """
    Entry point for querying analysis results (nodes, elements, SRF) by stage and SRF value.

    Examples:
        See :ref:`beam_result_example`, :ref:`bolt_result_example`, :ref:`solid_result_example`,
        :ref:`pile_result_example`, :ref:`composite_liner_result_example`, :ref:`joint_result_example`.
    """

    def __init__(self, client : Client, projectID : str):
        super().__init__(client, projectID)
        self._queryService = ResultsQueryServiceGrpc.ResultsQueryServiceStub(self._client.channel)
        self._srfValues = None

    def getResultsAvailability(self, stageNumber: int, srfResultIndex: int = 0):
        '''
        Read cached results for a specific stage and SRF value.
        Parameters:
            stageNumber: int: The analysis stage index (1-based) at which to perform the query.
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 1
                - srfResultIndex is greater than the number of SRF results in the project
        Returns:
            bool: True if results are available, False otherwise.
        '''
        request = ResultsQueryService.ReadResultsByStageSRFRequest(_projectId = self._objectId, stageNumber=stageNumber, srfValueNumber=srfResultIndex)
        response = self._client.callFunction(self._queryService.ReadResultsByStageSRFValue, request)
        return response.resultsAvailable

    def _checkResultsAvailability(self, stageNumber: int, srfResultIndex: int = 0) -> bool:
        if not self.getResultsAvailability(stageNumber, srfResultIndex):
            raise Exception(f"Results are not available for stage {stageNumber} and SRF result index {srfResultIndex}")
        return True

    def _processNodeInformationStream(self, stream, wrapper_class):
        """
        Process streaming node information response chunks and wrap them.
        
        Parameters:
            stream: The streaming RPC response.
            wrapper_class: The class to wrap each node information item.
        
        Returns:
            list: A list of wrapped node information objects.
        
        Raises:
            RuntimeError: If the number of nodes received does not match the expected count.
        """
        allNodes = []
        totalNodesCount = None

        for chunk in stream:
            if chunk.HasField('header'):
                # Process header chunk
                header = chunk.header
                totalNodesCount = header.totalNodesCount
            elif chunk.HasField('data'):
                # Process data chunk
                allNodes.extend(chunk.data.NodesInformation)

        if totalNodesCount != len(allNodes):
            raise RuntimeError(f"Number of nodes received does not match the expected total nodes count. Expected {totalNodesCount}, but received {len(allNodes)}.")

        return list(wrapper_class(n) for n in allNodes)

    def _processElementInformationStream(self, stream, wrapper_class):
        """
        Process streaming element information response chunks and wrap them.
        
        Parameters:
            stream: The streaming RPC response.
            wrapper_class: The class to wrap each element information item.
        
        Returns:
            list: A list of wrapped element information objects.
        
        Raises:
            RuntimeError: If the number of elements received does not match the expected count.
        """
        allElements = []
        totalElementsCount = None

        for chunk in stream:
            if chunk.HasField('header'):
                # Process header chunk
                header = chunk.header
                totalElementsCount = header.totalElementsCount
            elif chunk.HasField('data'):
                # Process data chunk
                allElements.extend(chunk.data.ElementsInformation)

        if totalElementsCount != len(allElements):
            raise RuntimeError(f"Number of elements received does not match the expected total elements count. Expected {totalElementsCount}, but received {len(allElements)}.")

        return list(wrapper_class(e) for e in allElements)

    def queryNodeInfoFromVolume(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on meshed external solid volumes at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromMeshedExternalSolidVolumes(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromBolts(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on bolts at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromBolts(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromBeams(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on beams at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromBeams(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromPilesForepoles(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on piles and forepoles at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromPilesForepoles(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromLiners(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on liners at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromLiners(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromJoints(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on joints at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromJoints(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryNodeInfoFromCompositeLinerInterfaces(self, stageNumber: int) -> list[NodeInformation]:
        """
        Query node information on composite liner interfaces at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[NodeInformation]: A list of node information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.QueryNodeInformationRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryNodeInformationFromCompositeLinerInterfaces(request)
        return self._processNodeInformationStream(stream, NodeInformation)

    def queryElementInfoFromVolume(self, stageNumber: int) -> list[ElementInformation]:
        '''
        Query element information on meshed external solid volumes at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
            stageNumber is less than 1
            stageNumber is greater than the number of stages in the project
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        '''
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromMeshedExternalSolidVolumes(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromBolts(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on bolts at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromBolts(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromBeamsForepolesPiles(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on beams, forepoles, and piles at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromBeamsForepolesPiles(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromLiners(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on liners at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project       
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromLiners(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromJoints(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on joints at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project       
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromJoints(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromCompositeLinerInterfaces(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on composite liner interfaces at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project       
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromCompositeLinerInterfaces(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromBeams(self, stageNumber: int) -> list[ElementInformation]:
        """
        Query element information on beams at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[ElementInformation]: A list of element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromBeams(request)
        return self._processElementInformationStream(stream, ElementInformation)

    def queryElementInfoFromPilesForepoles(self, stageNumber: int) -> list[PileForepoleElementInformation]:
        """
        Query element information on piles and forepoles at a specific stage.

        Parameters:
            stageNumber (int): The analysis stage index (1-based) at which to perform the query.

        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
        Returns:
            list[PileForepoleElementInformation]: A list of pile forepole element information wrappers for the requested stage.
        """
        self._checkResultsAvailability(stageNumber)
        request = ResultsQueryService.ElementInformationQueryRequest(_projectId = self._objectId, stageNumber=stageNumber)
        stream = self._queryService.QueryElementInformationFromPilesForepoles(request)
        return self._processElementInformationStream(stream, PileForepoleElementInformation)

    # SRF Values
    def querySRFValues(self) -> list[SRFValue]:
        """
        Query SRF values at a specific stage.
        """
        if self._srfValues is None:
            self._srfValues = self._querySRFValues()
        return self._srfValues

    def _querySRFValues(self) -> list[SRFValue]:
        """
        Query SRF values at a specific stage.

        Parameters:
            ProjectID (str): The project ID.

        Raises:
            Exception if:
                - projectID is invalid
                - results are not available
        Returns:
            list[SRFValue]: A list of SRF value wrappers for the requested stage.
        """
        request = ResultsQueryService.SRFValuesQueryRequest(_projectId = self._objectId)
        response = self._client.callFunction(self._queryService.QuerySRFValues, request)
        return list(SRFValue(s) for s in response.srfValues)

    # end SRF Values

    def _getMeshResults(self, srfResultIndex: int = 0, stageNumber: int = 1, requiredDataTypes: Optional[set[SolidsDataType]] = None) -> SolidResults:
        '''
        Get the mesh results for a specific stage and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: int: The stage number. Defaults to 1.
            requiredDataTypes: Optional[set[SolidsDataType]]: Optional set of SolidsDataType enum values to check availability for.
                If None or empty, all data types are queried.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
                - Results are not available for the specified stage, SRF value, and data types
        Returns:
            SolidResults: A SolidResults object.
        '''
        return SolidResults.createWithAvailabilityCheck(self._client, self._objectId, stageNumber, srfResultIndex, requiredDataTypes)

    def getMeshResults(self, srfResultIndex: int = 0, stageNumber: list[int] = [1], requiredDataTypes: Optional[set[SolidsDataType]] = None) -> list[SolidResults]:
        '''
        Get the mesh results for specific stages and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: list[int]: The stage number list. Defaults to [1].
            requiredDataTypes: Optional[set[SolidsDataType]]: Optional set of SolidsDataType enum values to check availability for.
                If None or empty, all data types are queried.
        Raises:
            Exception if:
                - a selected stageNumber is less than 1
                - a selected stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
                - Results are not available for the specified stage, SRF value, and data types
        Returns:
            list[SolidResults]: SolidResults objects for the requested stages.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[SolidResults] = []
        for st in stageNumber:
            result_list.append(self._getMeshResults(srfResultIndex, st, requiredDataTypes))
        return result_list

    def getBeamResults(self, srfResultIndex: int = 0, stageNumber: list[int] = [1]) -> list[BeamResults]:
        '''
        Get the beam results for specific stages and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: list[int]: The stage number list. Defaults to [1].
        Raises:
            Exception if:
                - a selected stageNumber is less than 1
                - a selected stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
        Returns:
            list[BeamResults]: BeamResults objects for the requested stages.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[BeamResults] = []
        for st in stageNumber:
            resultsAvailable = self.getResultsAvailability(st, srfResultIndex)
            if not resultsAvailable:
                raise Exception(f"Cached results are not available for stage {st} and SRF result index {srfResultIndex}")
            result_list.append(BeamResults(self._client, self._objectId, st, srfResultIndex))
        return result_list

    def getPileForepoleResults(self, srfResultIndex: int = 0, stageNumber: list[int] = [1]) -> list[PileForepoleResults]:
        '''
        Get the pile forepole results for specific stages and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: list[int]: The stage number list. Defaults to [1].
        Raises:
            Exception if:
                - a selected stageNumber is less than 1
                - a selected stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
        Returns:
            list[PileForepoleResults]: PileForepoleResults objects for the requested stages.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[PileForepoleResults] = []
        for st in stageNumber:
            resultsAvailable = self.getResultsAvailability(st, srfResultIndex)
            if not resultsAvailable:
                raise Exception(f"Cached results are not available for stage {st} and SRF result index {srfResultIndex}")
            result_list.append(PileForepoleResults(self._client, self._objectId, st, srfResultIndex))
        return result_list    

    def getJointResults(self, stageNumber: list[int] = [1], srfResultIndex: int = 0) -> list[JointResults]:
        '''
        Get the joint results for a specific stage and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: int: The stage number. Defaults to 1.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
        Returns:
            JointResults: A JointResults object.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[JointResults] = []
        for stage in stageNumber:
            resultsAvailable = self.getResultsAvailability(stage, srfResultIndex)
            if not resultsAvailable:
                raise Exception(f"Cached results are not available for stage {stage} and SRF result index {srfResultIndex}")

            jointResult = JointResults(self._client, self._objectId, stage, srfResultIndex)
            result_list.append(jointResult)
        return result_list

    def getCompositeLinerResults(self, stageNumber: list[int] = [1], srfResultIndex: int = 0) -> list[CompositeLinerResults]:
        '''
        Get the mesh results for a specific stage and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: int: The stage number. Defaults to 1.
        Raises:
            Exception if:
                - stageNumber is less than 1
                - stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
        Returns:
            CompositeLinerResults: A CompositeLinerResults object.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[CompositeLinerResults] = []
        for stage in stageNumber:
            resultsAvailable = self.getResultsAvailability(stage, srfResultIndex)
            if not resultsAvailable:
                raise Exception(f"Cached results are not available for stage {stage} and SRF result index {srfResultIndex}")

            compositeLinerResult = CompositeLinerResults(self._client, self._objectId, stage, srfResultIndex)
            result_list.append(compositeLinerResult)
        return result_list

    def getBoltResults(self, srfResultIndex: int = 0, stageNumber: list[int] = [1]) -> list[BoltResults]:
        '''
        Get the bolt results for specific stages and SRF value.
        Parameters:
            srfResultIndex: int: The SRF result index. Defaults to 0 to query SRF-None.
            stageNumber: list[int]: The stage number list. Defaults to [1].
        Raises:
            Exception if:
                - a selected stageNumber is less than 1
                - a selected stageNumber is greater than the number of stages in the project
                - srfResultIndex is less than 0
                - srfResultIndex is greater or equal to the number of SRF results in the project
        Returns:   
            list[BoltResults]: BoltResults objects for the requested stages.
        '''
        if not isinstance(stageNumber, list) or len(stageNumber) == 0:
            raise ValueError("stageNumber must be a non-empty list of ints")
        result_list: list[BoltResults] = []
        for st in stageNumber:
            resultsAvailable = self.getResultsAvailability(st, srfResultIndex)
            if not resultsAvailable:
                raise Exception(f"Cached results are not available for stage {st} and SRF result index {srfResultIndex}")
            result_list.append(BoltResults(self._client, self._objectId, st, srfResultIndex))
        return result_list
