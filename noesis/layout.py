import javabridge as jb
from .utils import get_class_wrapper, java_collection_to_list

class Layout():

    def __init__(self, layout, *args):
        self.layout = layout
        self.args = args

    def compute(self, network):
        class_wrapper = get_class_wrapper(self.layout, ['noesis.algorithms.visualization'])
        layout = class_wrapper(*self.args)
        att_wrapper = get_class_wrapper('Attribute', ['noesis'])
        x = att_wrapper('x')
        y = att_wrapper('y')
        layout.layout(network.__o__, x, y)
        transform = lambda v: float(v.doubleValue())
        x = java_collection_to_list(x, transform)
        y = java_collection_to_list(y, transform)
        return x, y