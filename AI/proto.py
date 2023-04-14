# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Communication/AmongUsAI/NNOutput.proto, Recording/DeadBodies/DeadBodiesFrame.proto, Recording/DeadBodies/DeadBodyData.proto, Recording/Frame.proto, Recording/Header/HeaderFrame.proto, Recording/LocalPlayer/LocalPlayerFrame.proto, Recording/Map/DoorData.proto, Recording/Map/MapFrame.proto, Recording/Map/VentData.proto, Recording/MyVector2.proto, Recording/OtherPlayers/OtherPlayerData.proto, Recording/OtherPlayers/OtherPlayersFrame.proto, Recording/PositionData.proto, Recording/Tasks/TaskData.proto, Recording/Tasks/TasksFrame.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    List,
    Optional,
)

import betterproto


class HeaderFrameMapType(betterproto.Enum):
    Unset_MapType = 0
    Skeld = 1
    MiraHQ = 2
    Polus = 3
    Dleks = 4
    Airship = 5


class HeaderFrameRoleType(betterproto.Enum):
    Unset_RoleType = 0
    Crewmate = 1
    Impostor = 2
    Scientist = 3
    Engineer = 4
    GuardianAngel = 5
    Shapeshifter = 6


class TaskDataTaskType(betterproto.Enum):
    Unset = 0
    SubmitScan = 1
    PrimeShields = 2
    FuelEngines = 3
    ChartCourse = 4
    StartReactor = 5
    SwipeCard = 6
    ClearAsteroids = 7
    UploadData = 8
    InspectSample = 9
    EmptyChute = 10
    EmptyGarbage = 11
    AlignEngineOutput = 12
    FixWiring = 13
    CalibrateDistributor = 14
    DivertPower = 15
    UnlockManifolds = 16
    ResetReactor = 17
    FixLights = 18
    CleanO2Filter = 19
    FixComms = 20
    RestoreOxy = 21
    StabilizeSteering = 22
    AssembleArtifact = 23
    SortSamples = 24
    MeasureWeather = 25
    EnterIdCode = 26
    BuyBeverage = 27
    ProcessData = 28
    RunDiagnostics = 29
    WaterPlants = 30
    MonitorOxygen = 31
    StoreArtifacts = 32
    FillCanisters = 33
    ActivateWeatherNodes = 34
    InsertKeys = 35
    ResetSeismic = 36
    ScanBoardingPass = 37
    OpenWaterways = 38
    ReplaceWaterJug = 39
    RepairDrill = 40
    AlignTelescope = 41
    RecordTemperature = 42
    RebootWifi = 43
    PolishRuby = 44
    ResetBreakers = 45
    Decontaminate = 46
    MakeBurger = 47
    UnlockSafe = 48
    SortRecords = 49
    PutAwayPistols = 50
    FixShower = 51
    CleanToilet = 52
    DressMannequin = 53
    PickUpTowels = 54
    RewindTapes = 55
    StartFans = 56
    DevelopPhotos = 57
    GetBiggolSword = 58
    PutAwayRifles = 59
    StopCharles = 60
    VentCleaning = 61


@dataclass(eq=False, repr=False)
class MyVector2(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)


@dataclass(eq=False, repr=False)
class NnOutput(betterproto.Message):
    """TODO: Include more data in the neural network output"""

    desired_move_direction: "MyVector2" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DeadBodyData(betterproto.Message):
    parent_id: int = betterproto.uint32_field(1)
    position: "MyVector2" = betterproto.message_field(2)
    first_seen_time: float = betterproto.float_field(3)
    nearby_players: bytes = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class DeadBodiesFrame(betterproto.Message):
    dead_bodies: List["DeadBodyData"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class HeaderFrame(betterproto.Message):
    map: "HeaderFrameMapType" = betterproto.enum_field(1)
    is_impostor: bool = betterproto.bool_field(2)
    role: "HeaderFrameRoleType" = betterproto.enum_field(3)
    other_impostors: List[int] = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class LocalPlayerFrame(betterproto.Message):
    did_report: bool = betterproto.bool_field(1)
    did_vent: bool = betterproto.bool_field(2)
    did_kill: bool = betterproto.bool_field(3)
    sabotage_used: int = betterproto.uint32_field(4)
    doors_used: int = betterproto.uint32_field(5)
    raycast_obstacle_distances: List[float] = betterproto.float_field(6)
    position: "MyVector2" = betterproto.message_field(7)


@dataclass(eq=False, repr=False)
class PositionData(betterproto.Message):
    total_distance: float = betterproto.float_field(1)
    next_node_position: "MyVector2" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class DoorData(betterproto.Message):
    position: "PositionData" = betterproto.message_field(1)
    is_open: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class VentData(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    position: "PositionData" = betterproto.message_field(2)
    connecting_vents: List["VentDataConnectingVentData"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class VentDataConnectingVentData(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    position: "MyVector2" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MapFrame(betterproto.Message):
    nearby_doors: List["DoorData"] = betterproto.message_field(1)
    nearby_vents: List["VentData"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class OtherPlayerData(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    last_seen_position: "MyVector2" = betterproto.message_field(2)
    last_seen_time: float = betterproto.float_field(3)
    times_saw_vent: int = betterproto.uint32_field(4)
    round_time_visible: float = betterproto.float_field(5)
    game_time_visible: float = betterproto.float_field(6)


@dataclass(eq=False, repr=False)
class OtherPlayersFrame(betterproto.Message):
    last_seen_players: List["OtherPlayerData"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TaskData(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    type: "TaskDataTaskType" = betterproto.enum_field(2)
    consoles_of_interest: List["PositionData"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class TasksFrame(betterproto.Message):
    tasks: List["TaskData"] = betterproto.message_field(1)
    sabotage: Optional["TaskData"] = betterproto.message_field(
        2, optional=True, group="_Sabotage"
    )


@dataclass(eq=False, repr=False)
class Frame(betterproto.Message):
    dead_bodies: Optional["DeadBodiesFrame"] = betterproto.message_field(
        1, optional=True, group="_DeadBodies"
    )
    header: Optional["HeaderFrame"] = betterproto.message_field(
        2, optional=True, group="_Header"
    )
    local_player: Optional["LocalPlayerFrame"] = betterproto.message_field(
        3, optional=True, group="_LocalPlayer"
    )
    map: Optional["MapFrame"] = betterproto.message_field(
        4, optional=True, group="_Map"
    )
    other_players: Optional["OtherPlayersFrame"] = betterproto.message_field(
        5, optional=True, group="_OtherPlayers"
    )
    tasks: Optional["TasksFrame"] = betterproto.message_field(
        6, optional=True, group="_Tasks"
    )
