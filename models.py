from pydantic import BaseModel 

class HVACDetials(BaseModel):
    number_of_peoples_inside : int 
    camera_id                : int 
    area_covered             : float 
    