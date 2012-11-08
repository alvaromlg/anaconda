from chowdren.writers.objects import ObjectWriter

from chowdren.common import (get_image_name, get_animation_name, to_c,
    make_color)

from chowdren.writers.events import (StaticActionWriter, StaticConditionWriter, 
    StaticExpressionWriter, make_table)

class WindowControl(ObjectWriter):
    class_name = 'WindowControl'
    static = True

actions = make_table(StaticActionWriter, {
    21 : 'set_focus(true)'
})

conditions = make_table(StaticConditionWriter, {
    4 : 'has_focus'
})

expressions = make_table(StaticExpressionWriter, {
})

def get_object():
    return WindowControl