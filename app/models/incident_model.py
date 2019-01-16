from datetime import datetime

red_flags_list = []

class Incident:
    def __init__(self, **kwargs):
        self.incident_id = len(red_flags_list) + 1
        self.incident_title = kwargs.get("incident_title")
        self.incident_status = "under_investigation"
        self.created_on = datetime.now()
        self.created_by = kwargs.get("created_by")
        self.location = kwargs.get("location")
        self.images = kwargs.get("images")
        self.videos = kwargs.get("videos")
        self.comment = kwargs.get("comment")

    #fn to return incident dict with proper structure and type not errored
    def incident_struct(self, type):
        if type == "red-flag":
            self.incident_type = "red-flag"
        else:
            self.incident_type = "intervention"

        return {
            "incident_id": self.incident_id,
            "incident_title": self.incident_title,
            "incident_type": self.incident_type,
            "incident_status": self.incident_status,
            "created_on": self.created_on,
            "created_by": self.created_by,
            "location": self.location,
            "images": self.images,
            "videos": self.videos,
            "comment": self.comment
        }

    

