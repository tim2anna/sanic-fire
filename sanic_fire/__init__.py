import fire
from sanic_fire.core import command_base


def cmd(component=None, command=None, name='cmd'):
    if component is None:
        context = {}
        context.update(command_base.func_dict)
        context.update(command_base.class_dict)
        return fire.Fire(context, command, name)
    else:
        return fire.Fire(component, command, name)
