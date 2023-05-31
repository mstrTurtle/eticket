from . import caigou
from . import yunwei

ticket_types={
    1:caigou,
    2:yunwei
}

def get_schema_by_id(id:int):
        import schemas
        m=ticket_types[id]
        return schemas.TicketType(id=id,name=m.name,groups=m.groups,fields=m.fields)