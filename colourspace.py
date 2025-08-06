# -*- coding: utf-8 -*-

__author__ = "Gilles Ferrand (RIKEN)"
__version__ = "1.3"


try:
    from . import convert
    from . import gamut
    from . import limits
    from . import slices
    from . import maps
except ImportError:
    # Fallback for direct execution
    import convert
    import limits
    import gamut
    import slices
    import maps