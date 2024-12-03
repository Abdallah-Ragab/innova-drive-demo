class Validator:
    def validate(source):
        raise NotImplementedError("validate method not implemented")

class VideoSourceValidator(Validator):
    def validate(source):
        valid_path = os.path.exists(source)
        if not valid_path:
            raise ValueError(f"Invalid video source path: {source}")
        return True

class CameraSourceValidator(Validator):
    def validate(source):
        # check with opencv if if camera with id exists
        valid_camera = cv2.VideoCapture(source).isOpened()        
        if not valid_camera:
            raise ValueError(f"Invalid camera source: {source}")
        return True
