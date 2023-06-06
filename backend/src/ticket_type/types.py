from . import caigou
from . import yunwei

ticket_types={
    1:caigou,
    2:yunwei
}

def check_id(i):
        if(i not in ticket_types.keys()):
                raise KeyError('TicketType Id Not In Scope')

def get_schema_by_id(id:int):
        check_id(id)
        import schemas
        m=ticket_types[id]
        return schemas.TicketType(id=id,name=m.name,groups=m.groups,fields=m.fields)

def get_ticket_types_by_id(i):
        check_id(i)
        return ticket_types[i]