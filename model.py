import pandas as pd
import networkx
from typing import Literal, List
import uuid
from dataclasses import dataclass, field
from shapely import Point, MultiLineString
import pypsa

@dataclass
class BaseEntity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    name: str = ""

class Node(BaseEntity):
    geometry: Point

class Platform(BaseEntity):
    length: float

class Trainstation(Node):
    platforms: List[Platform]
    geometry: Point

class  Track(BaseEntity):
    geometry: MultiLineString
    trackcount: int

class Train(BaseEntity):
    wagon_count: int                
    category: Literal["ICE","IC", "RE", "S", "Cargo"]
    start: Trainstation 
    maximum_passangers: float
    wagon_length:float = 20
    

                  
network = pypsa.Network()
snapshots = pd.date_range(
        start=f"2024-01-01 05:00",
        freq=f"1M",
        periods=60*20,
    )
network.snapshots = snapshots

network