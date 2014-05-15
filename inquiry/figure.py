from .helpers import *
from .garden import Garden
from .results import FigureResult


class Figure(object):
    __slots__ = ("id", "title", "help", "outline", "alias", "seed")

    def __init__(self, id, figure):
        self.id = id
        self.title = figure.pop('title') if 'title' in figure else None
        self.help = figure.pop('help') if 'help' in figure else None
        self.outline = figure.pop('outline')
        self.alias = array(figure.pop('alias')) if 'alias' in figure else []
        self.seed = figure

    def _process(self, inquiry, paths, userkwargs):
        # filter out empty paths and generate a garden
        garden = Garden(self, [p for p in paths if p])
        # water down the garden with user arguments
        query, period = garden.harvest(inquiry, userkwargs)
        # return a FigureResults
        return FigureResult(inquiry, query, period)
