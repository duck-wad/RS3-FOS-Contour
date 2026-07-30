from dataclasses import dataclass
import rs3.generatedFiles.CommonGeometryMessages_pb2 as CommonGeometryMessages

class Geometry:
    pass

@dataclass
class Point(Geometry):
    x: float
    y: float
    z: float
    
    def toCommonGeometryObject(self):
        point_ = CommonGeometryMessages.Point(x=self.x, y=self.y, z=self.z)
        geometry_ = CommonGeometryMessages.Geometry(point=point_)
        return geometry_

@dataclass
class Polyline(Geometry):
    points: list[Point]
    
    def toCommonGeometryObject(self):
        points_ = [CommonGeometryMessages.Point(x=p.x, y=p.y, z=p.z) for p in self.points]
        polyline_ = CommonGeometryMessages.Polyline(point=points_)
        geometry_ = CommonGeometryMessages.Geometry(polyline=polyline_)
        return geometry_

@dataclass
class Cube(Geometry):
    """
    Represents a 3D cube defined by two opposite corners and optional rotations.

    The rotation angles (rotationAboutX, rotationAboutY, rotationAboutZ) are in degrees
    and follow the **right-hand rule** for positive direction. i.e., positive rotation
    is counterclockwise when looking along the axis toward the origin.
    """
    corner1: Point
    corner2: Point
    rotationAboutX: float = 0
    rotationAboutY: float = 0
    rotationAboutZ: float = 0

    def toCommonGeometryObject(self):
        corner1_ = CommonGeometryMessages.Point(x=self.corner1.x, y=self.corner1.y, z=self.corner1.z)
        corner2_ = CommonGeometryMessages.Point(x=self.corner2.x, y=self.corner2.y, z=self.corner2.z)
        box_ = CommonGeometryMessages.Box(corner1=corner1_, corner2=corner2_, rotationAboutX=self.rotationAboutX, rotationAboutY=self.rotationAboutY, rotationAboutZ=self.rotationAboutZ)
        geometry_ = CommonGeometryMessages.Geometry(box=box_)
        return geometry_
    
@dataclass
class Cylinder(Geometry):
    axisStartPoint: Point
    axisEndPoint: Point
    radius: float
    
    def toCommonGeometryObject(self):
        axisStartPoint_ = CommonGeometryMessages.Point(x=self.axisStartPoint.x, y=self.axisStartPoint.y, z=self.axisStartPoint.z)
        axisEndPoint_ = CommonGeometryMessages.Point(x=self.axisEndPoint.x, y=self.axisEndPoint.y, z=self.axisEndPoint.z)
        radius_ = self.radius
        cylinder_ = CommonGeometryMessages.Cylinder(axisStartPoint=axisStartPoint_, axisEndPoint=axisEndPoint_, radius=radius_)
        geometry_ = CommonGeometryMessages.Geometry(cylinder=cylinder_)
        return geometry_

@dataclass
class Sphere(Geometry):
    center: Point
    radius: float
    
    def toCommonGeometryObject(self):
        center_ = CommonGeometryMessages.Point(x=self.center.x, y=self.center.y, z=self.center.z)
        radius_ = self.radius
        sphere_ = CommonGeometryMessages.Sphere(center=center_, radius=radius_)
        geometry_ = CommonGeometryMessages.Geometry(sphere=sphere_)
        return geometry_