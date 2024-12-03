from lib.frame.source.validator import VideoSourceValidator, CameraSourceValidator

__all__ = ["Source", "SourceType"]

class SourceType(enum.Enum):
    VIDEO = "VIDEO"
    CAMERA = "DEVICE"
    
class Source:
    # initiate a source obj, set its type and validate it
    def __init__(self, source):
        self.source = source
        self.set_type()
        self.validate_source()
        self.set_validators()   
    
    def __str__(self):
        return f"Source[{self.type}]: {self.source}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.source == other.source and self.type == other.type
    
    def __dict__(self):
        return {
            "source": self.source,
            "type": self.type
        }
    
    def set_type(self):
        _type = type(self.source)
        if _type == str:
            self.type = SourceType.VIDEO
        elif _type == int:
            self.type = SourceType.CAMERA
        else:
            raise ValueError(f"Invalid source type. provided:{_type}. available types: (str) for video file path, (int) for camera device id")
    
    def set_validators(self):
        if self.type == SourceType.VIDEO:
            self.validators = [VideoSourceValidator]
        elif self.type == SourceType.CAMERA:
            self.validators = [CameraSourceValidator]
    
    def validate_source(self):
        for validator in self.validators:
            validator.validate(self.source)