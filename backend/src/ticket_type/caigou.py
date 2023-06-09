name='采购工单'

groups=['后勤','领导','运维']

fields={}

fields['后勤']=[
    {
        "type": "input",
        "inputType": "text",
        "label": "ID",
        "model": "id",
        "readonly": True,
        "featured": False,
        "disabled": True
    }, {
        "type": "input",
        "inputType": "text",
        "label": "Name",
        "model": "name",
        "readonly": False,
        "featured": True,
        "required": True,
        "disabled": True,
        "placeholder": "User's name"
    }]

fields['领导']=[
    {
        "type": "input",
        "inputType": "password",
        "label": "Password",
        "model": "password",
        "min": 6,
        "required": True,
        "hint": "Minimum 6 characters"
    }, {
        "type": "input",
        "inputType": "number",
        "label": "Age",
        "model": "age",
        "min": 18
    }, {
        "type": "input",
        "inputType": "email",
        "label": "E-mail",
        "model": "email",
        "placeholder": "User's e-mail address"
    }
]

fields['运维']=[
    {
        'type': "checklist",
        "label": "Skills",
        "model": "skills",
        "multi": True,
        "required": True,
        "multiSelect": True,
        "values": ["HTML5", "Javascript", "CSS3", "CoffeeScript", "AngularJS", "ReactJS", "VueJS"]
    }, {
        "type": "switch",
        "label": "Status",
        "model": "status",
        "multi": True,
        "readonly": False,
        "featured": False,
        "disabled": False,
        "default": True,
        "textOn": "Active",
        "textOff": "Inactive"
    }]

displays={}

for g in groups:
    displays[g] = [{"label":f['label'],"model":f['model']} for f in fields[g]]

def postHandler(s,M):
    if s=='后勤':
        return ('领导',M)
    elif s=='领导':
        if M['驳回']:
            return ('后勤',M)
        else:
            return ('运维',M)
    elif s=='运维':
        return ('归档',M)
    else:
        raise Exception('有问题的状态')
