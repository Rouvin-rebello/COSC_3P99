import os
import sys
import random

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'src'
        )
    )
)

from ataque import AtaqueNormal, AtaqueStrategy
